import hashlib
import random
from ctypes import c_uint32
from typing import Any, Dict, List, Tuple, Union

import assist
import numpy as np
import numpy.typing as npt
import pyarrow as pa
import pyarrow.compute as pc
import quivr as qv
import rebound
from adam_core.constants import KM_P_AU
from adam_core.constants import Constants as c
from adam_core.coordinates import (
    CartesianCoordinates,
    Origin,
    OriginCodes,
    SphericalCoordinates,
    transform_coordinates,
)
from adam_core.dynamics.impacts import CollisionConditions, CollisionEvent, ImpactMixin
from adam_core.orbits import Orbits
from adam_core.orbits.variants import VariantOrbits
from adam_core.time import Timestamp
from jpl_small_bodies_de441_n16 import de441_n16
from naif_de440 import de440
from quivr.concat import concatenate

from adam_core.propagator.propagator import OrbitType, Propagator, TimestampType

C = c.C

try:
    from adam_assist.version import __version__
except ImportError:
    __version__ = "0.0.0"

# Use the Earth's equatorial radius as used in DE4XX ephemerides
# adam_core defines it in au but we need it in km
EARTH_RADIUS_KM = c.R_EARTH_EQUATORIAL * KM_P_AU


def uint32_hash(s: str) -> c_uint32:
    sha256_result = hashlib.sha256(s.encode()).digest()
    # Get the first 4 bytes of the SHA256 hash to obtain a uint32 value.
    return c_uint32(int.from_bytes(sha256_result[:4], byteorder="big"))


def hash_orbit_ids_to_uint32(
    # orbit_ids: np.ndarray[Tuple[np.dtype[np.int_]], np.dtype[np.str_]],
    orbit_ids: npt.NDArray[np.str_],
) -> Tuple[Dict[int, str], List[c_uint32]]:
    """
    Derive uint32 hashes from orbit id strigns

    Rebound uses uint32 to track individual particles, but we use orbit id strings.
    Here we attempt to generate uint32 hashes for each and return the mapping as well.
    """
    hashes = [uint32_hash(o) for o in orbit_ids]
    # Because uint32 is an unhashable type,
    # we use a dict mapping from uint32 to orbit id string
    mapping = {hashes[i].value: orbit_ids[i] for i in range(len(orbit_ids))}

    return mapping, hashes


def generate_unique_separator(
    *string_arrays: npt.NDArray[np.str_],
    alphabet: str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789",
    length: int = 4,
) -> str:
    """
    Generate a random string of specified length that is not present as a substring in any of the input arrays.
    All characters in the generated string will be different to prevent misplaced substring matches when splitting.

    Parameters
    ----------
    *string_arrays : npt.NDArray[np.str_]
        One or more numpy arrays of strings to check against
    alphabet : str, optional
        Characters to use for generating the random string, by default includes letters and digits
    length : int, optional
        Length of the random string to generate, by default 4

    Returns
    -------
    str
        A random string that is not present as a substring in any of the input arrays

    Raises
    ------
    ValueError
        If unable to generate a unique string after many attempts
    """
    # Combine all arrays into a single numpy array for vectorized operations
    all_strings = (
        np.concatenate([arr.astype(str) for arr in string_arrays])
        if string_arrays
        else np.array([])
    )

    max_attempts = 1000
    for _ in range(max_attempts):
        # Generate a random string with all different characters
        chars = random.sample(alphabet, length)
        candidate = "".join(chars)

        # Vectorized substring check using numpy
        if len(all_strings) == 0:
            return candidate

        # Use numpy's vectorized string operations for faster substring checking
        contains_candidate = np.char.find(all_strings, candidate) >= 0
        if not np.any(contains_candidate):
            return candidate

    raise ValueError(
        f"Could not generate a unique {length}-character string after {max_attempts} attempts"
    )


