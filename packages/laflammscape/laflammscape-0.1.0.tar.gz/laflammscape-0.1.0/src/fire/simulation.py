"""Fire Simulation Interface implementation.

Provides classes and functions for simulating fire spread with multiple
algorithms, spatial partitioning, and laflammap integration.
"""

import enum
import os
import queue
import threading
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import numpy as np

from ..state.representation import StateRepresentation
from .behavior import FireBehaviorCalculator, FuelModel
from .mtt_numba import mtt_minimum_travel_time_improved


class FireSpreadAlgorithm(enum.Enum):
    """Supported fire spread algorithms."""

    MINIMUM_TRAVEL_TIME = "minimum_travel_time"


@dataclass
class FireSimulationInterface:
    """Interface for fire spread simulation algorithms.

    Features:
    - MTT algorithm
    - Performance optimization
    """

    algorithm: FireSpreadAlgorithm = FireSpreadAlgorithm.MINIMUM_TRAVEL_TIME
    spatial_resolution: float = 90.0  # meters
    max_iterations: int = 1000
    fuel_models: List[FuelModel] = field(default_factory=list)

    # Performance settings
    use_spatial_partitioning: bool = False

    # Cached arrays for performance
    _fuel_base_rates: Optional[np.ndarray] = field(default=None, init=False)
    _fuel_property_arrays: Optional[Tuple] = field(default=None, init=False)

    def set_algorithm(self, algorithm: FireSpreadAlgorithm) -> None:
        """Set the fire spread algorithm.

        Args:
            algorithm: Fire spread algorithm to use
        """
        self.algorithm = algorithm

    def _generate_fuel_property_arrays(
        self,
    ) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
        """Generate fuel property arrays for all fuel models from the registry.

        Returns:
            Tuple of (loading_1hr, loading_10hr, loading_100hr, sav_1hr, depth, moisture_extinction) arrays
        """
        # Determine the maximum fuel model ID to size arrays appropriately
        # We need to handle the actual fuel model IDs used, not just the count
        if not self.fuel_models:
            max_fuel_model = 100  # Default size for empty registry
        else:
            # Get the maximum fuel model ID from the fuel model objects
            max_fuel_id = 0
            for fuel_model in self.fuel_models:
                try:
                    fuel_id = int(fuel_model.id)
                    max_fuel_id = max(max_fuel_id, fuel_id)
                except (ValueError, AttributeError):
                    pass
            max_fuel_model = max(max_fuel_id + 1, 100)  # Ensure at least 100 elements

        # Initialize arrays with default values
        loading_1hr = np.zeros(max_fuel_model, dtype=np.float32)
        loading_10hr = np.zeros(max_fuel_model, dtype=np.float32)
        loading_100hr = np.zeros(max_fuel_model, dtype=np.float32)
        sav_1hr = np.full(max_fuel_model, 2000.0, dtype=np.float32)  # Default SAV
        depth = np.ones(max_fuel_model, dtype=np.float32)  # Default depth
        moisture_extinction = np.full(
            max_fuel_model, 15.0, dtype=np.float32
        )  # Default moisture extinction

        # Fill in the fuel model properties from the registry using fuel model IDs as indices
        for fuel_id, fuel_model in enumerate(self.fuel_models):
            loading_1hr[fuel_id] = fuel_model.loading.get("1hr", 0.0)
            loading_10hr[fuel_id] = fuel_model.loading.get("10hr", 0.0)
            loading_100hr[fuel_id] = fuel_model.loading.get("100hr", 0.0)
            sav_1hr[fuel_id] = fuel_model.sav.get("1hr", 2000.0)
            depth[fuel_id] = fuel_model.depth
            moisture_extinction[fuel_id] = fuel_model.moisture_extinction

        # Debug output
        print(f"Generated fuel property arrays for {max_fuel_model} fuel model slots:")
        for fuel_model in self.fuel_models:
            try:
                fuel_id = int(fuel_model.id)
                if 0 <= fuel_id < max_fuel_model:
                    print(
                        f"  Model {fuel_id}: loading_1hr={loading_1hr[fuel_id]:.3f}, depth={depth[fuel_id]:.3f}, sav={sav_1hr[fuel_id]:.0f}, mext={moisture_extinction[fuel_id]:.1f}"  # noqa: E501
                    )
            except (ValueError, AttributeError):
                continue

        return (
            loading_1hr,
            loading_10hr,
            loading_100hr,
            sav_1hr,
            depth,
            moisture_extinction,
        )

    def _calculate_rothermel_base_rates(self) -> np.ndarray:
        """Calculate base spread rates for all fuel models using Rothermel equations.

        Returns:
            Array of base spread rates in m/min for each fuel model
        """
        max_fuel_model = len(self.fuel_models) if self.fuel_models else 100
        base_rates = np.zeros(max_fuel_model, dtype=np.float32)

        print("Calculating Rothermel base spread rates:")

        for fuel_id, fuel_model in enumerate(self.fuel_models):
            # Get fuel properties
            loading_1hr = fuel_model.loading.get("1hr", 0.0)  # tons/acre
            loading_10hr = fuel_model.loading.get("10hr", 0.0)
            loading_100hr = fuel_model.loading.get("100hr", 0.0)
            loading_herb = fuel_model.loading.get("herb", 0.0)
            loading_woody = fuel_model.loading.get("woody", 0.0)

            sav_1hr = fuel_model.sav.get("1hr", 2000.0)  # ft²/ft³

            depth = fuel_model.depth  # feet

            # Calculate total loading
            total_dead_loading = loading_1hr + loading_10hr + loading_100hr
            total_live_loading = loading_herb + loading_woody
            total_loading = total_dead_loading + total_live_loading

            if total_loading <= 0:
                base_rates[fuel_id] = 0.05  # Minimal rate for zero-fuel models
                print(f"  Fuel {fuel_id}: No fuel loading, base_rate = 0.05 m/min")
                continue

            # Simplified Rothermel reaction intensity calculation
            # This is a simplified version focusing on the most important factors

            # 1. Calculate weighted SAV for dead fuels (primary contributor to spread)
            if total_dead_loading > 0:
                weighted_sav_dead = (loading_1hr * sav_1hr) / total_dead_loading
            else:
                weighted_sav_dead = sav_1hr

            # 2. Calculate relative dead fuel loading (1hr fuels are most reactive)
            # 1hr fuels contribute most to reaction intensity
            dead_fuel_reactivity = loading_1hr + (loading_10hr * 0.3) + (loading_100hr * 0.1)

            # 3. Live fuel contribution (herbs more reactive than woody)
            live_fuel_reactivity = loading_herb * 0.8 + loading_woody * 0.3

            # 4. Total fuel reactivity
            total_reactivity = dead_fuel_reactivity + live_fuel_reactivity

            # 5. SAV effect on reaction intensity (higher SAV = faster burning)
            # Normalize SAV effect: typical range 1000-4000 ft²/ft³
            sav_factor = min(weighted_sav_dead / 2000.0, 3.0)  # 1.0 at 2000, max 3.0

            # 6. Fuel bed depth effect (deeper beds can sustain faster spread)
            # Normalize depth: typical range 0.1-6.0 feet
            depth_factor = min(np.sqrt(depth), 2.5)  # Square root relationship, max 2.5

            # 7. Calculate base reaction intensity (simplified Rothermel)
            # This represents the energy release rate that drives fire spread
            reaction_intensity = total_reactivity * sav_factor * depth_factor

            # 8. Convert reaction intensity to spread rate
            # Empirical relationship: higher reaction intensity = faster spread
            # Scale to realistic fire spread rates (0.1-2.0 m/min for base rates)
            base_rate = reaction_intensity * 0.15  # Scaling factor from fire research

            # 9. Apply realistic bounds
            # Grass fuels: 0.3-1.5 m/min (18-90 m/hr)
            # Shrub fuels: 0.2-1.0 m/min (12-60 m/hr)
            # Timber fuels: 0.1-0.5 m/min (6-30 m/hr)
            if fuel_model.id.startswith("GR"):  # Grass models
                base_rate = max(0.3, min(base_rate, 1.5))
            elif fuel_model.id.startswith("GS"):  # Grass-shrub models
                base_rate = max(0.25, min(base_rate, 1.2))
            elif fuel_model.id.startswith("SH"):  # Shrub models
                base_rate = max(0.2, min(base_rate, 1.0))
            elif fuel_model.id.startswith("TU") or fuel_model.id.startswith("TL"):  # Timber models
                base_rate = max(0.1, min(base_rate, 0.5))
            else:  # Default bounds
                base_rate = max(0.1, min(base_rate, 1.0))

            base_rates[fuel_id] = base_rate

            print(
                f"  Fuel {fuel_model.id} ({fuel_id}): loading={total_loading:.2f}, "
                f"reactivity={total_reactivity:.2f}, SAV={weighted_sav_dead:.0f}, "
                f"depth={depth:.1f} -> base_rate = {base_rate:.3f} m/min ({base_rate*60:.0f} m/hr)"
            )

        # Set non-burnable fuel models to zero
        for i in [91, 92, 93, 98, 99]:
            if i < len(base_rates):
                base_rates[i] = 0.0

        return base_rates

    def simulate_spread(
        self,
        burn_times: np.ndarray,
        fuel_models: np.ndarray,
        moisture_1hr: np.ndarray,
        moisture_10hr: np.ndarray,
        moisture_100hr: np.ndarray,
        moisture_herb: np.ndarray,
        moisture_woody: np.ndarray,
        wind_speed: np.ndarray,
        wind_direction: np.ndarray,
        slope: np.ndarray,
        aspect: np.ndarray,
        spatial_resolution: float,
        burn_time_minutes: float = 1680.0,
    ) -> np.ndarray:
        """Simulate fire spread from ignition points using MTT.
        Args:
            burn_times: Initial burn times array (NumPy)
            fuel_models: Fuel model array (NumPy)
            ... (other arrays)
            spatial_resolution: Cell size in meters
            burn_time_minutes: Simulation time in minutes
        Returns:
            2D array of burn times in minutes (NumPy)
        """
        result_np = self._simulate_minimum_travel_time(
            burn_times,
            fuel_models,
            moisture_1hr,
            moisture_10hr,
            moisture_100hr,
            moisture_herb,
            moisture_woody,
            wind_speed,
            wind_direction,
            slope,
            aspect,
            spatial_resolution,
            burn_time_minutes,
        )
        return result_np

    def _simulate_minimum_travel_time(
        self,
        burn_times: np.ndarray,
        fuel_models: np.ndarray,
        moisture_1hr: np.ndarray,
        moisture_10hr: np.ndarray,
        moisture_100hr: np.ndarray,
        moisture_herb: np.ndarray,
        moisture_woody: np.ndarray,
        wind_speed: np.ndarray,
        wind_direction: np.ndarray,
        slope: np.ndarray,
        aspect: np.ndarray,
        spatial_resolution: float,
        burn_time_minutes: float,
    ) -> np.ndarray:
        """Simulate fire spread using Numba-accelerated minimum travel time algorithm (NumPy/Numba).
        Args:
            burn_times: Initial burn times array (NumPy)
            fuel_models: Fuel model array (NumPy)
            ... (other arrays)
            spatial_resolution: Cell size in meters
            burn_time_minutes: Simulation time in minutes
        Returns:
            2D array of burn times in minutes (NumPy)
        """
        # Generate fuel property arrays from the registry (cached for performance)
        if self._fuel_property_arrays is None:
            self._fuel_property_arrays = self._generate_fuel_property_arrays()
        (
            fuel_loading_1hr,
            fuel_loading_10hr,
            fuel_loading_100hr,
            fuel_sav_1hr,
            fuel_depth,
            fuel_moisture_extinction,
        ) = self._fuel_property_arrays

        # Calculate base rates using Rothermel equations (cached for performance)
        if self._fuel_base_rates is None:
            self._fuel_base_rates = self._calculate_rothermel_base_rates()
        self._fuel_base_rates

        result = mtt_minimum_travel_time_improved(
            burn_times,
            fuel_models,
            moisture_1hr,
            moisture_10hr,
            moisture_100hr,
            moisture_herb,
            moisture_woody,
            wind_speed,
            wind_direction,
            slope,
            aspect,
            spatial_resolution,
            burn_time_minutes,
            fuel_loading_1hr,
            fuel_loading_10hr,
            fuel_loading_100hr,
            fuel_sav_1hr,
            fuel_depth,
            fuel_moisture_extinction,
        )
        return result

    def calculate_fire_effects(self, state: StateRepresentation, burn_times: np.ndarray) -> None:
        """Calculate fire effects based on burn times using NumPy operations.
        Args:
            state: Landscape state to update with fire effects
            burn_times: 2D array of burn times in minutes
        """
        burned_mask = np.logical_and(burn_times < np.inf, burn_times > 0)
        burn_severity = np.where(burned_mask, np.ones_like(burn_times), np.zeros_like(burn_times))
        state.set_variable("burn_severity", burn_severity)