class ASSISTPropagator(Propagator, ImpactMixin):  # type: ignore

    def __init__(
        self,
        *args: object,  # Generic type for arbitrary positional arguments
        min_dt: float = 1e-9,
        initial_dt: float = 1e-6,
        adaptive_mode: int = 1,
        epsilon: float = 1e-6,
        **kwargs: object,  # Generic type for arbitrary keyword arguments
    ) -> None:
        super().__init__(*args, **kwargs)
        if min_dt <= 0:
            raise ValueError("min_dt must be positive")
        if initial_dt <= 0:
            raise ValueError("initial_dt must be positive")
        if min_dt > initial_dt:
            raise ValueError("min_dt must be smaller than initial_dt")
        self.min_dt = min_dt
        self.initial_dt = initial_dt
        self.adaptive_mode = adaptive_mode
        self.epsilon = epsilon

    def __getstate__(self) -> Dict[str, Any]:
        state = self.__dict__.copy()
        state.pop("_last_simulation", None)
        return state

    def __setstate__(self, state: Dict[str, Any]) -> None:
        self.__dict__.update(state)

    def _propagate_orbits(self, orbits: OrbitType, times: TimestampType) -> OrbitType:
        """
        Propagate the orbits to the specified times.
        """
        # OPTIMIZATION: Fast path for single orbits
        if len(orbits) == 1:
            return self._propagate_single_orbit_optimized(orbits, times)

        # The coordinate frame is the equatorial International Celestial Reference Frame (ICRF).
        # This is also the native coordinate system for the JPL binary files.
        # For units we use solar masses, astronomical units, and days.
        # The time coordinate is Barycentric Dynamical Time (TDB) in Julian days.
        # Convert coordinates to ICRF using TDB time
        transformed_coords = transform_coordinates(
            orbits.coordinates,
            origin_out=OriginCodes.SOLAR_SYSTEM_BARYCENTER,
            frame_out="equatorial",
        )
        transformed_input_orbit_times = transformed_coords.time.rescale("tdb")
        transformed_coords = transformed_coords.set_column(
            "time", transformed_input_orbit_times
        )
        transformed_orbits = orbits.set_column("coordinates", transformed_coords)

        # Group orbits by unique time, then propagate them
        results = None
        unique_times = transformed_orbits.coordinates.time.unique()
        for epoch in unique_times:
            mask = transformed_orbits.coordinates.time.equals(epoch)
            epoch_orbits = transformed_orbits.apply_mask(mask)
            propagated_orbits = self._propagate_orbits_inner(epoch_orbits, times)
            if results is None:
                results = propagated_orbits
            else:
                results = concatenate([results, propagated_orbits])

        # Sanity check that the results are of the correct type
        assert isinstance(results, OrbitType)

        return results

    def _propagate_single_orbit_optimized(
        self, orbit: OrbitType, times: TimestampType
    ) -> OrbitType:
        """
        Optimized propagation for a single orbit, bypassing grouping overhead.
        """
        # Validate assumption
        if len(orbit) != 1:
            raise ValueError(f"Expected exactly 1 orbit, got {len(orbit)}")

        # Transform coordinates directly without grouping
        transformed_coords = transform_coordinates(
            orbit.coordinates,
            origin_out=OriginCodes.SOLAR_SYSTEM_BARYCENTER,
            frame_out="equatorial",
        )
        transformed_input_orbit_times = transformed_coords.time.rescale("tdb")
        transformed_coords = transformed_coords.set_column(
            "time", transformed_input_orbit_times
        )
        transformed_orbit = orbit.set_column("coordinates", transformed_coords)

        return self._propagate_single_orbit_inner_optimized(transformed_orbit, times)

    def _propagate_single_orbit_inner_optimized(
        self, orbit: OrbitType, times: TimestampType
    ) -> OrbitType:
        """
        Inner propagation optimized for exactly one orbit.
        """
        # Setup ephemeris and simulation
        ephem = assist.Ephem(planets_path=de440, asteroids_path=de441_n16)
        sim = rebound.Simulation()

        start_tdb_time = orbit.coordinates.time.jd().to_numpy()[0]
        sim.t = start_tdb_time - ephem.jd_ref

        # Handle particle ID creation (optimized for single orbit)
        is_variant = isinstance(orbit, VariantOrbits)
        if is_variant:
            orbit_id = str(orbit.orbit_id.to_numpy(zero_copy_only=False)[0])
            variant_id = str(orbit.variant_id.to_numpy(zero_copy_only=False)[0])
            particle_hash = uint32_hash(f"{orbit_id}\x1f{variant_id}")
        else:
            orbit_id = str(orbit.orbit_id.to_numpy(zero_copy_only=False)[0])
            particle_hash = uint32_hash(orbit_id)

        assist.Extras(sim, ephem)

        # Add single particle
        coords = orbit.coordinates
        position_arrays = coords.r
        velocity_arrays = coords.v

        sim.add(
            x=position_arrays[0, 0],
            y=position_arrays[0, 1],
            z=position_arrays[0, 2],
            vx=velocity_arrays[0, 0],
            vy=velocity_arrays[0, 1],
            vz=velocity_arrays[0, 2],
            hash=particle_hash,
        )

        # Set integrator parameters
        sim.dt = self.initial_dt
        sim.ri_ias15.min_dt = self.min_dt
        sim.ri_ias15.adaptive_mode = self.adaptive_mode
        sim.ri_ias15.epsilon = self.epsilon

        # Prepare integration times (numpy only)
        integrator_times = times.rescale("tdb").jd().to_numpy()
        integrator_times = integrator_times - ephem.jd_ref

        # Integration loop (preallocate state array)
        N = len(integrator_times)
        if N == 0:
            return VariantOrbits.empty() if is_variant else Orbits.empty()

        xyzvxvyvz = np.zeros((N, 6), dtype="float64")
        scratch = np.zeros((1, 6), dtype="float64")

        for i in range(N):
            sim.integrate(integrator_times[i])
            scratch.fill(0.0)
            sim.serialize_particle_data(xyzvxvyvz=scratch)
            xyzvxvyvz[i, :] = scratch[0, :]

        # Build results
        jd_times = integrator_times + ephem.jd_ref
        times_out = Timestamp.from_jd(jd_times, scale="tdb")
        origin_codes = Origin.from_kwargs(
            code=pa.repeat("SOLAR_SYSTEM_BARYCENTER", xyzvxvyvz.shape[0])
        )

        if is_variant:
            orbit_ids_out = [orbit_id] * N
            variant_ids_out = [variant_id] * N
            object_id_out = np.tile(orbit.object_id.to_numpy(zero_copy_only=False), N)

            return VariantOrbits.from_kwargs(
                orbit_id=orbit_ids_out,
                variant_id=variant_ids_out,
                object_id=object_id_out,
                weights=orbit.weights,
                weights_cov=orbit.weights_cov,
                coordinates=CartesianCoordinates.from_kwargs(
                    x=xyzvxvyvz[:, 0],
                    y=xyzvxvyvz[:, 1],
                    z=xyzvxvyvz[:, 2],
                    vx=xyzvxvyvz[:, 3],
                    vy=xyzvxvyvz[:, 4],
                    vz=xyzvxvyvz[:, 5],
                    time=times_out,
                    origin=origin_codes,
                    frame="equatorial",
                ),
            )
        else:
            orbit_ids_out = [orbit_id] * N
            object_id_out = np.tile(orbit.object_id.to_numpy(zero_copy_only=False), N)

            return Orbits.from_kwargs(
                coordinates=CartesianCoordinates.from_kwargs(
                    x=xyzvxvyvz[:, 0],
                    y=xyzvxvyvz[:, 1],
                    z=xyzvxvyvz[:, 2],
                    vx=xyzvxvyvz[:, 3],
                    vy=xyzvxvyvz[:, 4],
                    vz=xyzvxvyvz[:, 5],
                    time=times_out,
                    origin=origin_codes,
                    frame="equatorial",
                ),
                orbit_id=orbit_ids_out,
                object_id=object_id_out,
            )

    def _propagate_orbits_inner(
        self, orbits: OrbitType, times: TimestampType
    ) -> OrbitType:
        """
        Propagates one or more orbits with the same epoch to the specified times.
        """
        ephem = assist.Ephem(
            planets_path=de440,
            asteroids_path=de441_n16,
        )
        sim = None
        sim = rebound.Simulation()

        # Set the simulation time, relative to the jd_ref
        start_tdb_time = orbits.coordinates.time.jd().to_numpy()[0]
        start_tdb_time = start_tdb_time - ephem.jd_ref
        sim.t = start_tdb_time

        particle_ids = orbits.orbit_id.to_numpy(zero_copy_only=False)
        separator = None

        # Serialize the variantorbit
        if isinstance(orbits, VariantOrbits):
            orbit_ids = orbits.orbit_id.to_numpy(zero_copy_only=False).astype(str)
            variant_ids = orbits.variant_id.to_numpy(zero_copy_only=False).astype(str)

            # Generate a unique separator that doesn't appear in either array
            separator = generate_unique_separator(orbit_ids, variant_ids)

            # Use numpy string operations to concatenate the orbit_id and variant_id
            particle_ids = np.char.add(
                np.char.add(orbit_ids, np.repeat(separator, len(orbit_ids))),
                variant_ids,
            )
            particle_ids = np.array(particle_ids, dtype="object")

        orbit_id_mapping, uint_orbit_ids = hash_orbit_ids_to_uint32(particle_ids)
        hash_to_index = {uint_orbit_ids[i].value: i for i in range(len(uint_orbit_ids))}

        # Add the orbits as particles to the simulation
        # OPTIMIZED: Use direct array access instead of DataFrame conversion
        coords = orbits.coordinates
        position_arrays = coords.r  # x, y, z columns
        velocity_arrays = coords.v  # vx, vy, vz columns

        assist.Extras(sim, ephem)

        for i in range(len(position_arrays)):
            sim.add(
                x=position_arrays[i, 0],
                y=position_arrays[i, 1],
                z=position_arrays[i, 2],
                vx=velocity_arrays[i, 0],
                vy=velocity_arrays[i, 1],
                vz=velocity_arrays[i, 2],
                hash=uint_orbit_ids[i],
            )

        # Set the integrator parameters
        sim.dt = self.initial_dt
        sim.ri_ias15.min_dt = self.min_dt
        sim.ri_ias15.adaptive_mode = self.adaptive_mode
        sim.ri_ias15.epsilon = self.epsilon

        # Prepare the times as jd - jd_ref
        integrator_times = times.rescale("tdb").jd()
        integrator_times = pc.subtract(integrator_times, ephem.jd_ref)
        integrator_times = integrator_times.to_numpy()

        # Unified accumulation for both Orbits and VariantOrbits
        results = None
        is_variant = isinstance(orbits, VariantOrbits)
        step_states: List[npt.NDArray[np.float64]] = []
        step_orbit_ids: List[npt.NDArray[np.object_]] = []
        step_variant_ids: List[npt.NDArray[np.object_]] = []

        # Step through each time, move the simulation forward and collect state
        for i in range(len(integrator_times)):
            sim.integrate(integrator_times[i])

            orbit_id_hashes = np.zeros(sim.N, dtype="uint32")
            step_xyzvxvyvz = np.zeros((sim.N, 6), dtype="float64")
            sim.serialize_particle_data(xyzvxvyvz=step_xyzvxvyvz, hash=orbit_id_hashes)

            step_states.append(step_xyzvxvyvz)

            if is_variant:
                indices = np.fromiter(
                    (hash_to_index[h] for h in orbit_id_hashes),
                    dtype=np.int64,
                    count=sim.N,
                )
                step_orbit_ids.append(orbit_ids[indices])
                step_variant_ids.append(variant_ids[indices])
            else:
                indices = np.fromiter(
                    (hash_to_index[h] for h in orbit_id_hashes),
                    dtype=np.int64,
                    count=sim.N,
                )
                step_orbit_ids.append(particle_ids[indices])

        # Build a single result table
        if len(step_states) == 0:
            results = VariantOrbits.empty() if is_variant else Orbits.empty()
        else:
            xyzvxvyvz = np.concatenate(step_states, axis=0)
            jd_times = integrator_times + ephem.jd_ref
            times_out = Timestamp.from_jd(np.repeat(jd_times, sim.N), scale="tdb")
            origin_codes = Origin.from_kwargs(
                code=pa.repeat("SOLAR_SYSTEM_BARYCENTER", xyzvxvyvz.shape[0])
            )

            if is_variant:
                orbit_ids_out = np.concatenate(step_orbit_ids, axis=0)
                variant_ids_out = np.concatenate(step_variant_ids, axis=0)
                object_id_out = np.tile(
                    orbits.object_id.to_numpy(zero_copy_only=False),
                    len(integrator_times),
                )

                results = VariantOrbits.from_kwargs(
                    orbit_id=orbit_ids_out,
                    variant_id=variant_ids_out,
                    object_id=object_id_out,
                    weights=orbits.weights,
                    weights_cov=orbits.weights_cov,
                    coordinates=CartesianCoordinates.from_kwargs(
                        x=xyzvxvyvz[:, 0],
                        y=xyzvxvyvz[:, 1],
                        z=xyzvxvyvz[:, 2],
                        vx=xyzvxvyvz[:, 3],
                        vy=xyzvxvyvz[:, 4],
                        vz=xyzvxvyvz[:, 5],
                        time=times_out,
                        origin=origin_codes,
                        frame="equatorial",
                    ),
                )
            else:
                orbit_ids_out = np.concatenate(step_orbit_ids, axis=0)
                object_id_out = np.tile(
                    orbits.object_id.to_numpy(zero_copy_only=False),
                    len(integrator_times),
                )

                results = Orbits.from_kwargs(
                    coordinates=CartesianCoordinates.from_kwargs(
                        x=xyzvxvyvz[:, 0],
                        y=xyzvxvyvz[:, 1],
                        z=xyzvxvyvz[:, 2],
                        vx=xyzvxvyvz[:, 3],
                        vy=xyzvxvyvz[:, 4],
                        vz=xyzvxvyvz[:, 5],
                        time=times_out,
                        origin=origin_codes,
                        frame="equatorial",
                    ),
                    orbit_id=orbit_ids_out,
                    object_id=object_id_out,
                )

        # Store the last simulation in a private variable for reference
        self._last_simulation = sim
        return results

    def _detect_collisions(
        self,
        orbits: OrbitType,
        num_days: int,
        conditions: CollisionConditions,
    ) -> Tuple[VariantOrbits, CollisionEvent]:
        # Assert that the time for each orbit definition is the same for the simulator to work
        assert len(pc.unique(orbits.coordinates.time.mjd())) == 1

        # The coordinate frame is the equatorial International Celestial Reference Frame (ICRF).
        # This is also the native coordinate system for the JPL binary files.
        # For units we use solar masses, astronomical units, and days.
        # The time coordinate is Barycentric Dynamical Time (TDB) in Julian days.

        # KK Note: do we want to specify the version of spice kernels that were used- if we're doing
        # addtional work down stream, to ensure that the same kernels are used? de440, 441 for asteroid position

        coords = transform_coordinates(
            orbits.coordinates,
            origin_out=OriginCodes.SOLAR_SYSTEM_BARYCENTER,
            frame_out="equatorial",
        )
        input_orbit_times = coords.time.rescale("tdb")
        coords = coords.set_column("time", input_orbit_times)
        orbits = orbits.set_column("coordinates", coords)

        ephem = assist.Ephem(
            planets_path=de440,
            asteroids_path=de441_n16,
        )
        sim = None
        sim = rebound.Simulation()

        # Set the simulation time, relative to the jd_ref
        start_tdb_time = orbits.coordinates.time.jd().to_numpy()[0]
        start_tdb_time = start_tdb_time - ephem.jd_ref
        sim.t = start_tdb_time

        backward_propagation = num_days < 0
        if backward_propagation:
            sim.dt = sim.dt * -1

        particle_ids = orbits.orbit_id.to_numpy(zero_copy_only=False)
        separator = None

        # Serialize the variantorbit
        if isinstance(orbits, VariantOrbits):
            orbit_ids = orbits.orbit_id.to_numpy(zero_copy_only=False).astype(str)
            variant_ids = orbits.variant_id.to_numpy(zero_copy_only=False).astype(str)

            # Generate a unique separator that doesn't appear in either array
            separator = generate_unique_separator(orbit_ids, variant_ids)

            # Use numpy string operations to concatenate the orbit_id and variant_id
            particle_ids = np.char.add(
                np.char.add(orbit_ids, np.repeat(separator, len(orbit_ids))),
                variant_ids,
            )
            particle_ids = np.array(particle_ids, dtype="object")

        orbit_id_mapping, uint_orbit_ids = hash_orbit_ids_to_uint32(particle_ids)
        {uint_orbit_ids[i].value: i for i in range(len(uint_orbit_ids))}

        # Add the orbits as particles to the simulation
        # OPTIMIZED: Use direct array access instead of DataFrame conversion
        coords = orbits.coordinates
        position_arrays = coords.r  # x, y, z columns
        velocity_arrays = coords.v  # vx, vy, vz columns

        assist.Extras(sim, ephem)

        for i in range(len(position_arrays)):
            sim.add(
                x=position_arrays[i, 0],
                y=position_arrays[i, 1],
                z=position_arrays[i, 2],
                vx=velocity_arrays[i, 0],
                vy=velocity_arrays[i, 1],
                vz=velocity_arrays[i, 2],
                hash=uint_orbit_ids[i],
            )

        # Prepare the times as jd - jd_ref
        final_integrator_time = (
            orbits.coordinates.time.add_days(num_days).jd().to_numpy()[0]
        )
        final_integrator_time = final_integrator_time - ephem.jd_ref

        # Results stores the final positions of the objects
        # If an object is an impactor, this represents its position at impact time
        results = None
        collision_events = CollisionEvent.empty()
        # Accumulators to reduce per-iteration concatenation
        collisions_list: List[CollisionEvent] = []
        colliders_list: List[OrbitType] = []
        results_list: List[OrbitType] = []
        past_integrator_time = False
        time_step_results: Union[None, OrbitType] = None

        # Set the integrator parameters
        sim.dt = self.initial_dt
        sim.ri_ias15.min_dt = self.min_dt
        sim.ri_ias15.adaptive_mode = self.adaptive_mode
        sim.ri_ias15.epsilon = self.epsilon

        if backward_propagation:
            sim.dt = sim.dt * -1

        # Step through each time, move the simulation forward and
        # collect the results. End if all orbits are removed from
        # the simulation or the final integrator time is reached.
        while past_integrator_time is False and len(orbits) > 0:
            sim.steps(1)
            if (sim.t >= final_integrator_time and not backward_propagation) or (
                backward_propagation and sim.t <= final_integrator_time
            ):
                past_integrator_time = True

            # Get serialized particle data as numpy arrays
            orbit_id_hashes = np.zeros(sim.N, dtype="uint32")
            step_xyzvxvyvz = np.zeros((sim.N, 6), dtype="float64")

            sim.serialize_particle_data(xyzvxvyvz=step_xyzvxvyvz, hash=orbit_id_hashes)

            if isinstance(orbits, Orbits):
                # Retrieve original orbit id from hash
                orbit_ids = [orbit_id_mapping[h] for h in orbit_id_hashes]
                time_step_results = Orbits.from_kwargs(
                    coordinates=CartesianCoordinates.from_kwargs(
                        x=step_xyzvxvyvz[:, 0],
                        y=step_xyzvxvyvz[:, 1],
                        z=step_xyzvxvyvz[:, 2],
                        vx=step_xyzvxvyvz[:, 3],
                        vy=step_xyzvxvyvz[:, 4],
                        vz=step_xyzvxvyvz[:, 5],
                        time=Timestamp.from_jd(
                            pa.repeat(sim.t + ephem.jd_ref, sim.N), scale="tdb"
                        ),
                        origin=Origin.from_kwargs(
                            code=pa.repeat(
                                "SOLAR_SYSTEM_BARYCENTER",
                                sim.N,
                            )
                        ),
                        frame="equatorial",
                    ),
                    orbit_id=orbit_ids,
                    object_id=orbits.object_id,
                )
            elif isinstance(orbits, VariantOrbits):
                # Retrieve the orbit id and weights from hash
                particle_ids = [orbit_id_mapping[h] for h in orbit_id_hashes]

                orbit_ids, variant_ids = zip(
                    *[particle_id.split(separator) for particle_id in particle_ids]
                )

                # Historically we've done a check here to make sure the orbit of the orbits
                # and serialized particles is consistent
                # np.testing.assert_array_equal(orbits.orbit_id.to_numpy(zero_copy_only=False).astype(str), orbit_ids)
                # np.testing.assert_array_equal(orbits.variant_id.to_numpy(zero_copy_only=False).astype(str), variant_ids)

                time_step_results = VariantOrbits.from_kwargs(
                    orbit_id=orbit_ids,
                    variant_id=variant_ids,
                    object_id=orbits.object_id,
                    weights=orbits.weights,
                    weights_cov=orbits.weights_cov,
                    coordinates=CartesianCoordinates.from_kwargs(
                        x=step_xyzvxvyvz[:, 0],
                        y=step_xyzvxvyvz[:, 1],
                        z=step_xyzvxvyvz[:, 2],
                        vx=step_xyzvxvyvz[:, 3],
                        vy=step_xyzvxvyvz[:, 4],
                        vz=step_xyzvxvyvz[:, 5],
                        time=Timestamp.from_jd(
                            pa.repeat(sim.t + ephem.jd_ref, sim.N), scale="tdb"
                        ),
                        origin=Origin.from_kwargs(
                            code=pa.repeat(
                                "SOLAR_SYSTEM_BARYCENTER",
                                sim.N,
                            )
                        ),
                        frame="equatorial",
                    ),
                )

            assert isinstance(time_step_results, OrbitType)

            for condition in conditions:

                collision_object_code = condition.collision_object.code[0].as_py()
                particle_location = ephem.get_particle(
                    collision_object_code,
                    sim.t,
                )
                particle_location = CartesianCoordinates.from_kwargs(
                    x=[particle_location.x],
                    y=[particle_location.y],
                    z=[particle_location.z],
                    vx=[particle_location.vx],
                    vy=[particle_location.vy],
                    vz=[particle_location.vz],
                    time=Timestamp.from_jd([sim.t + ephem.jd_ref], scale="tdb"),
                    origin=Origin.from_kwargs(
                        code=["SOLAR_SYSTEM_BARYCENTER"],
                    ),
                    frame="equatorial",
                )
                diff = time_step_results.coordinates.values - particle_location.values

                # Calculate the distance in KM
                # We use the IAU definition of the astronomical unit (149_597_870.7 km)
                normalized_distance = np.linalg.norm(diff[:, :3], axis=1) * KM_P_AU

                # Calculate which particles are within the collision distance
                within_radius = normalized_distance < condition.collision_distance

                # If any are within our collision distance, we record the impact
                # and do bookkeeping to remove the particle from the simulation
                if np.any(within_radius):
                    colliding_orbits = time_step_results.apply_mask(within_radius)

                    if isinstance(orbits, VariantOrbits):
                        new_impacts = CollisionEvent.from_kwargs(
                            orbit_id=colliding_orbits.orbit_id,
                            coordinates=colliding_orbits.coordinates,
                            variant_id=colliding_orbits.variant_id,
                            condition_id=pa.repeat(
                                condition.condition_id[0].as_py(), len(colliding_orbits)
                            ),
                            collision_coordinates=transform_coordinates(
                                colliding_orbits.coordinates,
                                representation_out=SphericalCoordinates,
                                origin_out=condition.collision_object.as_OriginCodes(),
                                frame_out="ecliptic",
                            ),
                            collision_object=condition.collision_object.take(
                                [0 for _ in range(len(colliding_orbits))]
                            ),
                            stopping_condition=pa.repeat(
                                condition.stopping_condition[0].as_py(),
                                len(colliding_orbits),
                            ),
                        )
                    elif isinstance(orbits, Orbits):
                        new_impacts = CollisionEvent.from_kwargs(
                            orbit_id=colliding_orbits.orbit_id,
                            coordinates=colliding_orbits.coordinates,
                            condition_id=pa.repeat(
                                condition.condition_id[0].as_py(), len(colliding_orbits)
                            ),
                            collision_coordinates=transform_coordinates(
                                colliding_orbits.coordinates,
                                representation_out=SphericalCoordinates,
                                origin_out=condition.collision_object.as_OriginCodes(),
                                frame_out="ecliptic",
                            ),
                            collision_object=condition.collision_object.take(
                                [0 for _ in range(len(colliding_orbits))]
                            ),
                            stopping_condition=pa.repeat(
                                condition.stopping_condition[0].as_py(),
                                len(colliding_orbits),
                            ),
                        )
                    collision_events = qv.concatenate([collision_events, new_impacts])

                    stopping_condition = condition.stopping_condition.to_numpy(
                        zero_copy_only=False
                    )[0]

                    if stopping_condition:
                        removed_hashes = orbit_id_hashes[within_radius]
                        for hash_id in removed_hashes:
                            sim.remove(hash=c_uint32(hash_id))
                            # For some reason, it fails if we let rebound convert the hash to c_uint32

                        if isinstance(orbits, VariantOrbits):
                            keep_mask = pc.invert(
                                pc.is_in(orbits.variant_id, colliding_orbits.variant_id)
                            )
                        else:
                            keep_mask = pc.invert(
                                pc.is_in(orbits.orbit_id, colliding_orbits.orbit_id)
                            )

                        orbits = orbits.apply_mask(keep_mask)
                        # Accumulate impactors: add to results and colliders lists
                        results_list.append(colliding_orbits)
                        colliders_list.append(colliding_orbits)
                    # Accumulate new impacts regardless of stopping condition
                    collisions_list.append(new_impacts)

        # Build collisions and colliders once
        if len(collisions_list) > 0:
            collision_events = qv.concatenate(collisions_list)
        if len(colliders_list) > 0:
            colliders = qv.concatenate(colliders_list)
        else:
            colliders = None

        # Add the final positions of the particles that are not already in the results
        if time_step_results is not None:
            if colliders is None:
                results_list.append(time_step_results)
            else:
                if isinstance(orbits, Orbits):
                    still_in_simulation = pc.invert(
                        pc.is_in(time_step_results.orbit_id, colliders.orbit_id)
                    )
                elif isinstance(orbits, VariantOrbits):
                    still_in_simulation = pc.invert(
                        pc.is_in(time_step_results.variant_id, colliders.variant_id)
                    )
                addl = time_step_results.apply_mask(still_in_simulation)
                results_list.append(addl)

        # Build results once
        if len(results_list) > 0:
            results = qv.concatenate(results_list)
        else:
            results = (
                Orbits.empty() if isinstance(orbits, Orbits) else VariantOrbits.empty()
            )

        return results, collision_events