class FireSimulationModule:
    """Module that wraps FireSimulationInterface for orchestrator use."""

    def __init__(
        self,
        simulation_interface: FireSimulationInterface,
        fuel_models: Dict[int, FuelModel],
        weather_module=None,
        state_id_to_idx: Optional[Dict[str, int]] = None,
        idx_to_state_id: Optional[Dict[int, str]] = None,
        state_thresholds: Optional[Dict[str, Dict[str, float]]] = None,
    ):
        self.simulation_interface = simulation_interface
        self.behavior_calculator = FireBehaviorCalculator()
        self.fuel_models = fuel_models
        self.weather_module = weather_module
        self.state_id_to_idx = state_id_to_idx or {}
        self.idx_to_state_id = idx_to_state_id or {}
        self.state_thresholds = state_thresholds or {}

        self.simulation_orchestrator = FireSimulationOrchestrator(
            simulation_interface=simulation_interface,
            behavior_calculator=self.behavior_calculator,
            window_hours=8.0,  # 8-hour simulation windows
            state_id_to_idx=self.state_id_to_idx,
            idx_to_state_id=self.idx_to_state_id,
            state_thresholds=self.state_thresholds,
        )

    def apply_to_state(
        self,
        state,
        ignition_points=None,
        burn_time_minutes=73920.0,
        initial_weather_day=1,
        **kwargs,
    ):
        """
        Run the fire simulation and update the state with burn times and effects.
        Args:
            state: StateRepresentation
            ignition_points: List of (row, col) tuples for ignitions (optional)
            burn_time_minutes: Total simulation time in minutes
            initial_weather_day: Starting day of year for simulation (1-366)
        """
        # If ignition_points not provided, try to get from state variable 'ignitions'
        if ignition_points is None and state.has_variable("ignitions"):
            ignitions = state.get_variable("ignitions")
            ignition_points = list(zip(*np.where(ignitions)))
        if ignition_points is None:
            ignition_points = []
            print("no ignition points")
        total_hours = burn_time_minutes / 60.0
        self.simulation_orchestrator.simulate_with_windows(
            state=state,
            ignition_points=ignition_points,
            initial_weather_day=initial_weather_day,
            total_hours=total_hours,
            weather_module=self.weather_module,
        )


@dataclass
class FireSimulationOrchestrator:
    """Orchestrates time-windowed fire simulation with behavior calculation.

    Features:
    - Simulates fire spread in configurable time windows
    - Updates weather and fuel models between windows
    - Calculates fire behavior after each spread calculation
    - Integrates with state representation
    - Multithreaded data saving for performance
    """

    simulation_interface: FireSimulationInterface
    behavior_calculator: FireBehaviorCalculator
    window_hours: float = 8.0  # Default 8-hour simulation windows
    year: int = 0
    state_id_to_idx: Dict[str, int] = field(default_factory=dict)
    idx_to_state_id: Dict[int, str] = field(default_factory=dict)
    state_thresholds: Dict[str, Dict[str, float]] = field(default_factory=dict)

    # Multithreaded data saving
    _data_save_queue: Optional[queue.Queue] = field(default=None, init=False)
    _data_save_thread: Optional[threading.Thread] = field(default=None, init=False)
    _data_save_running: bool = field(default=False, init=False)

    def __post_init__(self):
        """Initialize multithreaded data saving after object creation."""
        # DISABLED: Background data saving to avoid hanging issues
        # self._data_save_queue = queue.Queue()
        # self._data_save_running = True
        # self._data_save_thread = threading.Thread(target=self._data_save_worker, daemon=True)
        # self._data_save_thread.start()
        # print("OPTIMIZATION: Started multithreaded data saving worker")
        print("OPTIMIZATION: Background data saving disabled - using synchronous saving")

    def _data_save_worker(self):
        """Background worker thread for saving data to disk with HDF5 compression."""
        save_count = 0
        while self._data_save_running:
            try:
                # Check running flag more frequently
                if not self._data_save_running:
                    break

                # Get data from queue with timeout to allow checking _data_save_running
                if self._data_save_queue is not None:
                    save_task = self._data_save_queue.get(timeout=0.5)  # Shorter timeout
                else:
                    break
                if save_task is None:  # Shutdown signal
                    break

                save_count += 1

                # Check running flag again before processing
                if not self._data_save_running:
                    break

                # Unpack save task (simplified format)
                fire_state, current_time, output_dir, save_data = save_task

                # Calculate actual day of year and hour for filename
                hours = current_time / 60.0
                # Use the actual simulation day that corresponds to this time
                if hasattr(self, "_initial_weather_day"):
                    # Calculate the actual simulation day (same logic as in simulate_with_windows)
                    actual_simulation_day = self._initial_weather_day + int(hours // 24)
                    day_of_year = actual_simulation_day
                else:
                    # Fallback to fire day if initial weather day not set
                    day_of_year = int(hours // 24)
                hour_of_day = int(hours % 24)

                # Try HDF5 first, fallback to NPZ if it fails
                data_filename = f"fire_data_year_{int(self.year):04d}_day_{day_of_year:03d}_hour_{hour_of_day:02d}.h5"
                data_path = Path(output_dir) / data_filename

                try:
                    import h5py

                    # Use parallel compression with optimal settings
                    compression_opts = {
                        "compression": "gzip",
                        "compression_opts": 6,  # Good balance of speed vs compression
                        "shuffle": True,  # Improves compression for integer data
                        "fletcher32": True,  # Data integrity checks
                    }

                    with h5py.File(data_path, "w", libver="latest") as f:
                        # Save each array with optimized compression
                        for key, value in save_data.items():
                            if isinstance(value, np.ndarray):
                                # Use optimal chunk size for 2D arrays
                                if value.ndim == 2:
                                    chunk_size = min(value.shape[0], 100), min(value.shape[1], 100)
                                else:
                                    chunk_size = None

                                f.create_dataset(
                                    key,
                                    data=value,
                                    chunks=chunk_size,
                                    **compression_opts,
                                )
                            else:
                                # Store scalar values as attributes
                                f.attrs[key] = value

                    file_size_kb = os.path.getsize(data_path) / 1024
                    if file_size_kb > 10:
                        print(
                            f"OPTIMIZATION: Background saved HDF5 fire data: {data_path} ({file_size_kb:.1f} KB)"
                        )

                except (ImportError, Exception) as e:
                    # Fallback to NPZ if HDF5 fails
                    print(f"OPTIMIZATION: HDF5 save failed ({e}), falling back to NPZ")

                    # Only copy fire_state if it's not already the right type
                    if save_data["fire_state"].dtype != np.uint8:
                        save_data["fire_state"] = save_data["fire_state"].astype(np.uint8)

                    npz_filename = f"fire_data_year_{int(self.year):04d}_day_{day_of_year:03d}_hour_{hour_of_day:02d}.npz"  # noqa: E501
                    npz_path = Path(output_dir) / npz_filename
                    np.savez_compressed(npz_path, **save_data)

                    file_size_kb = os.path.getsize(npz_path) / 1024
                    if file_size_kb > 10:
                        print(
                            f"OPTIMIZATION: Background saved NPZ fire data: {npz_path} ({file_size_kb:.1f} KB)"
                        )

            except queue.Empty:
                continue  # Timeout, check if we should continue
            except Exception as e:
                print(f"Error in data save worker: {e}")
                continue

        print(f"OPTIMIZATION: Data save worker processed {save_count} saves before shutdown")

    def shutdown_data_saving(self):
        """Shutdown the data saving worker thread."""
        if self._data_save_running:
            print("OPTIMIZATION: Shutting down data saving worker thread...")
            self._data_save_running = False

            # Immediately clear the queue to prevent any new work
            if self._data_save_queue is not None:
                try:
                    while not self._data_save_queue.empty():
                        self._data_save_queue.get_nowait()
                except queue.Empty:
                    pass
                print("OPTIMIZATION: Cleared data save queue")

            # Don't wait for the thread - just let it die naturally
            # The thread will exit on its own when it checks _data_save_running
            print("OPTIMIZATION: Data save worker will exit naturally (no waiting)")

            print("OPTIMIZATION: Shutdown multithreaded data saving worker")

    def _save_fire_state_visualization(
        self,
        fire_state: np.ndarray,
        current_time: float,
        output_dir: str,
        state: Optional[StateRepresentation] = None,
    ) -> None:
        """OPTIMIZED: Save fire state data using multithreaded background saving with performance improvements.

        Performance optimizations:
        - Selective data saving (only save what changed)
        - Reduced data copying
        - Better compression settings
        - Smarter data preparation
        - Skip saves when fire state hasn't changed significantly

        Args:
            fire_state: 2D array of fire state (0=unburned, 1=burning, 2=burned)
            current_time: Current simulation time in minutes
            output_dir: Directory to save the data
            state: State representation to access elevation data (optional)
        """
        # OPTIMIZATION: Skip saving if fire state hasn't changed significantly
        if hasattr(self, "_last_fire_state"):
            # Calculate how much the fire state has changed
            changes = np.sum(fire_state != self._last_fire_state)
            total_cells = fire_state.size
            change_percentage = (changes / total_cells) * 100

            # Skip save if less than 1% of cells changed (prevents excessive small saves)
            if change_percentage < 1.0 and changes < 100:  # Also skip if < 100 cells changed
                return

        # Update the last fire state for next comparison
        self._last_fire_state = fire_state.copy()

        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)

        hours = current_time / 60.0
        # Calculate actual day of year: initial_weather_day + days elapsed since fire start
        if hasattr(self, "_initial_weather_day"):
            day_of_year = self._initial_weather_day + int(hours // 24)
        else:
            # Fallback to fire day if initial weather day not set
            day_of_year = int(hours // 24)
        hour_of_day = int(hours % 24)

        # OPTIMIZATION: Only save essential data to reduce file size and I/O time
        save_data = {
            "fire_state": fire_state.astype(np.uint8),  # Compress to uint8
            "time_minutes": current_time,
            "time_hours": hours,
            "year": self.year,
            "grid_shape": fire_state.shape,
        }

        # OPTIMIZATION: Only add elevation once per simulation (it doesn't change)
        if (
            state is not None
            and state.has_variable("elevation")
            and not hasattr(self, "_elevation_saved")
        ):
            elevation = state.get_variable("elevation")
            save_data["elevation"] = elevation.astype(np.float32)
            self._elevation_saved = True
            print("OPTIMIZATION: Saved elevation data (will be reused for subsequent saves)")

        # OPTIMIZATION: Only save ecological state once per simulation (it doesn't change during fire)
        if state is not None and not hasattr(self, "_eco_state_saved"):
            eco_state_found = False
            for eco_var_name in [
                "eco_state",
                "ecological_state",
                "state",
                "vegetation_state",
                "forest_state",
            ]:
                if state.has_variable(eco_var_name):
                    eco_state = state.get_variable(eco_var_name)
                    save_data["eco_state"] = eco_state  # Save integer indices
                    eco_state_found = True
                    print(
                        f"OPTIMIZATION: Saved ecological state data from variable '{eco_var_name}' (will be reused)"
                    )

                    # OPTIMIZATION: Only convert to strings once and cache
                    if self.idx_to_state_id and not hasattr(self, "_eco_state_strings"):
                        try:
                            self._eco_state_strings = np.array(
                                [
                                    [self.idx_to_state_id.get(idx, "unknown") for idx in row]
                                    for row in eco_state
                                ]
                            )
                            save_data["eco_state_strings"] = self._eco_state_strings
                            print("OPTIMIZATION: Cached ecological state string IDs for reuse")
                        except Exception as e:
                            print(f"Could not convert ecological state indices to strings: {e}")

                    break

            if eco_state_found:
                self._eco_state_saved = True
            else:
                available_vars = (
                    list(state.state_variables.keys()) if hasattr(state, "state_variables") else []
                )
                print(
                    f"No ecological state variable found. Available variables: {available_vars[:10]}..."
                )

        # OPTIMIZATION: Only save fire behavior data if there are burning cells (most timesteps have none)
        burning_cells = np.sum(fire_state == 1)
        if burning_cells > 0 and state is not None:
            # Save fire intensity data if available
            if state.has_variable("fire_intensity"):
                fire_intensity = state.get_variable("fire_intensity")
                save_data["fire_intensity"] = fire_intensity.astype(np.float32)
            elif state.has_variable("fire_fireline_intensity"):
                fire_intensity = state.get_variable("fire_fireline_intensity")
                save_data["fire_intensity"] = fire_intensity.astype(np.float32)

            # Save flame length data if available
            if state.has_variable("fire_flame_length"):
                flame_length = state.get_variable("fire_flame_length")
                save_data["fire_flame_length"] = flame_length.astype(np.float32)
            elif state.has_variable("flame_length"):
                flame_length = state.get_variable("flame_length")
                save_data["fire_flame_length"] = flame_length.astype(np.float32)
        # Always save max_flame_length if present
        if state is not None and state.has_variable("max_flame_length"):
            save_data["max_flame_length"] = state.get_variable("max_flame_length").astype(
                np.float32
            )
        # Save burn times for severity calculation
        if state is not None and state.has_variable("burn_times"):
            burn_times = state.get_variable("burn_times")
            save_data["burn_times"] = burn_times.astype(np.float32)

        # OPTIMIZATION: Only save state mappings and thresholds once per simulation
        if self.idx_to_state_id and not hasattr(self, "_state_mappings_saved"):
            save_data["state_id_mapping"] = {
                "idx_to_state_id": self.idx_to_state_id,
                "state_id_to_idx": self.state_id_to_idx,
            }
            self._state_mappings_saved = True
            print("OPTIMIZATION: Saved state ID mappings (will be reused)")

        if self.state_thresholds and not hasattr(self, "_state_thresholds_saved"):
            save_data["state_thresholds"] = self.state_thresholds
            self._state_thresholds_saved = True
            print("OPTIMIZATION: Saved fire thresholds (will be reused)")

        # OPTIMIZATION: Only save weather data if it's significantly different from last save
        if (
            state is not None
            and not hasattr(self, "_last_weather_save")
            or (current_time - getattr(self, "_last_weather_save", 0)) > 60
        ):  # Save every hour
            weather_data = {}
            for var_name in [
                "weather_temperature",
                "weather_humidity",
                "weather_wind_speed",
                "fuel_moisture_1hr",
                "fuel_moisture_10hr",
            ]:
                if state.has_variable(var_name):
                    var_data = state.get_variable(var_name)
                    if isinstance(var_data, np.ndarray):
                        # Store mean values to save space
                        weather_data[f"{var_name}_mean"] = float(np.mean(var_data))
                    else:
                        weather_data[f"{var_name}_value"] = float(var_data)

            if weather_data:
                save_data.update(weather_data)
                self._last_weather_save = current_time

        # OPTIMIZATION: Queue data for background saving with minimal copying
        if self._data_save_queue is not None:
            # OPTIMIZATION: Don't copy large arrays unnecessarily
            # Only copy what's actually needed for the background thread
            save_task = (fire_state, current_time, output_dir, save_data)
            try:
                self._data_save_queue.put_nowait(save_task)
                print(
                    f"OPTIMIZATION: Queued fire data for background saving (day {day_of_year}, hour {hour_of_day})"
                )
            except queue.Full:
                print(f"WARNING: Data save queue full, skipping save for time {current_time}")
        else:
            print("WARNING: Data save queue not available, using synchronous saving")

            # OPTIMIZATION: Use HDF5 format for synchronous saving too
            try:
                import h5py

                # Calculate day of year and hour for filename
                hours = current_time / 60.0
                # Calculate actual day of year: initial_weather_day + days elapsed since fire start
                if hasattr(self, "_initial_weather_day"):
                    day_of_year = self._initial_weather_day + int(hours // 24)
                else:
                    # Fallback to fire day if initial weather day not set
                    day_of_year = int(hours // 24)
                hour_of_day = int(hours % 24)

                data_filename = f"fire_data_year_{int(self.year):04d}_day_{day_of_year:03d}_hour_{hour_of_day:02d}.h5"
                data_path = Path(output_dir) / data_filename

                # Use parallel compression with optimal settings
                compression_opts = {
                    "compression": "gzip",
                    "compression_opts": 6,  # Good balance of speed vs compression
                    "shuffle": True,  # Improves compression for integer data
                    "fletcher32": True,  # Data integrity checks
                }

                with h5py.File(data_path, "w", libver="latest") as f:
                    # Save each array with optimized compression
                    for key, value in save_data.items():
                        if isinstance(value, np.ndarray):
                            # Use optimal chunk size for 2D arrays
                            if value.ndim == 2:
                                chunk_size = min(value.shape[0], 100), min(value.shape[1], 100)
                            else:
                                chunk_size = None

                            f.create_dataset(
                                key,
                                data=value,
                                chunks=chunk_size,
                                **compression_opts,
                            )
                        else:
                            # Store scalar values as attributes
                            f.attrs[key] = value

                file_size_kb = os.path.getsize(data_path) / 1024
                if file_size_kb > 10:
                    print(
                        f"OPTIMIZATION: Synchronously saved HDF5 fire data: {data_path} ({file_size_kb:.1f} KB)"
                    )

            except (ImportError, Exception) as e:
                # Fallback to NPZ if HDF5 fails
                print(f"OPTIMIZATION: HDF5 save failed ({e}), falling back to NPZ")

                # Calculate day of year and hour for filename
                hours = current_time / 60.0
                # Calculate actual day of year: initial_weather_day + days elapsed since fire start
                if hasattr(self, "_initial_weather_day"):
                    day_of_year = self._initial_weather_day + int(hours // 24)
                else:
                    # Fallback to fire day if initial weather day not set
                    day_of_year = int(hours // 24)
                hour_of_day = int(hours % 24)

                # Only copy fire_state if it's not already the right type
                if save_data["fire_state"].dtype != np.uint8:
                    save_data["fire_state"] = save_data["fire_state"].astype(np.uint8)

                npz_filename = f"fire_data_year_{int(self.year):04d}_day_{day_of_year:03d}_hour_{hour_of_day:02d}.npz"
                npz_path = Path(output_dir) / npz_filename
                np.savez_compressed(npz_path, **save_data)

                file_size_kb = os.path.getsize(npz_path) / 1024
                if file_size_kb > 10:
                    print(
                        f"OPTIMIZATION: Synchronously saved NPZ fire data: {npz_path} ({file_size_kb:.1f} KB)"
                    )

    def _save_quick_2d_plot(
        self, fire_state: np.ndarray, current_time: float, output_dir: str
    ) -> None:
        """Save a quick 2D fire state plot for real-time monitoring.

        Args:
            fire_state: 2D array of fire state
            current_time: Current simulation time in minutes
            output_dir: Directory to save the plot
        """
        from pathlib import Path

        import matplotlib.pyplot as plt

        hours = current_time / 60.0

        # Calculate day of year and hour for better filename organization
        if hasattr(self, "_initial_weather_day"):
            day_of_year = self._initial_weather_day + int(hours // 24)
        else:
            # Fallback to fire day if initial weather day not set
            day_of_year = int(hours // 24)
        hour_of_day = int(hours % 24)

        # Quick 2D plot with minimal processing
        plt.figure(figsize=(8, 6))

        # Create custom colormap for fire states
        colors = [
            (0.8, 0.8, 0.8),  # Unburned - light gray
            (1.0, 0.5, 0.0),  # Burning - orange
            (0.5, 0.0, 0.0),
        ]  # Burned - dark red
        cmap = plt.cm.colors.ListedColormap(colors)

        # Plot fire state
        plt.imshow(fire_state, cmap=cmap, vmin=0, vmax=2, interpolation="nearest")
        plt.colorbar(ticks=[0, 1, 2], label="Fire State")
        plt.title(f"Fire State at {hours:.1f} hours (Year {self.year})")
        plt.xticks([])
        plt.yticks([])

        # Save 2D figure with year-day-hour format
        output_path_2d = (
            Path(output_dir)
            / f"fire_state_2d_year_{int(self.year):04d}_day_{day_of_year:03d}_hour_{hour_of_day:02d}.png"
        )
        plt.savefig(output_path_2d, dpi=150, bbox_inches="tight")
        plt.close()

    @staticmethod
    def generate_visualizations_from_data(
        data_dir: str,
        output_dir: str = None,
        generate_3d: bool = True,
        longest_fire_only: bool = False,
        use_severity: bool = True,
        specific_year: int = None,
    ) -> None:
        """Generate all visualizations from saved fire data files.

        Supports both HDF5 (.h5) and NPZ (.npz) formats for backward compatibility.

        Run this after simulation to create high-quality plots offline.

        Args:
            data_dir: Directory containing .h5 or .npz fire data files
            output_dir: Directory to save visualizations (defaults to data_dir/visualizations)
            generate_3d: Whether to generate 3D plots (can be slow)
            longest_fire_only: Only process the year with the longest fire duration
            use_severity: Use calculated fire severity instead of fire state for visualization
            specific_year: If provided, only process data from this specific year (overrides longest_fire_only)
        """
        import glob
        import os
        from pathlib import Path

        import matplotlib.pyplot as plt

        # from mpl_toolkits.mplot3d import Axes3D
        import numpy as np

        if output_dir is None:
            output_dir = Path(data_dir) / "visualizations"

        os.makedirs(output_dir, exist_ok=True)

        # Find all data files (both HDF5 and NPZ formats)
        h5_files = glob.glob(os.path.join(data_dir, "fire_data_*.h5"))
        npz_files = glob.glob(os.path.join(data_dir, "fire_data_*.npz"))
        data_files = h5_files + npz_files
        data_files.sort()

        print(
            f"Found {len(data_files)} fire data files ({len(h5_files)} HDF5, {len(npz_files)} NPZ)"
        )

        # Filter data files based on year selection
        if specific_year is not None:
            # Filter to specific year (overrides longest_fire_only)
            original_count = len(data_files)
            data_files = [f for f in data_files if f"_year_{specific_year:04d}_" in f]
            print(
                f"Filtered to {len(data_files)} files from year {specific_year} (was {original_count})"
            )
        elif longest_fire_only:
            # Find the year with the longest fire duration
            data_files = FireSimulationOrchestrator._filter_longest_fire_year(data_files)
            print(f"Filtered to {len(data_files)} files from the year with longest fire duration")

        # Pre-compute 3D elevation data if generating 3D plots
        elevation_3d_data = None
        if generate_3d:
            # Load first file to get elevation data
            try:
                first_data = FireSimulationOrchestrator._load_data_file(data_files[0])
                if "elevation" in first_data:
                    print("Pre-computing 3D elevation surface (reused for all timesteps)...")
                    elevation_3d_data = FireSimulationOrchestrator._precompute_3d_elevation(
                        first_data
                    )
                    print(f"✓ 3D surface pre-computed for {elevation_3d_data['grid_shape']} grid")
                else:
                    print("No elevation data found - skipping 3D plots")
                    generate_3d = False
            except Exception as e:
                print(f"Error pre-computing 3D data: {e}")
                generate_3d = False

        for i, data_file in enumerate(data_files):
            try:
                # Load data using the unified loader
                data = FireSimulationOrchestrator._load_data_file(data_file)
                fire_state = data["fire_state"]
                time_hours = float(data["time_hours"])
                year = int(data["year"])

                print(f"Processing {i+1}/{len(data_files)}: {Path(data_file).name}")

                # Calculate fire severity if requested
                if use_severity:
                    fire_display_data, display_label, colormap_info = (
                        FireSimulationOrchestrator._calculate_fire_severity(
                            fire_state, data, time_hours
                        )
                    )
                else:
                    fire_display_data = fire_state
                    display_label = "Fire State"
                    colormap_info = {
                        "colors": [
                            (0.8, 0.8, 0.8),
                            (1.0, 0.5, 0.0),
                            (0.5, 0.0, 0.0),
                        ],
                        "ticks": [0, 1, 2],
                        "vmin": 0,
                        "vmax": 2,
                    }

                # Generate 2D plot
                plt.figure(figsize=(10, 8))
                cmap = plt.cm.colors.ListedColormap(colormap_info["colors"])

                plt.imshow(
                    fire_display_data,
                    cmap=cmap,
                    vmin=colormap_info["vmin"],
                    vmax=colormap_info["vmax"],
                )
                plt.colorbar(ticks=colormap_info["ticks"], label=display_label)
                plt.title(f"{display_label} at {time_hours:.1f} hours (Year {year})")

                # Add statistics
                if use_severity:
                    # Severity statistics
                    unburned = np.sum(fire_display_data == 0)
                    low_severity = np.sum(fire_display_data == 1)
                    moderate_severity = np.sum(fire_display_data == 2)
                    high_severity = np.sum(fire_display_data == 3)
                    total_burned = low_severity + moderate_severity + high_severity
                    plt.text(
                        0.02,
                        0.98,
                        f"Unburned: {unburned}\nLow: {low_severity}\nModerate: {moderate_severity}\nHigh: {high_severity}\nTotal burned: {total_burned}",  # noqa: E501
                        transform=plt.gca().transAxes,
                        verticalalignment="top",
                        bbox=dict(boxstyle="round", facecolor="white", alpha=0.8),
                    )
                else:
                    # Fire state statistics
                    burning_cells = np.sum(fire_state == 1)
                    burned_cells = np.sum(fire_state == 2)
                    total_affected = burning_cells + burned_cells
                    plt.text(
                        0.02,
                        0.98,
                        f"Burning: {burning_cells}\nBurned: {burned_cells}\nTotal: {total_affected}",
                        transform=plt.gca().transAxes,
                        verticalalignment="top",
                        bbox=dict(boxstyle="round", facecolor="white", alpha=0.8),
                    )

                plt.xticks([])
                plt.yticks([])

                # Extract day of year from filename (e.g., fire_data_year_0000_day_162_hour_08.h5)
                filename = Path(data_file).name
                if "_day_" in filename:
                    # Extract day from filename: fire_data_year_0000_day_162_hour_08.h5
                    day_part = filename.split("_day_")[1].split("_")[0]
                    day_of_year = int(day_part)
                else:
                    # Fallback: calculate from time_hours if initial_weather_day is available
                    if "initial_weather_day" in data:
                        day_of_year = int(data["initial_weather_day"]) + int(time_hours // 24)
                    else:
                        day_of_year = int(time_hours // 24)

                hour_of_day = int(time_hours % 24)
                prefix = "severity" if use_severity else "fire"
                output_path_2d = (
                    Path(output_dir)
                    / f"{prefix}_2d_year_{year:04d}_day_{day_of_year:03d}_hour_{hour_of_day:02d}.png"
                )
                plt.savefig(output_path_2d, dpi=300, bbox_inches="tight")
                plt.close()

                # Generate 3D plot using pre-computed elevation data
                if generate_3d and elevation_3d_data is not None:
                    FireSimulationOrchestrator._generate_3d_plot_fast(
                        fire_display_data,
                        time_hours,
                        year,
                        elevation_3d_data,
                        output_dir,
                        use_severity,
                        display_label,
                        colormap_info,
                        data,
                    )

            except Exception as e:
                print(f"Error processing {data_file}: {e}")
                continue

        print(f"Generated visualizations in {output_dir}")
        prefix = "severity" if use_severity else "fire"
        print(
            f"To create animations, use: ffmpeg -framerate 2 -pattern_type glob -i '{prefix}_2d_*.png' -c:v libx264 {prefix}_animation.mp4"  # noqa: E501
        )

    @staticmethod
    def _load_data_file(file_path: str) -> dict:
        """Load data from either HDF5 or NPZ file format.

        Args:
            file_path: Path to the data file

        Returns:
            Dictionary containing the loaded data
        """
        if file_path.endswith(".h5"):
            # Load HDF5 file
            try:
                import h5py

                data = {}
                with h5py.File(file_path, "r") as f:
                    # Load datasets
                    for key in f.keys():
                        data[key] = f[key][:]

                    # Load attributes
                    for key, value in f.attrs.items():
                        data[key] = value

                return data
            except ImportError:
                raise ImportError("h5py is required to read HDF5 files")
        else:
            # Load NPZ file
            return np.load(file_path, allow_pickle=True)

    @staticmethod
    def _filter_longest_fire_year(data_files: list) -> list:
        """Filter data files to only include the year with the longest fire duration.

        Args:
            data_files: List of data file paths

        Returns:
            Filtered list containing only files from the year with longest fire
        """
        from collections import defaultdict

        import numpy as np

        # Group files by year and calculate fire duration for each year
        year_files = defaultdict(list)
        year_durations = {}

        for data_file in data_files:
            try:
                data = np.load(data_file, allow_pickle=True)
                year = int(data["year"])
                time_hours = float(data["time_hours"])

                year_files[year].append((data_file, time_hours))

                # Track maximum time for each year
                if year not in year_durations:
                    year_durations[year] = 0
                year_durations[year] = max(year_durations[year], time_hours)

            except Exception as e:
                print(f"Warning: Could not process {data_file}: {e}")
                continue

        # Find year with longest fire duration
        if not year_durations:
            return data_files

        longest_year = max(year_durations.keys(), key=lambda y: year_durations[y])
        longest_duration = year_durations[longest_year]

        print(f"Year {longest_year} has the longest fire duration: {longest_duration:.1f} hours")
        print(f"Fire durations by year: {dict(year_durations)}")

        # Return only files from the longest fire year, sorted by time
        longest_year_files = sorted(year_files[longest_year], key=lambda x: x[1])
        return [f[0] for f in longest_year_files]

    @staticmethod
    def _calculate_fire_severity(
        fire_state: np.ndarray, data: dict, current_time_hours: float
    ) -> tuple:
        """Calculate fire severity based on ecological state and fire intensity thresholds.

        Uses the state transition model thresholds to determine severity based on:
        1. Current ecological state of each pixel
        2. Fire intensity calculated during simulation
        3. State-specific thresholds from the transition model

        Args:
            fire_state: Fire state array (0=unburned, 1=burning, 2=burned)
            data: Data dictionary containing additional fire information
            current_time_hours: Current time in hours

        Returns:
            Tuple of (severity_array, label, colormap_info)
        """
        import numpy as np

        # Initialize severity array (0=unburned, 1=low, 2=moderate, 3=high)
        severity = np.zeros_like(fire_state, dtype=np.uint8)

        # For burned areas, calculate severity based on available data
        burned_mask = fire_state == 2
        burning_mask = fire_state == 1

        if np.any(burned_mask) or np.any(burning_mask):
            # Method 1: Use ecological state and flame length with state-specific thresholds (preferred)
            # Safe access to data arrays - handle both dict-like and numpy array access
            eco_state_data = (
                data["eco_state"]
                if "eco_state" in data
                else (data["ecological_state"] if "ecological_state" in data else None)
            )
            eco_state_strings = data["eco_state_strings"] if "eco_state_strings" in data else None
            # Use max_flame_length if present, otherwise fire_flame_length, otherwise flame_length
            if "max_flame_length" in data:
                flame_length_data = data["max_flame_length"]
            elif "fire_flame_length" in data:
                flame_length_data = data["fire_flame_length"]
            elif "flame_length" in data:
                flame_length_data = data["flame_length"]
            else:
                flame_length_data = None

            # Handle state_thresholds - convert from numpy array if necessary
            state_thresholds_raw = data["state_thresholds"] if "state_thresholds" in data else {}
            if isinstance(state_thresholds_raw, np.ndarray):
                # Convert numpy array back to dictionary
                try:
                    state_thresholds = state_thresholds_raw.item()
                    print(
                        f"Debug: Converted state_thresholds from numpy array to dict with {len(state_thresholds)} entries"  # noqa: E501
                    )
                except (ValueError, AttributeError):
                    print(
                        "Debug: Could not convert state_thresholds from numpy array, using empty dict"
                    )
                    state_thresholds = {}
            else:
                state_thresholds = state_thresholds_raw

            # Handle state_id_mapping - convert from numpy array if necessary
            state_id_mapping_raw = data["state_id_mapping"] if "state_id_mapping" in data else {}
            if isinstance(state_id_mapping_raw, np.ndarray):
                # Convert numpy array back to dictionary
                try:
                    state_id_mapping = state_id_mapping_raw.item()
                    print("Debug: Converted state_id_mapping from numpy array to dict")
                except (ValueError, AttributeError):
                    print(
                        "Debug: Could not convert state_id_mapping from numpy array, using empty dict"
                    )
                    state_id_mapping = {}
            else:
                state_id_mapping = state_id_mapping_raw

            if eco_state_data is not None and flame_length_data is not None:
                # Use state-specific thresholds for severity classification (preferred method)
                affected_mask = burned_mask | burning_mask

                # Get ecological state IDs for affected pixels
                if eco_state_strings is not None:
                    # Use string state IDs directly
                    eco_states_affected = eco_state_strings[affected_mask]
                elif state_id_mapping and "idx_to_state_id" in state_id_mapping:
                    # Convert integer indices to state IDs
                    idx_to_state_id = state_id_mapping["idx_to_state_id"]
                    eco_indices_affected = eco_state_data[affected_mask]
                    eco_states_affected = np.array(
                        [
                            (
                                idx_to_state_id[str(idx)]
                                if str(idx) in idx_to_state_id
                                else "unknown"
                            )
                            for idx in eco_indices_affected
                        ]
                    )
                else:
                    # Fallback: use generic thresholds
                    eco_states_affected = None

                flame_length_values = flame_length_data[affected_mask]
                severity_values = np.ones(
                    len(flame_length_values), dtype=np.uint8
                )  # Default to low

                if eco_states_affected is not None and state_thresholds:
                    # Use state-specific thresholds for severity classification
                    print("Using state-specific fire severity thresholds:")
                    print(f"  Available state thresholds: {list(state_thresholds.keys())}")
                    print(f"  Unique affected states: {np.unique(eco_states_affected)}")
                    print(f"  Total affected pixels: {len(eco_states_affected)}")

                    # Track thresholds used for debugging
                    threshold_debug = {}
                    fallback_count = 0
                    state_specific_count = 0

                    for i, (state_id, flame_length) in enumerate(
                        zip(eco_states_affected, flame_length_values)
                    ):
                        # Decode bytes if necessary
                        if isinstance(state_id, (bytes, np.bytes_)):
                            state_id = state_id.decode("utf-8")

                        # Get thresholds for this state
                        thresholds = state_thresholds.get(state_id, {})

                        # Check if we're using fallback values and why
                        using_fallback = False
                        fallback_reasons = []

                        if state_id not in state_thresholds:
                            using_fallback = True
                            fallback_reasons.append(f"state '{state_id}' not in state_thresholds")

                        very_low_max = thresholds.get("very_low_max")
                        low_max = thresholds.get("low_max")
                        medium_max = thresholds.get("medium_max")

                        if very_low_max is None:
                            very_low_max = 0.25
                            using_fallback = True
                            fallback_reasons.append("very_low_max is None")
                        if low_max is None:
                            low_max = 1.2
                            using_fallback = True
                            fallback_reasons.append("low_max is None")
                        if medium_max is None:
                            medium_max = 2.4
                            using_fallback = True
                            fallback_reasons.append("medium_max is None")

                        if using_fallback:
                            fallback_count += 1
                            if fallback_count <= 5:  # Only print first 5 examples to avoid spam
                                print(
                                    f"Debug: Using fallback for state '{state_id}': {', '.join(fallback_reasons)}"
                                )
                        else:
                            state_specific_count += 1

                        # Store thresholds for debugging
                        if state_id not in threshold_debug:
                            threshold_debug[state_id] = {
                                "very_low_max": very_low_max,
                                "low_max": low_max,
                                "medium_max": medium_max,
                                "count": 0,
                                "max_flame_length": 0.0,
                                "using_fallback": using_fallback,
                            }
                        threshold_debug[state_id]["count"] += 1
                        threshold_debug[state_id]["max_flame_length"] = max(
                            threshold_debug[state_id]["max_flame_length"],
                            flame_length,
                        )

                        # Classify severity based on state-specific thresholds
                        if flame_length <= very_low_max:
                            severity_values[i] = 1  # Low severity (very low threshold)
                        elif flame_length <= low_max:
                            severity_values[i] = 1  # Low severity
                        elif flame_length <= medium_max:
                            severity_values[i] = 2  # Moderate severity
                        else:
                            severity_values[i] = 3  # High severity

                    # Apply to severity grid
                    severity[affected_mask] = severity_values

                    # Summarize severity by eco state
                    eco_severity_counts = defaultdict(
                        lambda: [0, 0, 0, 0]
                    )  # [unburned, low, moderate, high]
                    for state_id, sev in zip(eco_states_affected, severity_values):
                        if isinstance(state_id, (bytes, np.bytes_)):
                            state_id = state_id.decode("utf-8")
                        eco_severity_counts[state_id][sev] += 1
                    print("\nEco-state-specific fire severity counts:")
                    print(f"{'Eco State':<15} {'Low':>8} {'Mod':>8} {'High':>8}  Total")
                    print("-" * 45)
                    for state_id, counts in eco_severity_counts.items():
                        total = counts[1] + counts[2] + counts[3]
                        print(
                            f"{state_id:<15} {counts[1]:>8} {counts[2]:>8} {counts[3]:>8}  {total:>8}"
                        )
                    print()

                    print("State-specific flame length severity classification:")
                    print(
                        f"  Flame length range: {np.min(flame_length_values):.3f}-{np.max(flame_length_values):.3f}m"
                    )
                    print(
                        f"  Used thresholds from {len(set(eco_states_affected))} unique ecological states"
                    )
                    print(f"  State-specific thresholds used for {state_specific_count} pixels")
                    print(f"  Fallback thresholds used for {fallback_count} pixels")

                    # Debug output showing thresholds for each state
                    print("  State-specific thresholds used:")
                    for state_id, info in threshold_debug.items():
                        fallback_indicator = (
                            " (FALLBACK)" if info["using_fallback"] else " (STATE-SPECIFIC)"
                        )
                        print(
                            f"    {state_id}: very_low≤{info['very_low_max']:.2f}, low≤{info['low_max']:.2f}, medium≤{info['medium_max']:.2f} "  # noqa: E501
                            f"(cells: {info['count']}, max_flame: {info['max_flame_length']:.3f}m){fallback_indicator}"
                        )

                    # Show specific examples of high flame lengths that aren't classified as high severity
                    max_flame_indices = np.where(flame_length_values > 2.0)[0]  # Examples > 2.0m
                    if len(max_flame_indices) > 0:
                        print("  Examples of high flame lengths (>2.0m) and their classification:")
                        for idx in max_flame_indices[:5]:  # Show first 5 examples
                            np.where(affected_mask)[0][idx]
                            state_id = eco_states_affected[idx]
                            if isinstance(state_id, (bytes, np.bytes_)):
                                state_id = state_id.decode("utf-8")
                            flame_val = flame_length_values[idx]
                            severity_val = severity_values[idx]
                            severity_names = {
                                1: "Low",
                                2: "Moderate",
                                3: "High",
                            }
                            thresholds = state_thresholds.get(state_id, {})
                            medium_max = thresholds.get("medium_max", 2.4)
                            print(
                                f"    Flame {flame_val:.3f}m in state {state_id} -> {severity_names[severity_val]} severity "  # noqa: E501
                                f"(medium_max={medium_max:.2f}m)"
                            )
                else:
                    # Only print fallback log if no eco-state-specific thresholds were used
                    print("Generic flame length severity classification (fallback):")
                    print(
                        f"  Flame length range: {np.min(flame_length_values):.3f}-{np.max(flame_length_values):.3f}m"
                    )
                    print(f"  Low severity (<1.2m): {np.sum(severity_values == 1)} cells")
                    print(f"  Moderate severity (1.2-2.4m): {np.sum(severity_values == 2)} cells")
                    print(f"  High severity (>2.4m): {np.sum(severity_values == 3)} cells")

            # Method 2: Use flame length if available (without ecological state)
            elif flame_length_data is not None:
                # Use flame length for severity classification (same thresholds as Method 1)
                affected_mask = burned_mask | burning_mask

                # Vectorized flame length severity classification
                flame_length_values = flame_length_data[affected_mask]
                severity_values = np.ones(
                    len(flame_length_values), dtype=np.uint8
                )  # Default to low

                # Apply flame length thresholds
                severity_values[flame_length_values >= 1.2] = 2  # Moderate severity
                severity_values[flame_length_values >= 2.4] = 3  # High severity

                # Apply to severity grid
                severity[affected_mask] = severity_values

                print("Flame length severity classification (no eco state):")
                print(
                    f"  Flame length range: {np.min(flame_length_values):.3f}-{np.max(flame_length_values):.3f}m"
                )
                print(f"  Low severity (<1.2m): {np.sum(severity_values == 1)} cells")
                print(f"  Moderate severity (1.2-2.4m): {np.sum(severity_values == 2)} cells")
                print(f"  High severity (>2.4m): {np.sum(severity_values == 3)} cells")

            # Method 3: Use fire intensity if flame length not available (fallback)
            elif "fire_intensity" in data:
                fire_intensity = data["fire_intensity"]
                affected_mask = burned_mask | burning_mask

                # Use updated thresholds appropriate for fire intensity (kW/m)
                # Based on fire science literature: Low <500, Moderate 500-2000, High >2000 kW/m
                intensity_thresholds = {"low_max": 500.0, "medium_max": 2000.0}

                intensity_values = fire_intensity[affected_mask]
                severity_values = np.ones(len(intensity_values), dtype=np.uint8)  # Default to low

                # Apply intensity thresholds
                severity_values[intensity_values >= intensity_thresholds["low_max"]] = (
                    2  # Moderate severity
                )
                severity_values[intensity_values >= intensity_thresholds["medium_max"]] = (
                    3  # High severity
                )

                # Apply to severity grid
                severity[affected_mask] = severity_values

                print("Fire intensity severity classification (fallback):")
                print(
                    f"  Intensity range: {np.min(intensity_values):.1f}-{np.max(intensity_values):.1f} kW/m"
                )
                print(f"  Low severity (<500 kW/m): {np.sum(severity_values == 1)} cells")
                print(f"  Moderate severity (500-2000 kW/m): {np.sum(severity_values == 2)} cells")
                print(f"  High severity (>2000 kW/m): {np.sum(severity_values == 3)} cells")

            # Method 4: Use burn times if available (fallback)
            elif "burn_times" in data:
                burn_times = data["burn_times"]

                # Calculate burn duration (how long ago the fire passed)
                burn_duration = current_time_hours * 60 - burn_times  # Convert to minutes
                burn_duration = np.maximum(burn_duration, 0)  # Ensure non-negative

                # Classify severity based on burn duration
                # Longer exposure = higher severity
                severity[burned_mask] = 1  # Default to low severity

                # Moderate severity: burned for more than 2 hours
                moderate_mask = burned_mask & (burn_duration > 120)
                severity[moderate_mask] = 2

                # High severity: burned for more than 6 hours
                high_mask = burned_mask & (burn_duration > 360)
                severity[high_mask] = 3

            else:
                # Method 5: Simple classification based on fire state (last resort)
                severity[burned_mask] = 2  # Default moderate severity for burned areas

                # Use spatial clustering to identify high-severity core areas
                # Areas surrounded by other burned areas likely had higher intensity
                from scipy import ndimage

                # Dilate burned areas to find cores
                structure = np.ones((3, 3))
                dilated = ndimage.binary_dilation(burned_mask, structure=structure)
                eroded = ndimage.binary_erosion(dilated, structure=structure, iterations=2)

                # Core areas get high severity
                severity[eroded] = 3

                # Edge areas get low severity
                edge_mask = burned_mask & ~ndimage.binary_erosion(burned_mask, structure=structure)
                severity[edge_mask] = 1

        # Currently burning areas get moderate severity (unless already classified above)
        burning_unclassified = burning_mask & (severity == 0)
        severity[burning_unclassified] = 2

        # Define colormap for severity
        colormap_info = {
            "colors": [
                (0.8, 0.8, 0.8),  # Unburned - light gray
                (1.0, 1.0, 0.6),  # Low severity - light yellow
                (1.0, 0.5, 0.0),  # Moderate severity - orange
                (0.8, 0.0, 0.0),  # High severity - dark red
            ],
            "ticks": [0, 1, 2, 3],
            "vmin": 0,
            "vmax": 3,
        }

        return severity, "Fire Severity (State-Specific)", colormap_info

    @staticmethod
    def _precompute_3d_elevation(data: dict) -> dict:
        """Pre-compute 3D elevation surface data that can be reused across timesteps.

        Args:
            data: First data file containing elevation

        Returns:
            Dictionary with pre-computed 3D data
        """
        import numpy as np

        elevation = data["elevation"]
        fire_state = data["fire_state"]  # Just for grid shape
        rows, cols = fire_state.shape

        # Use full resolution for offline processing (no downsampling)
        elevation_3d = elevation
        x_3d = np.arange(cols)
        y_3d = np.arange(rows)

        X_3d, Y_3d = np.meshgrid(x_3d, y_3d)

        # Create terrain colors that incorporate ecological state information
        elev_min, elev_max = elevation_3d.min(), elevation_3d.max()
        elev_norm = (
            (elevation_3d - elev_min) / (elev_max - elev_min)
            if elev_max > elev_min
            else np.zeros_like(elevation_3d)
        )

        # Check if ecological state data is available
        if "eco_state" in data or "eco_state_strings" in data:
            # Use ecological state-based colors
            terrain_colors, eco_legend_info = (
                FireSimulationOrchestrator._create_ecological_terrain_colors(
                    data, elevation_3d, elev_norm
                )
            )
            print("Using ecological state-based terrain colors for 3D visualization")
        else:
            # Fallback to elevation-based colors
            low_color = np.array([0.2, 0.6, 0.2])  # Forest green
            high_color = np.array([0.6, 0.4, 0.2])  # Brown
            terrain_colors = (
                low_color[None, None, :]
                + elev_norm[:, :, None] * (high_color - low_color)[None, None, :]
            )
            eco_legend_info = {}
            print(
                "Using elevation-based terrain colors for 3D visualization (no ecological state data)"
            )

        return {
            "elevation_3d": elevation_3d,
            "X_3d": X_3d,
            "Y_3d": Y_3d,
            "terrain_colors": terrain_colors,
            "eco_legend_info": eco_legend_info,
            "elev_min": elev_min,
            "elev_max": elev_max,
            "grid_shape": elevation_3d.shape,
        }

    @staticmethod
    def _generate_3d_plot_fast(
        fire_state: np.ndarray,
        time_hours: float,
        year: int,
        elevation_data: dict,
        output_dir: str,
        use_severity: bool,
        display_label: str,
        colormap_info: dict,
        data: dict,
    ) -> None:
        """Generate 3D plot quickly using pre-computed elevation data.

        Args:
            fire_state: Fire state or severity array
            time_hours: Time in hours
            year: Year number
            elevation_data: Pre-computed elevation data from _precompute_3d_elevation
            output_dir: Output directory
            use_severity: Whether to use fire severity for coloring
            display_label: Label to use for the plot
            colormap_info: Colormap information for fire severity
            data: Original data dictionary
        """
        from pathlib import Path

        import matplotlib.pyplot as plt

        # from mpl_toolkits.mplot3d import Axes3D
        import numpy as np

        # Extract pre-computed data
        elevation_3d = elevation_data["elevation_3d"]
        X_3d = elevation_data["X_3d"]
        Y_3d = elevation_data["Y_3d"]
        terrain_colors = elevation_data["terrain_colors"]
        eco_legend_info = elevation_data.get("eco_legend_info", {})
        elev_min = elevation_data["elev_min"]
        elev_max = elevation_data["elev_max"]

        # Use full resolution fire state (no downsampling)
        fire_state_3d = fire_state

        # Create fire state colors using pre-computed terrain colors
        fire_colors = np.zeros(fire_state_3d.shape + (4,))  # RGBA

        if use_severity:
            # Use severity-based coloring
            unburned_mask = fire_state_3d == 0
            low_severity_mask = fire_state_3d == 1
            moderate_severity_mask = fire_state_3d == 2
            high_severity_mask = fire_state_3d == 3

            # Apply colors based on severity levels
            fire_colors[unburned_mask] = np.column_stack(
                [
                    terrain_colors[unburned_mask],
                    np.full(np.sum(unburned_mask), 0.8),  # Alpha
                ]
            )
            fire_colors[low_severity_mask] = [
                1.0,
                1.0,
                0.6,
                0.9,
            ]  # Light yellow
            fire_colors[moderate_severity_mask] = [
                1.0,
                0.5,
                0.0,
                0.95,
            ]  # Orange
            fire_colors[high_severity_mask] = [0.8, 0.0, 0.0, 0.95]  # Dark red

            # Count cells for each severity level
            low_count = np.sum(low_severity_mask)
            moderate_count = np.sum(moderate_severity_mask)
            high_count = np.sum(high_severity_mask)

            fire_legend_elements = []
            if low_count > 0:
                fire_legend_elements.append(
                    plt.matplotlib.patches.Patch(
                        facecolor=(1.0, 1.0, 0.6),
                        label=f"Low Severity ({low_count:,} cells)",
                    )
                )
            if moderate_count > 0:
                fire_legend_elements.append(
                    plt.matplotlib.patches.Patch(
                        facecolor=(1.0, 0.5, 0.0),
                        label=f"Moderate Severity ({moderate_count:,} cells)",
                    )
                )
            if high_count > 0:
                fire_legend_elements.append(
                    plt.matplotlib.patches.Patch(
                        facecolor=(0.8, 0.0, 0.0),
                        label=f"High Severity ({high_count:,} cells)",
                    )
                )
        else:
            # Use traditional fire state coloring
            unburned_mask = fire_state_3d == 0
            burning_mask = fire_state_3d == 1
            burned_mask = fire_state_3d == 2

            # Apply colors - reuse pre-computed terrain colors for unburned areas
            fire_colors[unburned_mask] = np.column_stack(
                [
                    terrain_colors[unburned_mask],
                    np.full(np.sum(unburned_mask), 0.8),  # Alpha
                ]
            )
            fire_colors[burning_mask] = [1.0, 0.5, 0.0, 0.95]  # Orange
            fire_colors[burned_mask] = [0.25, 0.25, 0.25, 0.9]  # Dark grey

            # Count cells for each fire state
            burning_count = np.sum(burning_mask)
            burned_count = np.sum(burned_mask)

            fire_legend_elements = []
            if burning_count > 0:
                fire_legend_elements.append(
                    plt.matplotlib.patches.Patch(
                        facecolor=(1.0, 0.5, 0.0),
                        label=f"Burning ({burning_count:,} cells)",
                    )
                )
            if burned_count > 0:
                fire_legend_elements.append(
                    plt.matplotlib.patches.Patch(
                        facecolor=(0.25, 0.25, 0.25),
                        label=f"Burned ({burned_count:,} cells)",
                    )
                )

        # Create ecological state legend elements
        eco_legend_elements = []
        if eco_legend_info:
            # Get the affected mask (burned + burning areas) to count only relevant cells
            affected_mask = fire_state_3d > 0  # Only count burned/burning areas
            affected_cells = np.sum(affected_mask)

            # Recalculate counts for only the affected areas
            affected_eco_counts = {}
            if "eco_state_strings" in data or "eco_state" in data:
                # Get the actual ecological state data for accurate counting
                if "eco_state_strings" in data:
                    eco_states_data = data["eco_state_strings"]
                elif "eco_state" in data and "state_id_mapping" in data:
                    # Convert indices to strings
                    eco_indices = data["eco_state"]
                    state_id_mapping = data["state_id_mapping"]
                    if isinstance(state_id_mapping, np.ndarray):
                        state_id_mapping = state_id_mapping.item()

                    if "idx_to_state_id" in state_id_mapping:
                        idx_to_state_id = state_id_mapping["idx_to_state_id"]
                        eco_states_data = np.array(
                            [
                                [idx_to_state_id.get(str(idx), f"State_{idx}") for idx in row]
                                for row in eco_indices
                            ]
                        )
                    else:
                        eco_states_data = np.array(
                            [[f"State_{idx}" for idx in row] for row in eco_indices]
                        )
                else:
                    eco_states_data = None

                if eco_states_data is not None and affected_cells > 0:
                    # Get ecological states for only the affected (burned/burning) areas
                    affected_eco_states = eco_states_data[affected_mask]

                    # Count each state in the affected areas
                    unique_affected_states, counts = np.unique(
                        affected_eco_states, return_counts=True
                    )

                    for state_id, count in zip(unique_affected_states, counts):
                        # Decode bytes if necessary
                        if isinstance(state_id, (bytes, np.bytes_)):
                            state_id = state_id.decode("utf-8")

                        # Get color from legend info
                        if state_id in eco_legend_info:
                            color = eco_legend_info[state_id]["color"]
                        else:
                            # Fallback color if not in legend
                            color = np.array([0.5, 0.5, 0.5])

                        affected_eco_counts[state_id] = {
                            "color": color,
                            "count": int(count),
                        }
                else:
                    affected_eco_counts = {}

            # Sort states by count (most common first) and limit to top 8 for readability
            if affected_eco_counts:
                # Create combined legend showing both burned and total counts for ALL states
                combined_legend_data = []

                # Include all states from the landscape, not just burned ones
                for state_id, total_info in eco_legend_info.items():
                    total_count = total_info["count"]
                    color = total_info["color"]

                    # Get burned count for this state (0 if not burned)
                    burned_count = affected_eco_counts.get(state_id, {}).get("count", 0)

                    combined_legend_data.append(
                        {
                            "state_id": state_id,
                            "burned_count": burned_count,
                            "total_count": total_count,
                            "color": color,
                        }
                    )

                # Sort by total count (most common states first), then by burned count
                combined_legend_data.sort(
                    key=lambda x: (x["total_count"], x["burned_count"]),
                    reverse=True,
                )
                sorted_states = combined_legend_data[:8]  # Limit to top 8
                legend_title = "Ecological States"

                for state_data in sorted_states:
                    state_id = state_data["state_id"]
                    burned_count = state_data["burned_count"]
                    total_count = state_data["total_count"]
                    color = state_data["color"]

                    # Format counts with commas for readability
                    burned_str = f"{burned_count:,}" if burned_count >= 1000 else str(burned_count)
                    total_str = f"{total_count:,}" if total_count >= 1000 else str(total_count)

                    eco_legend_elements.append(
                        plt.matplotlib.patches.Patch(
                            facecolor=tuple(color),
                            label=f"{state_id} ({burned_str} of {total_str} cells burned)",
                        )
                    )
            else:
                # Fallback to original counts if we can't calculate affected counts
                sorted_states = sorted(
                    eco_legend_info.items(),
                    key=lambda x: x[1]["count"],
                    reverse=True,
                )[:8]
                legend_title = "Ecological States (Landscape)"

                for state_id, info in sorted_states:
                    # Format cell count with commas for readability
                    cell_count = info["count"]
                    if cell_count >= 1000:
                        count_str = f"{cell_count:,}"  # Add commas for thousands
                    else:
                        count_str = str(cell_count)

                    eco_legend_elements.append(
                        plt.matplotlib.patches.Patch(
                            facecolor=tuple(info["color"]),
                            label=f"{state_id} ({count_str} cells)",
                        )
                    )

        # Create 3D plot
        fig = plt.figure(figsize=(14, 10))  # Make wider to accommodate legends
        ax = fig.add_subplot(111, projection="3d")

        # Plot surface with pre-computed coordinates and new fire colors
        # Use higher resolution surface plotting for better visual quality
        ax.plot_surface(
            X_3d,
            Y_3d,
            elevation_3d,
            facecolors=fire_colors,
            shade=True,
            linewidth=0,
            antialiased=True,
            alpha=0.9,
            rcount=fire_state_3d.shape[0],  # Force full row resolution
            ccount=fire_state_3d.shape[1],
        )  # Force full column resolution

        # Add contour lines for better visualization (since we're offline, we can afford this)
        contour_levels = np.linspace(elev_min, elev_max, 5)  # More contours for better detail
        ax.contour(
            X_3d,
            Y_3d,
            elevation_3d,
            levels=contour_levels,
            colors="black",
            alpha=0.3,
            linewidths=0.5,
        )

        # remove grid and panes
        ax.grid(False)
        ax.xaxis.pane.fill = False
        ax.yaxis.pane.fill = False
        ax.zaxis.pane.fill = False
        ax.xaxis.pane.set_edgecolor("white")
        ax.yaxis.pane.set_edgecolor("white")
        ax.zaxis.pane.set_edgecolor("white")
        ax.set_axis_off()

        # remove ticks
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_zticks([])

        # Set labels and formatting
        ax.set_xlabel("")
        ax.set_ylabel("")
        ax.set_zlabel("")
        ax.set_title(f"{display_label} on 3D Elevation\n{time_hours:.1f} hours (Year {year})")
        ax.view_init(elev=75, azim=45)

        # Add dual legends - fire severity on upper left, ecological states on upper right
        if fire_legend_elements:
            fire_legend = ax.legend(
                handles=fire_legend_elements,
                loc="upper left",
                title="Fire Status",
                framealpha=0.9,
                fontsize=9,
            )
            fire_legend.set_title("Fire Status", prop={"size": 10, "weight": "bold"})

        if eco_legend_elements:
            # Position the ecological legend on the upper right
            eco_legend = ax.legend(
                handles=eco_legend_elements,
                loc="upper right",
                title=legend_title,
                framealpha=0.9,
                fontsize=8,
                bbox_to_anchor=(1.02, 1.0),
            )
            eco_legend.set_title(legend_title, prop={"size": 9, "weight": "bold"})

            # Add the fire legend back (matplotlib only keeps the last legend by default)
            if fire_legend_elements:
                ax.add_artist(fire_legend)  # Re-add the fire legend

        # Save plot with high quality settings
        prefix = "severity" if use_severity else "fire"
        output_path_3d = (
            Path(output_dir) / f"{prefix}_3d_year_{year:04d}_{int(time_hours*60):06d}.png"
        )
        plt.savefig(
            output_path_3d,
            dpi=600,
            bbox_inches="tight",
            facecolor="white",
            edgecolor="none",
            format="png",
            metadata={"Software": "LaFlammscape"},
        )
        plt.close()

    def _clear_fire_state_variables(self, state: StateRepresentation) -> None:
        """Clear fire-related state variables at the end of each year.

        This prevents fire state from persisting between years and causing
        'flashing' artifacts in multi-year simulations.

        Args:
            state: State representation to clear fire variables from
        """
        fire_variables_to_clear = [
            "fire_state",
            "burn_times",
            "burn_severity",
            "fire_intensity",
            "fire_mortality",
            "fire_effects",
            "fire_flame_length",
            "fire_rate_of_spread",
            "fire_scorch_height",
            "fire_fireline_intensity",
            "flame_length",  # Used by transition module, set by fire behavior/laflammap
            "ignitions",
        ]

        # Note: Weather variables are NOT cleared - they should continue naturally
        # from year to year, with the weather module generating new conditions as needed

        cleared_count = len([v for v in fire_variables_to_clear if state.has_variable(v)])

        for var_name in fire_variables_to_clear:
            if state.has_variable(var_name):
                # Reset to appropriate default value
                if var_name == "fire_state":
                    # Reset to unburned (0)
                    state.set_variable(var_name, np.zeros(state.grid_shape, dtype=np.int8))
                elif var_name == "burn_times":
                    # Reset to infinite (unburned)
                    state.set_variable(
                        var_name,
                        np.full(state.grid_shape, np.inf, dtype=np.float32),
                    )
                elif var_name == "ignitions":
                    # Clear ignition points
                    state.set_variable(var_name, np.zeros(state.grid_shape, dtype=bool))
                else:
                    # Reset fire variables to zero
                    current_var = state.get_variable(var_name)
                    if isinstance(current_var, np.ndarray):
                        state.set_variable(var_name, np.zeros_like(current_var))

        print(
            f"Cleared {cleared_count} fire-related state variables (weather variables preserved for continuity)"
        )

    def simulate_with_windows(
        self,
        state: StateRepresentation,
        ignition_points: List[Tuple[int, int]],
        initial_weather_day: int,
        total_hours: Optional[float] = None,
        weather_module=None,
        output_dir: Optional[str] = None,
    ) -> None:
        """OPTIMIZED: Simulate fire spread in time windows with performance improvements.
        ...
        # Validate initial_weather_day
        if initial_weather_day is None or not (1 <= initial_weather_day <= 366):
            raise ValueError("initial_weather_day must be set to a valid day of year (1-366)")
        self._initial_weather_day = initial_weather_day
        print(f"OPTIMIZATION: Fire simulation starting on day of year {self._initial_weather_day}")
        ...
        """
        if not ignition_points:
            print("No ignition points provided")
            return

        print(
            f"OPTIMIZATION: Starting windowed fire simulation with {len(ignition_points)} ignitions"
        )
        print(
            f"Window size: {self.window_hours} hours, Total time: {total_hours} hours"
            + ("" if total_hours else " (unlimited)")
        )

        # Validate initial_weather_day
        if initial_weather_day is None or not (1 <= initial_weather_day <= 366):
            raise ValueError("initial_weather_day must be set to a valid day of year (1-366)")
        self._initial_weather_day = initial_weather_day
        print(f"OPTIMIZATION: Fire simulation starting on day of year {self._initial_weather_day}")

        # OPTIMIZATION: Pre-allocate arrays and cache dimensions
        grid_shape = state.grid_shape
        cell_size = state.cell_size
        total_cells = grid_shape[0] * grid_shape[1]
        print(f"OPTIMIZATION: Grid {grid_shape}, {total_cells:,} cells, resolution {cell_size}m")

        # Track maximum flame length for each cell
        max_flame_length = np.zeros(grid_shape, dtype=np.float32)

        # OPTIMIZATION: Pre-allocate primary simulation arrays (avoid repeated allocation)
        burn_times = np.full(grid_shape, np.inf, dtype=np.float32)
        fire_state = np.zeros(grid_shape, dtype=np.int8)  # Use int8 to save memory

        # Set ignition points
        for row, col in ignition_points:
            if 0 <= row < grid_shape[0] and 0 <= col < grid_shape[1]:
                burn_times[row, col] = 0.0
                fire_state[row, col] = 1  # Burning

        current_time = 0.0
        simulation_day = initial_weather_day

        window_count = 0

        # OPTIMIZATION: Check if we have cached fuel property arrays
        if self.simulation_interface._fuel_property_arrays is None:
            print("OPTIMIZATION: Generating fuel property arrays (first time)")
            self.simulation_interface._fuel_property_arrays = (
                self.simulation_interface._generate_fuel_property_arrays()
            )
        else:
            print("OPTIMIZATION: Using cached fuel property arrays")

        if self.simulation_interface._fuel_base_rates is None:
            print("OPTIMIZATION: Calculating Rothermel base rates (first time)")
            self.simulation_interface._fuel_base_rates = (
                self.simulation_interface._calculate_rothermel_base_rates()
            )
        else:
            print("OPTIMIZATION: Using cached Rothermel base rates")

        # Main simulation loop
        early_stop_threshold = (
            20  # OPTIMIZATION: Increased from 3 to 20 windows (160+ hours instead of 24 hours)
        )
        no_spread_count = 0

        while True:
            window_count += 1
            window_start = current_time
            window_end = current_time + self.window_hours * 60  # Convert to minutes

            print(
                f"\n=== Window {window_count}: {window_start/60:.1f}-{window_end/60:.1f} hours ==="
            )

            # OPTIMIZATION: Check early stopping condition
            burning_cells = np.sum(fire_state == 1)
            if burning_cells == 0:
                print("OPTIMIZATION: No burning cells remaining - fire extinguished")
                break

            print(
                f"OPTIMIZATION: {burning_cells:,} cells currently burning ({(burning_cells/total_cells)*100:.2f}% of landscape)"  # noqa: E501
            )

            # Time limit check
            if total_hours is not None and window_end / 60 > total_hours:
                print(f"OPTIMIZATION: Reached time limit ({total_hours} hours)")
                break

            # OPTIMIZATION: Update weather conditions efficiently
            if weather_module is not None:
                actual_simulation_day = simulation_day + int(current_time / (24 * 60))
                weather_module._current_day = actual_simulation_day
                weather_module.apply_to_state(state)
                print(f"OPTIMIZATION: Updated weather for simulation day {actual_simulation_day}")

            # OPTIMIZATION: Store burning cells before simulation

            # OPTIMIZATION: Get required arrays efficiently with caching
            fuel_models = state.get_variable("fuel_model")

            # Use cached arrays for moisture data
            moisture_arrays = {}
            for var_name in [
                "fuel_moisture_1hr",
                "fuel_moisture_10hr",
                "fuel_moisture_100hr",
                "fuel_moisture_herb",
                "fuel_moisture_woody",
            ]:
                moisture_arrays[var_name] = self._get_moisture_array(state, var_name)

            wind_arrays = {}
            for var_name in ["weather_wind_speed", "weather_wind_direction"]:
                wind_arrays[var_name] = self._get_wind_array(state, var_name, grid_shape)

            # Get terrain arrays (cached if available)
            if not hasattr(self, "_cached_slope"):
                slope_array = (
                    state.get_variable("slope")
                    if state.has_variable("slope")
                    else np.zeros(grid_shape, dtype=np.float32)
                )
                self._cached_slope = slope_array
            else:
                slope_array = self._cached_slope

            if not hasattr(self, "_cached_aspect"):
                aspect_array = (
                    state.get_variable("aspect")
                    if state.has_variable("aspect")
                    else np.zeros(grid_shape, dtype=np.float32)
                )
                self._cached_aspect = aspect_array
            else:
                aspect_array = self._cached_aspect

            # OPTIMIZATION: Run fire spread simulation with cached arrays
            try:
                result_burn_times = self.simulation_interface.simulate_spread(
                    burn_times=burn_times,
                    fuel_models=fuel_models,
                    moisture_1hr=moisture_arrays["fuel_moisture_1hr"],
                    moisture_10hr=moisture_arrays["fuel_moisture_10hr"],
                    moisture_100hr=moisture_arrays["fuel_moisture_100hr"],
                    moisture_herb=moisture_arrays["fuel_moisture_herb"],
                    moisture_woody=moisture_arrays["fuel_moisture_woody"],
                    wind_speed=wind_arrays["weather_wind_speed"],
                    wind_direction=wind_arrays["weather_wind_direction"],
                    slope=slope_array,
                    aspect=aspect_array,
                    spatial_resolution=cell_size,
                    burn_time_minutes=window_end,
                )

                # OPTIMIZATION: Update arrays in-place
                burn_times[:] = result_burn_times

            except Exception as e:
                print(f"Error in fire spread simulation: {e}")
                break

            # OPTIMIZATION: Update fire state efficiently
            # Cells that burned in this window (finite burn time within window)
            newly_burned = (burn_times <= window_end) & (burn_times < np.inf) & (fire_state != 2)
            fire_state[newly_burned] = 2  # Set to burned

            # Cells still burning (burn time beyond current window OR ignited in this window)
            # FIX: Cells that ignited in this window should continue burning until end of window
            ignited_this_window = (
                (burn_times > window_start) & (burn_times <= window_end) & (burn_times < np.inf)
            )
            still_burning = (burn_times > window_end) & (burn_times < np.inf) | ignited_this_window
            fire_state[still_burning] = 1  # Keep as burning

            # OPTIMIZATION: Calculate spread statistics
            burned_cells = np.sum(fire_state == 2)
            burning_cells = np.sum(fire_state == 1)
            newly_burned_count = np.sum(newly_burned)

            print(f"OPTIMIZATION: Window {window_count} completed:")
            print(f"  Newly burned: {newly_burned_count:,} cells")
            print(f"  Total burned: {burned_cells:,} cells")
            print(f"  Still burning: {burning_cells:,} cells")

            # OPTIMIZATION: Early stopping condition
            if newly_burned_count == 0:
                no_spread_count += 1
                print(
                    f"OPTIMIZATION: No spread detected (count: {no_spread_count}/{early_stop_threshold})"
                )
                if no_spread_count >= early_stop_threshold:
                    print("OPTIMIZATION: Early stop - fire stopped spreading")
                    break
            else:
                no_spread_count = 0  # Reset counter

            # OPTIMIZATION: Update state variables efficiently
            state.set_variable("burn_times", burn_times)
            state.set_variable("fire_state", fire_state)

            # OPTIMIZATION: Calculate fire behavior only if there are burning cells
            if burning_cells > 0:
                fire_behavior = self.behavior_calculator.calculate_fire_behavior(state)
                for key, value in fire_behavior.items():
                    state.set_variable(f"fire_{key}", value)
                # Track max flame length
                if "fire_flame_length" in fire_behavior:
                    max_flame_length = np.maximum(max_flame_length, fire_behavior["flame_length"])
                elif state.has_variable("fire_flame_length"):
                    max_flame_length = np.maximum(
                        max_flame_length,
                        state.get_variable("fire_flame_length"),
                    )

            # OPTIMIZATION: Save visualization data efficiently (if requested)
            if output_dir is not None:
                self._save_fire_state_visualization(fire_state, window_end, output_dir, state)

            # Update time
            current_time = window_end

            print(
                f"OPTIMIZATION: Window {window_count} completed in {window_end/60:.1f} hours total"
            )

        # OPTIMIZATION: Final state update
        final_burned = np.sum(fire_state == 2)
        final_area_ha = (final_burned * (cell_size * cell_size)) / 10000  # Convert m² to hectares

        print("\n=== OPTIMIZATION: Fire Simulation Complete ===")
        print(f"Total windows: {window_count}")
        print(f"Final burned area: {final_burned:,} cells ({final_area_ha:.1f} ha)")
        print(f"Total simulation time: {current_time/60:.1f} hours")

        # OPTIMIZATION: Store final results
        state.set_variable("burn_times", burn_times)
        state.set_variable("fire_state", fire_state)
        state.set_variable("max_flame_length", max_flame_length)

        # OPTIMIZATION: Shutdown data saving thread immediately (no waiting)
        self.shutdown_data_saving()

    def _get_moisture_array(self, state: StateRepresentation, var_name: str) -> np.ndarray:
        """Get moisture array from state, handling both multi-channel and single-channel formats.

        Args:
            state: State representation
            var_name: Variable name to extract

        Returns:
            2D moisture array
        """
        # First check for individual moisture variables
        if var_name in state.state_variables:
            moisture = state.get_variable(var_name)
            if moisture.ndim == 3:
                # Multi-channel format from WeatherModule
                if var_name == "fuel_moisture_1hr":
                    return moisture[..., 0].astype(np.float32)
                elif var_name == "fuel_moisture_10hr":
                    return moisture[..., 1].astype(np.float32)
                elif var_name == "fuel_moisture_100hr":
                    return moisture[..., 2].astype(np.float32)
                elif var_name == "fuel_moisture_herb":
                    return moisture[..., 3].astype(np.float32)
                elif var_name == "fuel_moisture_woody":
                    return moisture[..., 4].astype(np.float32)
            else:
                # Single-channel format
                return moisture.astype(np.float32)

        # Check for multi-channel fuel_moisture variable from WeatherModule
        elif "fuel_moisture" in state.state_variables:
            moisture = state.get_variable("fuel_moisture")
            if moisture.ndim == 3 and moisture.shape[-1] >= 5:
                # Extract the correct channel based on variable name
                if "1hr" in var_name:
                    return moisture[..., 0].astype(np.float32)
                elif "10hr" in var_name:
                    return moisture[..., 1].astype(np.float32)
                elif "100hr" in var_name:
                    return moisture[..., 2].astype(np.float32)
                elif "herb" in var_name:
                    return moisture[..., 3].astype(np.float32)
                elif "woody" in var_name:
                    return moisture[..., 4].astype(np.float32)

        # Default values if variable doesn't exist (should rarely be used now)
        grid_shape = state.grid_shape
        if "1hr" in var_name:
            return np.full(grid_shape, 8.0, dtype=np.float32)
        elif "10hr" in var_name:
            return np.full(grid_shape, 10.0, dtype=np.float32)
        elif "100hr" in var_name:
            return np.full(grid_shape, 12.0, dtype=np.float32)
        elif "herb" in var_name:
            return np.full(grid_shape, 60.0, dtype=np.float32)
        elif "woody" in var_name:
            return np.full(grid_shape, 90.0, dtype=np.float32)
        else:
            return np.full(grid_shape, 10.0, dtype=np.float32)

    def _get_wind_array(
        self,
        state: StateRepresentation,
        var_name: str,
        grid_shape: Tuple[int, int],
    ) -> np.ndarray:
        """Get wind array from state with fallback defaults.

        Args:
            state: State representation
            var_name: Variable name to extract
            grid_shape: Grid shape for default arrays

        Returns:
            2D wind array
        """
        if var_name in state.state_variables:
            return state.get_variable(var_name).astype(np.float32)
        else:
            # Default values
            if "speed" in var_name:
                return np.full(grid_shape, 10.0, dtype=np.float32)  # 10 mph default
            else:  # direction
                return np.full(grid_shape, 270.0, dtype=np.float32)  # West wind default

    def _update_state_for_next_window(
        self, state: StateRepresentation, start_time: float, end_time: float
    ) -> None:
        """Update state variables for the next simulation window.
        Args:
            state: Landscape state to update
            start_time: Start time of current window (minutes)
            end_time: End time of current window (minutes)
        """
        if state.has_variable("weather_temperature"):
            temp = state.get_variable("weather_temperature")
            if isinstance(temp, np.ndarray):
                temp = np.array(temp)
            state.set_variable("weather_temperature", temp * 1.1)
        if state.has_variable("weather_humidity"):
            humidity = state.get_variable("weather_humidity")
            if isinstance(humidity, np.ndarray):
                humidity = np.array(humidity)
            state.set_variable("weather_humidity", humidity * 0.9)
        if state.has_variable("fuel_moisture_1hr"):
            moisture = state.get_variable("fuel_moisture_1hr")
            if isinstance(moisture, np.ndarray):
                moisture = np.array(moisture)
            state.set_variable("fuel_moisture_1hr", moisture * 0.95)
        if state.has_variable("weather_wind_speed"):
            wind = state.get_variable("weather_wind_speed")
            if isinstance(wind, np.ndarray):
                wind = np.array(wind)
            state.set_variable("weather_wind_speed", wind * 1.2)

    @staticmethod
    def _create_ecological_terrain_colors(
        data: dict, elevation_3d: np.ndarray, elev_norm: np.ndarray
    ) -> tuple:
        """Create terrain colors based on ecological states with elevation shading.

        Args:
            data: Data dictionary containing ecological state information
            elevation_3d: Elevation array
            elev_norm: Normalized elevation (0-1)

        Returns:
            Tuple of (RGB color array, legend_info dict)
        """
        import numpy as np

        # Get ecological state data
        if "eco_state_strings" in data:
            eco_states = data["eco_state_strings"]
            print(f"Using string ecological states: {np.unique(eco_states)}")
        elif "eco_state" in data:
            eco_states = data["eco_state"]
            # Convert indices to strings if we have mapping
            if "state_id_mapping" in data and "idx_to_state_id" in data["state_id_mapping"]:
                idx_to_state_id = data["state_id_mapping"]["idx_to_state_id"]
                eco_states = np.array(
                    [
                        [idx_to_state_id.get(str(idx), f"State_{idx}") for idx in row]
                        for row in eco_states
                    ]
                )
                print(f"Converted ecological state indices to strings: {np.unique(eco_states)}")
            else:
                # Use numeric states as strings
                eco_states = np.array([[f"State_{idx}" for idx in row] for row in eco_states])
                print(f"Using numeric ecological states as strings: {np.unique(eco_states)}")
        else:
            # Fallback - create uniform state
            eco_states = np.full(elevation_3d.shape, "Unknown", dtype=object)
            print("No ecological state data found - using uniform colors")

        # Define ecological state color palette - AVOID fire severity colors (yellow, orange, red)
        # Use blues, greens, purples, and browns to distinguish from fire colors
        state_colors = {
            # CDC (Canadian Boreal) states - deep greens and blue-greens (avoid yellow-green)
            "CDC-1A": np.array([0.0, 0.3, 0.1]),  # Very dark forest green (mature conifer)
            "CDC-1B": np.array([0.1, 0.4, 0.2]),  # Dark forest green
            "CDC-2A": np.array([0.1, 0.5, 0.3]),  # Forest green (younger forest)
            "CDC-2B": np.array([0.2, 0.5, 0.4]),  # Blue-green
            "CDC-3A": np.array([0.3, 0.6, 0.5]),  # Teal (regeneration)
            "CDC-3B": np.array([0.2, 0.6, 0.6]),  # Light teal
            "CDC-4A": np.array([0.4, 0.3, 0.2]),  # Brown (grass/shrub)
            "CDC-4B": np.array([0.5, 0.4, 0.3]),  # Light brown
            "CDC-5A": np.array([0.3, 0.2, 0.1]),  # Dark brown (shrub/sparse)
            "CDC-5B": np.array([0.4, 0.3, 0.2]),  # Medium brown
            # CMC (Coastal/Mixed) states - blues and blue-greens
            "CMC-1A": np.array([0.0, 0.2, 0.3]),  # Dark blue-green (coastal forest)
            "CMC-1B": np.array([0.1, 0.3, 0.4]),  # Blue-green
            "CMC-2A": np.array([0.0, 0.4, 0.4]),  # Cyan-green
            "CMC-2B": np.array([0.1, 0.4, 0.5]),  # Light blue-green
            "CMC-3A": np.array([0.2, 0.5, 0.6]),  # Light cyan
            "CMC-3B": np.array([0.3, 0.5, 0.6]),  # Pale blue
            "CMC-4A": np.array([0.2, 0.3, 0.5]),  # Blue (coastal shrub)
            "CMC-4B": np.array([0.3, 0.4, 0.6]),  # Light blue
            "CMC-5A": np.array([0.4, 0.3, 0.5]),  # Purple-brown
            "CMC-5B": np.array([0.5, 0.4, 0.6]),  # Light purple-brown
            # Generic fallback colors for unknown states
            "Unknown": np.array([0.3, 0.3, 0.3]),  # Dark gray
        }

        # Initialize color array
        terrain_colors = np.zeros(elevation_3d.shape + (3,), dtype=np.float32)

        # Get unique states and assign colors
        unique_states = np.unique(eco_states)
        print(f"Creating colors for {len(unique_states)} unique ecological states")

        # Track legend information
        legend_info = {}

        # Collect existing predefined colors to avoid conflicts
        existing_colors = [color for color in state_colors.values()]

        # Generate additional colors for unknown states
        unknown_states = [
            state
            for state in unique_states
            if (state.decode("utf-8") if isinstance(state, (bytes, np.bytes_)) else state)
            not in state_colors
        ]

        if unknown_states:
            additional_colors = FireSimulationOrchestrator._generate_well_separated_colors(
                len(unknown_states), existing_colors
            )
            print(f"Generated {len(additional_colors)} well-separated colors for unknown states")
        else:
            additional_colors = []

        # Create colors for each state
        unknown_color_idx = 0
        for i, state_id in enumerate(unique_states):
            # Decode bytes if necessary
            if isinstance(state_id, (bytes, np.bytes_)):
                state_id = state_id.decode("utf-8")

            # Get base color for this state
            if state_id in state_colors:
                base_color = state_colors[state_id]
            else:
                # Use pre-generated well-separated color
                if unknown_color_idx < len(additional_colors):
                    base_color = np.array(additional_colors[unknown_color_idx])
                    unknown_color_idx += 1
                    print(f"Assigned well-separated color to '{state_id}': {base_color}")
                else:
                    # Fallback to original method if we somehow run out
                    hash_val = hash(str(state_id)) % 240
                    if hash_val > 60 and hash_val < 180:
                        hash_val = (hash_val - 60) * 0.5 + 180

                    import colorsys

                    base_color = np.array(colorsys.hsv_to_rgb(hash_val / 360.0, 0.7, 0.6))
                    print(f"Fallback color for '{state_id}': {base_color}")

            # Find cells with this state
            state_mask = eco_states == state_id

            # Apply base color with elevation shading
            # Darken at low elevations, lighten at high elevations
            elevation_factor = 0.6 + 0.7 * elev_norm  # Range 0.6-1.3

            for channel in range(3):
                terrain_colors[state_mask, channel] = np.clip(
                    base_color[channel] * elevation_factor[state_mask],
                    0.0,
                    1.0,
                )

            cell_count = np.sum(state_mask)
            if cell_count > 0:  # Only add to legend if state is present
                legend_info[state_id] = {
                    "color": base_color,
                    "count": cell_count,
                }
            print(f"State '{state_id}': {cell_count} cells, color {base_color}")

        return terrain_colors, legend_info

    @staticmethod
    def _generate_well_separated_colors(num_colors: int, existing_colors: list = None) -> list:
        """Generate visually distinct colors for ecological states.

        Uses perceptually uniform color spacing to ensure good visual separation.
        Avoids fire colors (yellow, orange, red) and ensures minimum perceptual distance.

        Args:
            num_colors: Number of colors to generate
            existing_colors: List of existing colors to avoid (RGB tuples)

        Returns:
            List of RGB color tuples
        """
        import colorsys

        import numpy as np

        if existing_colors is None:
            existing_colors = []

        # Define cool color ranges (avoiding fire colors)
        # Hue ranges: blues (180-240°), blue-greens (120-180°), purples (240-300°), browns (20-60°)
        cool_hue_ranges = [
            (180, 240),  # Blues
            (120, 180),  # Blue-greens
            (240, 300),  # Purples
            (20, 60),  # Browns (earth tones)
        ]

        colors = []
        attempts = 0
        max_attempts = num_colors * 50  # Prevent infinite loops

        while len(colors) < num_colors and attempts < max_attempts:
            attempts += 1

            # Choose a hue range
            hue_range = cool_hue_ranges[len(colors) % len(cool_hue_ranges)]

            # Generate color with good spacing
            if len(colors) == 0:
                # First color - use middle of first range
                hue = (hue_range[0] + hue_range[1]) / 2
            else:
                # Subsequent colors - try to maximize distance from existing colors
                hue = hue_range[0] + (hue_range[1] - hue_range[0]) * (len(colors) / num_colors)

            # Vary saturation and value for additional distinction
            saturation = 0.6 + 0.3 * (len(colors) % 3) / 2  # 0.6-0.9
            value = 0.5 + 0.4 * ((len(colors) + 1) % 3) / 2  # 0.5-0.9

            # Convert to RGB
            rgb = np.array(colorsys.hsv_to_rgb(hue / 360.0, saturation, value))

            # Check minimum distance from existing colors (perceptual distance)
            min_distance = float("in")
            for existing_rgb in existing_colors + colors:
                # Simple Euclidean distance in RGB space (could use LAB for better perceptual uniformity)
                distance = np.sqrt(np.sum((rgb - np.array(existing_rgb)) ** 2))
                min_distance = min(min_distance, distance)

            # Accept color if it's sufficiently different (threshold of 0.3 in RGB space)
            if min_distance > 0.3 or len(colors) == 0:
                colors.append(tuple(rgb))
            elif attempts > max_attempts * 0.8:
                # If we're struggling to find distinct colors, lower the threshold
                if min_distance > 0.2:
                    colors.append(tuple(rgb))

        return colors

    @staticmethod
    def generate_severity_by_ecostate_summary(
        data_dir: str, output_dir: str = None, specific_year: int = None
    ) -> None:
        """Generate summary statistics of fire severity by ecological state.

        Creates bar charts and tables showing how many cells of each ecological state
        burned at different severity levels.

        Args:
            data_dir: Directory containing .npz fire data files
            output_dir: Directory to save summary (defaults to data_dir/summary)
            specific_year: If provided, only analyze data from this specific year
        """
        import glob
        import os
        from collections import defaultdict
        from pathlib import Path

        import numpy as np
        import pandas as pd

        if output_dir is None:
            output_dir = Path(data_dir) / "summary"

        os.makedirs(output_dir, exist_ok=True)

        # Find all data files (both HDF5 and NPZ formats)
        h5_files = glob.glob(os.path.join(data_dir, "fire_data_*.h5"))
        npz_files = glob.glob(os.path.join(data_dir, "fire_data_*.npz"))
        data_files = h5_files + npz_files
        data_files.sort()

        print(
            f"Found {len(data_files)} fire data files for severity analysis ({len(h5_files)} HDF5, {len(npz_files)} NPZ)"  # noqa: E501
        )

        # Group files by year
        year_files = defaultdict(list)
        for data_file in data_files:
            # Extract year from filename (e.g., fire_data_year_0002_000000.h5 or .npz)
            filename = os.path.basename(data_file)
            year_part = filename.split("_")[3]  # Should be something like '0002'
            year = int(year_part)
            year_files[year].append(data_file)

        print(f"Found data for {len(year_files)} years: {sorted(year_files.keys())}")

        # Filter by year if specified
        if specific_year is not None:
            if specific_year in year_files:
                year_files = {specific_year: year_files[specific_year]}
                print(f"Analyzing only year {specific_year}")
            else:
                print(f"Year {specific_year} not found in data")
                return

        # Analyze each year separately
        all_year_results = []

        for year in sorted(year_files.keys()):
            print(f"\n=== Analyzing Year {year} ===")
            data_files_year = sorted(year_files[year])

            # Track maximum severity reached for each cell across all timesteps in this year
            max_severity_grid = None
            eco_states_reference = None
            eco_severity_stats = defaultdict(lambda: defaultdict(int))
            eco_total_counts = defaultdict(int)
            all_eco_states = set()

            for i, data_file in enumerate(data_files_year):
                try:
                    # Load data using the unified loader
                    data = FireSimulationOrchestrator._load_data_file(data_file)
                    fire_state = data["fire_state"]
                    time_hours = float(data["time_hours"])

                    if i % 100 == 0:  # Print progress every 100 files
                        print(
                            f"Processing {i+1}/{len(data_files_year)}: {Path(data_file).name} ({time_hours:.1f}h)"
                        )

                    # Calculate fire severity
                    fire_severity, _, _ = FireSimulationOrchestrator._calculate_fire_severity(
                        fire_state, data, time_hours
                    )

                    # Get ecological state data
                    eco_states_data = None
                    if "eco_state_strings" in data:
                        eco_states_data = data["eco_state_strings"]
                    elif "eco_state" in data and "state_id_mapping" in data:
                        eco_indices = data["eco_state"]
                        state_id_mapping = data["state_id_mapping"]
                        if isinstance(state_id_mapping, np.ndarray):
                            state_id_mapping = state_id_mapping.item()

                        if "idx_to_state_id" in state_id_mapping:
                            idx_to_state_id = state_id_mapping["idx_to_state_id"]
                            eco_states_data = np.array(
                                [
                                    [idx_to_state_id.get(str(idx), f"State_{idx}") for idx in row]
                                    for row in eco_indices
                                ]
                            )

                    if eco_states_data is not None:
                        # Initialize grids on first timestep
                        if max_severity_grid is None:
                            max_severity_grid = np.zeros_like(fire_severity)
                            eco_states_reference = eco_states_data.copy()

                        # Update maximum severity reached for each cell
                        max_severity_grid = np.maximum(max_severity_grid, fire_severity)

                        # Count total cells for each ecological state (do this once)
                        if i == 0:  # Only count on first timestep to avoid duplicates
                            unique_states, state_counts = np.unique(
                                eco_states_data, return_counts=True
                            )
                            for state_id, count in zip(unique_states, state_counts):
                                if isinstance(state_id, (bytes, np.bytes_)):
                                    state_id = state_id.decode("utf-8")
                                all_eco_states.add(state_id)
                                eco_total_counts[state_id] = int(count)

                except Exception as e:
                    if i < 5:  # Only print first few errors to avoid spam
                        print(f"Error processing {data_file}: {e}")
                    continue

            # Count final severity statistics for this year
            if max_severity_grid is not None and eco_states_reference is not None:
                print(f"Calculating final severity statistics for year {year}...")

                for severity_level in [
                    0,
                    1,
                    2,
                    3,
                ]:  # unburned, low, moderate, high
                    severity_mask = max_severity_grid == severity_level
                    if np.any(severity_mask):
                        affected_eco_states = eco_states_reference[severity_mask]
                        unique_affected, affected_counts = np.unique(
                            affected_eco_states, return_counts=True
                        )

                        for state_id, count in zip(unique_affected, affected_counts):
                            if isinstance(state_id, (bytes, np.bytes_)):
                                state_id = state_id.decode("utf-8")
                            eco_severity_stats[state_id][severity_level] = int(count)

                # Create summary for this year
                year_summary = []
                total_burned_this_year = 0

                # First pass: calculate total burned for this year
                for state_id in sorted(all_eco_states):
                    if state_id in eco_severity_stats:
                        total_burned = (
                            eco_severity_stats[state_id][1]
                            + eco_severity_stats[state_id][2]
                            + eco_severity_stats[state_id][3]
                        )
                        total_burned_this_year += total_burned

                # Second pass: create summary with burned area percentages
                for state_id in sorted(all_eco_states):
                    if state_id in eco_severity_stats:
                        row = {
                            "Year": year,
                            "Ecological_State": state_id,
                            "Total_Cells": eco_total_counts[state_id],
                            "Unburned": eco_severity_stats[state_id][0],
                            "Low_Severity": eco_severity_stats[state_id][1],
                            "Moderate_Severity": eco_severity_stats[state_id][2],
                            "High_Severity": eco_severity_stats[state_id][3],
                        }
                        row["Total_Burned"] = (
                            row["Low_Severity"] + row["Moderate_Severity"] + row["High_Severity"]
                        )
                        row["Burn_Percentage"] = (
                            (row["Total_Burned"] / row["Total_Cells"] * 100)
                            if row["Total_Cells"] > 0
                            else 0
                        )
                        row["Burned_Area_Percentage"] = (
                            (row["Total_Burned"] / total_burned_this_year * 100)
                            if total_burned_this_year > 0
                            else 0
                        )
                        year_summary.append(row)
                        all_year_results.append(row)

                # Print summary for this year
                burned_states = [row for row in year_summary if row["Total_Burned"] > 0]
                if burned_states:
                    total_burned_all_states = sum(row["Total_Burned"] for row in burned_states)
                    print(
                        f"\nYear {year} - States that burned (Total burned: {total_burned_all_states:,} cells):"
                    )
                    for row in sorted(
                        burned_states,
                        key=lambda x: x["Total_Burned"],
                        reverse=True,
                    )[
                        :10
                    ]:  # Top 10
                        burned_pct_of_state = row["Burn_Percentage"]
                        burned_pct_of_total = (
                            (row["Total_Burned"] / total_burned_all_states * 100)
                            if total_burned_all_states > 0
                            else 0
                        )
                        print(
                            f"  {row['Ecological_State']}: {row['Total_Burned']:,} cells ({burned_pct_of_state:.1f}% of state, {burned_pct_of_total:.1f}% of total burned area)"  # noqa: E501
                        )
                else:
                    print(f"Year {year}: No burning detected")

        # Save comprehensive results
        if all_year_results:
            df_all = pd.DataFrame(all_year_results)

            # Save detailed CSV with all years
            csv_path = Path(output_dir) / "fire_severity_by_ecostate_all_years.csv"
            df_all.to_csv(csv_path, index=False)
            print(f"\nSaved detailed results: {csv_path}")

            # Create summary by state across all years
            state_totals = (
                df_all.groupby("Ecological_State")
                .agg(
                    {
                        "Total_Cells": "first",  # Should be same across years
                        "Total_Burned": "sum",
                        "Low_Severity": "sum",
                        "Moderate_Severity": "sum",
                        "High_Severity": "sum",
                    }
                )
                .reset_index()
            )
            state_totals["Burn_Percentage"] = (
                state_totals["Total_Burned"] / state_totals["Total_Cells"] * 100
            )

            # Add percentage of total burned area
            total_burned_overall = state_totals["Total_Burned"].sum()
            state_totals["Burned_Area_Percentage"] = (
                (state_totals["Total_Burned"] / total_burned_overall * 100)
                if total_burned_overall > 0
                else 0
            )

            state_totals = state_totals.sort_values("Total_Burned", ascending=False)

            # Save state summary
            csv_summary_path = Path(output_dir) / "fire_severity_by_ecostate.csv"
            state_totals.to_csv(csv_summary_path, index=False)
            print(f"Saved state summary: {csv_summary_path}")

            # Print top burning states across all years
            print(
                f"\nTop ecological states by total burning across all years (Total burned: {total_burned_overall:,} cells):"  # noqa: E501
            )
            print(
                f"{'State':<10} {'Total':<8} {'Burned':<8} {'Low':<6} {'Mod':<6} {'High':<6} {'%State':<7} {'%Burned':<8}"  # noqa: E501
            )
            print("-" * 75)
            for _, row in state_totals.head(10).iterrows():
                print(
                    f"{row['Ecological_State']:<10} {row['Total_Cells']:<8} {row['Total_Burned']:<8} "
                    f"{row['Low_Severity']:<6} {row['Moderate_Severity']:<6} {row['High_Severity']:<6} "
                    f"{row['Burn_Percentage']:<7.1f} {row['Burned_Area_Percentage']:<8.1f}"
                )

        print(f"Fire severity analysis complete. Results saved to {output_dir}")
