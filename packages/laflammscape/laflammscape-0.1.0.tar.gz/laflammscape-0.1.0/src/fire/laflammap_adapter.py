"""LaflamMap Adapter module implementation.

Provides integration between the laflammscape framework and the laflammap
fire simulation model, allowing high-performance GPU-based fire spread modeling.
"""

import logging
from typing import Any, Dict, List, Tuple

import numpy as np
import tensorflow as tf

# Import LaflamMap components if they are available
try:
    from laflammap.core.simulation import FlamMapSimulator

    LAFLAMMAP_AVAILABLE = True
except ImportError:
    LAFLAMMAP_AVAILABLE = False
    logging.warning("LaflamMap not found. LaflamMapAdapter will not be functional.")

from ..state.representation import StateRepresentation
from .simulation import FireSimulationInterface, FireSpreadAlgorithm


class LaflamMapAdapter(FireSimulationInterface):
    """Adapter for integrating LaflamMap with Laflammscape.

    Features:
    - GPU-accelerated fire spread simulation
    - Conversion between laflammscape and laflammap data structures
    - Support for all laflammap simulation features
    """

    # Class variable for test mode
    TEST_MODE = False

    @classmethod
    def enable_test_mode(cls):
        """Enable test mode to allow testing without laflammap installed."""
        cls.TEST_MODE = True
        logging.info("LaflamMapAdapter test mode enabled")

    def __init__(
        self,
        device: str = "/GPU:0",
        spatial_resolution: float = 30.0,
        temporal_resolution: float = 60.0,
        max_iterations: int = 1000,
    ):
        """Initialize the LaflamMap adapter.

        Args:
            device: TensorFlow device to use (e.g., "/GPU:0", "/CPU:0")
            spatial_resolution: Spatial resolution in meters
            temporal_resolution: Temporal resolution in minutes
            max_iterations: Maximum number of iterations for simulation

        Raises:
            ImportError: If laflammap is not available and not in test mode
        """
        super().__init__(
            algorithm=FireSpreadAlgorithm.MINIMUM_TRAVEL_TIME,
            spatial_resolution=spatial_resolution,
            max_iterations=max_iterations,
        )

        if not LAFLAMMAP_AVAILABLE and not self.__class__.TEST_MODE:
            raise ImportError("LaflamMap is required but not installed or available.")

        self.device = device
        self.temporal_resolution = temporal_resolution

        # Only initialize the actual simulator if laflammap is available
        if LAFLAMMAP_AVAILABLE:
            self.simulator = FlamMapSimulator(device=device)
        else:
            # Create a mock simulator for test mode
            class MockSimulator:
                def __init__(self, device):
                    self.device = device
                    self.landscape = None
                    self.weather = None
                    self.fuel_models = []

                def load_landscape(self, landscape_data):
                    self.landscape = landscape_data

                def load_weather(self, weather_data):
                    self.weather = weather_data

                def load_fuel_models(self, fuel_models):
                    self.fuel_models = fuel_models

                def calculate_fire_spread(self, ignition_points, time_steps):
                    # Create mock fire spread results
                    height, width = 20, 20  # Default size

                    # Extract actual grid size if available
                    if hasattr(self.landscape, "elevation") and hasattr(
                        self.landscape.elevation, "shape"
                    ):
                        height, width = self.landscape.elevation.shape
                    elif isinstance(self.landscape, dict) and "elevation" in self.landscape:
                        height, width = self.landscape["elevation"].shape

                    fire_spread = np.zeros((time_steps, height, width))
                    fire_intensity = np.zeros((time_steps, height, width))
                    flame_length = np.zeros((time_steps, height, width))

                    # Add ignition points
                    ignition_list = ignition_points.numpy()
                    for r, c in ignition_list:
                        if 0 <= r < height and 0 <= c < width:
                            fire_spread[0, r, c] = 1.0
                            fire_intensity[0, r, c] = 500.0
                            flame_length[0, r, c] = 1.5

                    # Simple fire spread for testing - grow by one cell in each direction
                    for t in range(1, time_steps):
                        for r in range(height):
                            for c in range(width):
                                if fire_spread[t - 1, r, c] > 0:
                                    for dr in [-1, 0, 1]:
                                        for dc in [-1, 0, 1]:
                                            nr, nc = r + dr, c + dc
                                            if 0 <= nr < height and 0 <= nc < width:
                                                fire_spread[t, nr, nc] = 1.0
                                                fire_intensity[t, nr, nc] = 500.0
                                                flame_length[t, nr, nc] = 1.5

                    # Convert to TensorFlow tensors
                    return {
                        "fire_spread": tf.convert_to_tensor(fire_spread),
                        "fire_intensity": tf.convert_to_tensor(fire_intensity),
                        "flame_length": tf.convert_to_tensor(flame_length),
                    }

            self.simulator = MockSimulator(device=device)

        self.variable_mapping = {
            # Laflammscape variable name -> LaflamMap attribute
            "elevation": "elevation",
            "slope": "slope",
            "aspect": "aspect",
            "fuel_model": "fuel",
            "canopy_cover": "cover",
            "canopy_height": "height",
            "canopy_base_height": "base_height",
            "canopy_bulk_density": "bulk_density",
            "duff_loading": "du",
            "woody_fuel_loading": "woody_fuel",
            # Weather variables
            "weather_temperature": "temperature",
            "weather_humidity": "humidity",
            "weather_precipitation": "precipitation",
            "weather_wind_speed": "wind_speed",
            "weather_wind_direction": "wind_direction",
        }

        # Initialize caches for converted data
        self._landscape_data_cache = None
        self._weather_data_cache = None
        self._fuel_models_cache = []

        # Conversion settings
        self.cell_size_meters = spatial_resolution
        self.latitude = 40.0  # Default latitude

        logging.info(f"LaflamMap adapter initialized with device: {device}")

    def set_variable_mapping(self, mapping: Dict[str, str]) -> None:
        """Set a custom variable mapping between Laflammscape and LaflamMap.

        Args:
            mapping: Dictionary mapping Laflammscape variable names to LaflamMap attributes
        """
        self.variable_mapping.update(mapping)

    def set_latitude(self, latitude: float) -> None:
        """Set the latitude for fire simulations.

        Args:
            latitude: Latitude in degrees (affects solar radiation calculations)
        """
        self.latitude = latitude

    def _create_landscape_data(self, state: StateRepresentation) -> Any:
        """Convert Laflammscape state to LaflamMap LandscapeData.

        Args:
            state: Current Laflammscape state

        Returns:
            LaflamMap LandscapeData object

        Raises:
            ValueError: If required variables are missing
        """
        # Cache validity check
        if self._landscape_data_cache is not None:
            return self._landscape_data_cache

        # Get required variables
        landscape_data = {}
        required_vars = ["elevation", "slope", "aspect", "fuel_model"]
        optional_vars = [
            "canopy_cover",
            "canopy_height",
            "canopy_base_height",
            "canopy_bulk_density",
            "duff_loading",
            "woody_fuel_loading",
        ]

        for var_name in required_vars:
            laflammap_name = self.variable_mapping.get(var_name)
            if var_name not in state.state_variables:
                raise ValueError(f"Required variable not found: {var_name}")
            landscape_data[laflammap_name] = tf.convert_to_tensor(
                state.get_variable(var_name), dtype=tf.float32
            )

        # Add optional variables if available
        for var_name in optional_vars:
            laflammap_name = self.variable_mapping.get(var_name)
            if var_name in state.state_variables:
                landscape_data[laflammap_name] = tf.convert_to_tensor(
                    state.get_variable(var_name), dtype=tf.float32
                )
            else:
                # Create zeros tensor for missing variables
                landscape_data[laflammap_name] = tf.zeros_like(landscape_data["elevation"])

        # Calculate UTM bounds (placeholder - in a real implementation, would use actual UTM coordinates)
        grid_shape = state.grid_shape
        west = 0
        east = west + grid_shape[1] * self.cell_size_meters
        south = 0
        north = south + grid_shape[0] * self.cell_size_meters

        # Create LandscapeData object
        if LAFLAMMAP_AVAILABLE:
            from laflammap.core.data_structures import LandscapeData

            landscape_obj = LandscapeData(
                elevation=landscape_data["elevation"],
                slope=landscape_data["slope"],
                aspect=landscape_data["aspect"],
                fuel=landscape_data["fuel"],
                cover=landscape_data["cover"],
                height=landscape_data["height"],
                base_height=landscape_data["base_height"],
                bulk_density=landscape_data["bulk_density"],
                duff=landscape_data["du"],
                woody_fuel=landscape_data["woody_fuel"],
                grid_units=0,  # 0 for metric
                x_resolution=self.cell_size_meters,
                y_resolution=self.cell_size_meters,
                utm_bounds=(west, east, south, north),
                latitude=int(self.latitude),
            )
        elif self.__class__.TEST_MODE:
            # Import the mock class for test mode
            from tests.unit.test_laflammap_adapter import MockLandscapeData

            # Create a mock LandscapeData object that wraps the dictionary
            landscape_obj = MockLandscapeData()

            # Add dictionary items as attributes
            for key, value in landscape_data.items():
                setattr(landscape_obj, key, value)

            # Add other attributes
            setattr(landscape_obj, "grid_units", 0)
            setattr(landscape_obj, "x_resolution", self.cell_size_meters)
            setattr(landscape_obj, "y_resolution", self.cell_size_meters)
            setattr(landscape_obj, "utm_bounds", (west, east, south, north))
            setattr(landscape_obj, "latitude", int(self.latitude))
        else:
            # For testing when laflammap is not available
            landscape_obj = landscape_data

        # Cache for reuse
        self._landscape_data_cache = landscape_obj

        return landscape_obj

    def _create_weather_data(self, state: StateRepresentation) -> Any:
        """Convert Laflammscape state to LaflamMap WeatherData.

        Args:
            state: Current Laflammscape state

        Returns:
            LaflamMap WeatherData object

        Raises:
            ValueError: If required weather variables are missing
        """
        # Cache validity check
        if self._weather_data_cache is not None:
            return self._weather_data_cache

        # Check for required weather variables
        required_weather = [
            "weather_temperature",
            "weather_humidity",
            "weather_wind_speed",
            "weather_wind_direction",
        ]

        for var_name in required_weather:
            if var_name not in state.state_variables:
                raise ValueError(f"Required weather variable not found: {var_name}")

        # Get weather data from state
        temperature = state.get_variable("weather_temperature")
        humidity = state.get_variable("weather_humidity")
        wind_speed = state.get_variable("weather_wind_speed")
        wind_direction = state.get_variable("weather_wind_direction")

        # Precipitation is optional with default of 0
        if "weather_precipitation" in state.state_variables:
            precipitation = state.get_variable("weather_precipitation")
        else:
            precipitation = np.zeros_like(temperature)

        # Convert from 2D grids to 1D time series (use mean values for simplicity)
        # In a real implementation, this might be more sophisticated based on location
        temp_mean = float(np.mean(temperature))
        humidity_mean = float(np.mean(humidity))
        precip_mean = float(np.mean(precipitation))
        wind_speed_mean = float(np.mean(wind_speed))
        wind_dir_mean = float(np.mean(wind_direction))

        # Create weather time series (1 time step for now)
        # Could be extended to support multiple time steps
        temp_tensor = tf.convert_to_tensor([temp_mean], dtype=tf.float32)
        humidity_tensor = tf.convert_to_tensor([humidity_mean], dtype=tf.float32)
        precip_tensor = tf.convert_to_tensor([precip_mean], dtype=tf.float32)
        wind_speed_tensor = tf.convert_to_tensor([wind_speed_mean], dtype=tf.float32)
        wind_dir_tensor = tf.convert_to_tensor([wind_dir_mean], dtype=tf.float32)

        # Simple cloudiness and solar radiation estimates
        cloudiness = tf.convert_to_tensor([0.0], dtype=tf.float32)  # Clear sky
        solar_radiation = tf.convert_to_tensor(
            [800.0], dtype=tf.float32
        )  # W/m2 (typical clear day)

        # Create time steps tensor - month, day, hour (e.g., July 15, 14:00)
        time_steps = tf.convert_to_tensor([[7, 15, 14]], dtype=tf.int32)

        # Create WeatherData object
        if LAFLAMMAP_AVAILABLE:
            from laflammap.core.data_structures import WeatherData

            weather_obj = WeatherData(
                temperature=temp_tensor,
                humidity=humidity_tensor,
                precipitation=precip_tensor,
                wind_speed=wind_speed_tensor,
                wind_direction=wind_dir_tensor,
                cloudiness=cloudiness,
                time_steps=time_steps,
                solar_radiation=solar_radiation,
            )
        elif self.__class__.TEST_MODE:
            # Import the mock class for test mode
            from tests.unit.test_laflammap_adapter import MockWeatherData

            # Create a mock WeatherData object
            weather_obj = MockWeatherData()

            # Add attributes
            setattr(weather_obj, "temperature", temp_tensor)
            setattr(weather_obj, "humidity", humidity_tensor)
            setattr(weather_obj, "precipitation", precip_tensor)
            setattr(weather_obj, "wind_speed", wind_speed_tensor)
            setattr(weather_obj, "wind_direction", wind_dir_tensor)
            setattr(weather_obj, "cloudiness", cloudiness)
            setattr(weather_obj, "time_steps", time_steps)
            setattr(weather_obj, "solar_radiation", solar_radiation)
        else:
            # For testing when laflammap is not available
            weather_obj = {
                "temperature": temp_tensor,
                "humidity": humidity_tensor,
                "precipitation": precip_tensor,
                "wind_speed": wind_speed_tensor,
                "wind_direction": wind_dir_tensor,
            }

        # Cache for reuse
        self._weather_data_cache = weather_obj

        return weather_obj

    def _create_fuel_models(self, state: StateRepresentation) -> List[Any]:
        """Convert Laflammscape fuel models to LaflamMap FuelModel objects.

        Args:
            state: Current Laflammscape state

        Returns:
            List of LaflamMap FuelModel objects
        """
        # Cache validity check
        if self._fuel_models_cache:
            return self._fuel_models_cache

        # Get unique fuel model ids from state
        fuel_model_grid = state.get_variable("fuel_model")
        unique_ids = np.unique(fuel_model_grid)

        # Standard fuel model parameters (simplified for this example)
        # In a real implementation, these would come from a database or file
        standard_models = {}

        if LAFLAMMAP_AVAILABLE:
            from laflammap.core.data_structures import FuelModel

            # Scott & Burgan fuel models (abbreviated selection)
            # Grass models
            standard_models[101] = FuelModel(
                number=101,
                code="GR1",
                h1=0.1,
                h10=0.0,
                h100=0.0,
                lh=0.3,
                lw=0.0,
                dynamic=1,
                sav1=2200,
                savlh=2000,
                savlw=1800,
                depth=0.4,
                xmext=15,
                heatd=8000,
                heatl=8000,
            )
            standard_models[102] = FuelModel(
                number=102,
                code="GR2",
                h1=0.1,
                h10=0.0,
                h100=0.0,
                lh=1.0,
                lw=0.0,
                dynamic=1,
                sav1=2000,
                savlh=1800,
                savlw=1600,
                depth=1.0,
                xmext=15,
                heatd=8000,
                heatl=8000,
            )

            # Shrub models
            standard_models[141] = FuelModel(
                number=141,
                code="SH1",
                h1=0.25,
                h10=0.25,
                h100=0.0,
                lh=0.15,
                lw=0.35,
                dynamic=1,
                sav1=2000,
                savlh=1800,
                savlw=1600,
                depth=1.0,
                xmext=15,
                heatd=8000,
                heatl=8000,
            )
            standard_models[142] = FuelModel(
                number=142,
                code="SH2",
                h1=0.25,
                h10=0.25,
                h100=0.0,
                lh=0.0,
                lw=0.75,
                dynamic=1,
                sav1=2000,
                savlh=1800,
                savlw=1600,
                depth=1.0,
                xmext=15,
                heatd=8000,
                heatl=8000,
            )

            # Timber models
            standard_models[161] = FuelModel(
                number=161,
                code="TU1",
                h1=0.2,
                h10=0.5,
                h100=0.5,
                lh=0.2,
                lw=0.0,
                dynamic=1,
                sav1=2000,
                savlh=1800,
                savlw=1600,
                depth=0.5,
                xmext=20,
                heatd=8000,
                heatl=8000,
            )
            standard_models[165] = FuelModel(
                number=165,
                code="TU5",
                h1=0.5,
                h10=0.5,
                h100=2.0,
                lh=0.0,
                lw=2.0,
                dynamic=0,
                sav1=1500,
                savlh=1800,
                savlw=1600,
                depth=1.0,
                xmext=25,
                heatd=8000,
                heatl=8000,
            )

            # Nonburnable
            standard_models[91] = FuelModel(
                number=91,
                code="NB1",
                h1=0.0,
                h10=0.0,
                h100=0.0,
                lh=0.0,
                lw=0.0,
                dynamic=0,
                sav1=1500,
                savlh=1800,
                savlw=1600,
                depth=0.0,
                xmext=25,
                heatd=8000,
                heatl=8000,
            )
        elif self.__class__.TEST_MODE:
            # Import the mock class for test mode
            # from tests.unit.test_laflammap_adapter import MockFuelModel

            # Create mock fuel models
            # Grass models
            standard_models[101] = self._create_mock_fuel_model(101, "GR1")
            standard_models[102] = self._create_mock_fuel_model(102, "GR2")

            # Shrub models
            standard_models[141] = self._create_mock_fuel_model(141, "SH1")
            standard_models[142] = self._create_mock_fuel_model(142, "SH2")

            # Timber models
            standard_models[161] = self._create_mock_fuel_model(161, "TU1")
            standard_models[165] = self._create_mock_fuel_model(165, "TU5")

            # Nonburnable
            standard_models[91] = self._create_mock_fuel_model(91, "NB1")
        else:
            # Mock fuel models for testing
            for model_id in [91, 101, 102, 141, 142, 161, 165]:
                standard_models[model_id] = {"number": model_id}

        # Create fuel model list
        fuel_models = []

        for model_id in unique_ids:
            if model_id in standard_models:
                fuel_models.append(standard_models[model_id])
            else:
                # Create a default model for unknown IDs
                logging.warning(f"Unknown fuel model ID: {model_id}, using default model")
                if LAFLAMMAP_AVAILABLE:
                    from laflammap.core.data_structures import FuelModel

                    default_model = FuelModel(
                        number=int(model_id),
                        code=f"FM{int(model_id)}",
                        h1=0.5,
                        h10=0.25,
                        h100=0.0,
                        lh=0.0,
                        lw=0.0,
                        dynamic=0,
                        sav1=1500,
                        savlh=1800,
                        savlw=1600,
                        depth=0.5,
                        xmext=20,
                        heatd=8000,
                        heatl=8000,
                    )
                elif self.__class__.TEST_MODE:
                    default_model = self._create_mock_fuel_model(
                        int(model_id), f"FM{int(model_id)}"
                    )
                else:
                    # Mock fuel model for testing
                    default_model = {"number": int(model_id)}
                fuel_models.append(default_model)

        # Cache for reuse
        self._fuel_models_cache = fuel_models

        return fuel_models

    def _create_mock_fuel_model(self, number, code):
        """Create a mock fuel model for testing.

        Args:
            number: Fuel model number
            code: Fuel model code

        Returns:
            Mock fuel model
        """

        # from tests.unit.test_laflammap_adapter import MockFuelModel
        # model = MockFuelModel()
        # Create a simple mock object instead
        class MockFuelModel:
            def __init__(self):
                self.number = 0
                self.code = ""
                self.h1 = 0.0
                self.h10 = 0.0
                self.h100 = 0.0
                self.lh = 0.0
                self.lw = 0.0
                self.dynamic = 0
                self.sav1 = 0.0
                self.savlh = 0.0
                self.savlw = 0.0
                self.depth = 0.0
                self.xmext = 0.0
                self.heatd = 0.0
                self.heatl = 0.0

        model = MockFuelModel()
        model.number = number
        model.code = code
        model.h1 = 0.5
        model.h10 = 0.25
        model.h100 = 0.0
        model.lh = 0.0
        model.lw = 0.0
        model.dynamic = 0
        model.sav1 = 1500
        model.savlh = 1800
        model.savlw = 1600
        model.depth = 0.5
        model.xmext = 20
        model.heatd = 8000
        model.heatl = 8000
        return model

    def simulate_spread(
        self,
        state: StateRepresentation,
        ignition_points: List[Tuple[int, int]],
        burn_time_minutes: float = 1440.0,
    ) -> np.ndarray:
        """Simulate fire spread using LaflamMap.

        Args:
            state: Landscape state
            ignition_points: List of (row, col) ignition points
            burn_time_minutes: Simulation time in minutes

        Returns:
            2D array of burn times in minutes

        Raises:
            ValueError: If required state variables are missing
        """
        # Reset caches
        self._landscape_data_cache = None
        self._weather_data_cache = None
        self._fuel_models_cache = []

        # Create LaflamMap data structures
        landscape_data = self._create_landscape_data(state)
        weather_data = self._create_weather_data(state)
        fuel_models = self._create_fuel_models(state)

        if LAFLAMMAP_AVAILABLE:
            # Load data into simulator
            self.simulator.load_landscape(landscape_data)
            self.simulator.load_weather(weather_data)
            self.simulator.load_fuel_models(fuel_models)

            # Convert ignition points to tensor
            ignition_tensor = tf.convert_to_tensor(ignition_points, dtype=tf.int32)

            # Calculate number of time steps based on burn time
            time_steps = int(burn_time_minutes / self.temporal_resolution) + 1
            time_steps = min(time_steps, self.max_iterations)

            # Run simulation
            result = self.simulator.calculate_fire_spread(
                ignition_points=ignition_tensor, time_steps=time_steps
            )

            # Extract fire spread results
            fire_spread = result["fire_spread"].numpy()  # [time_steps, height, width]
            fire_intensity = result["fire_intensity"].numpy()
            flame_length = result["flame_length"].numpy()
        else:
            # Mock implementation for test mode
            grid_shape = state.grid_shape
            height, width = grid_shape
            time_steps = int(burn_time_minutes / self.temporal_resolution) + 1
            time_steps = min(time_steps, self.max_iterations)

            # Create mock fire spread results
            fire_spread = np.zeros((time_steps, height, width))
            fire_intensity = np.zeros((time_steps, height, width))
            flame_length = np.zeros((time_steps, height, width))

            # Initialize ignition points
            for row, col in ignition_points:
                if 0 <= row < height and 0 <= col < width:
                    fire_spread[0, row, col] = 1.0
                    fire_intensity[0, row, col] = 500.0
                    flame_length[0, row, col] = 1.5

            # Simple fire spread for testing - grow by 1 cell in each direction per time step
            for t in range(1, time_steps):
                # Copy previous time step
                fire_spread[t] = fire_spread[t - 1].copy()
                fire_intensity[t] = fire_intensity[t - 1].copy()
                flame_length[t] = flame_length[t - 1].copy()

                # Expand the fire by one cell in each direction
                for r in range(height):
                    for c in range(width):
                        if fire_spread[t - 1, r, c] > 0:
                            for dr in [-1, 0, 1]:
                                for dc in [-1, 0, 1]:
                                    nr, nc = r + dr, c + dc
                                    if 0 <= nr < height and 0 <= nc < width:
                                        fire_spread[t, nr, nc] = 1.0
                                        fire_intensity[t, nr, nc] = 500.0
                                        flame_length[t, nr, nc] = 1.5

        # Calculate burn times
        # Convert from time steps to minutes and handle unburned cells
        burn_times = np.ones(state.grid_shape) * np.inf

        # For each time step, find newly burned cells and record the time
        for t in range(time_steps):
            burn_mask = fire_spread[t] > 0
            # Only update cells that haven't burned yet
            unburned_mask = np.isinf(burn_times)
            new_burns = burn_mask & unburned_mask
            burn_times[new_burns] = t * self.temporal_resolution

        # Store fire intensity and flame length in state for later use
        final_intensity = fire_intensity[-1]  # Use final time step
        final_flame = flame_length[-1]

        state.set_variable("fire_intensity", final_intensity)
        state.set_variable("flame_length", final_flame)

        # Calculate and store burn severity
        burn_severity = np.zeros_like(burn_times)
        burned_mask = ~np.isinf(burn_times)

        # Simple severity classification based on flame length
        # Low severity: < 1.2m, Moderate: 1.2-2.4m, High: >2.4m
        severity_low = (final_flame < 1.2) & burned_mask
        severity_moderate = (final_flame >= 1.2) & (final_flame < 2.4) & burned_mask
        severity_high = (final_flame >= 2.4) & burned_mask

        burn_severity[severity_low] = 1
        burn_severity[severity_moderate] = 2
        burn_severity[severity_high] = 3

        state.set_variable("burn_severity", burn_severity)

        return burn_times

    def calculate_fire_effects(self, state: StateRepresentation, burn_times: np.ndarray) -> None:
        """Calculate fire effects based on burn times and severity.

        Args:
            state: Landscape state to update with fire effects
            burn_times: 2D array of burn times in minutes
        """
        # Skip if burn severity is already calculated
        if "burn_severity" not in state.state_variables:
            logging.warning("Burn severity not found in state. Fire effects not calculated.")
            return

        burn_severity = state.get_variable("burn_severity")

        # Calculate mortality based on burn severity and vegetation type
        if "eco_state" in state.state_variables:
            veg_type = state.get_variable("eco_state")

            # Initialize mortality array
            mortality = np.zeros_like(burn_times, dtype=np.float32)

            # Apply mortality based on vegetation type and burn severity
            # Simplified model - would be more complex in real implementation
            # Low severity (1)
            mortality[(burn_severity == 1) & (veg_type == 1)] = 0.2  # Grass - low mortality
            mortality[(burn_severity == 1) & (veg_type == 2)] = 0.3  # Shrub - moderate mortality
            mortality[(burn_severity == 1) & (veg_type == 3)] = 0.1  # Forest - low mortality

            # Moderate severity (2)
            mortality[(burn_severity == 2) & (veg_type == 1)] = 0.7  # Grass - high mortality
            mortality[(burn_severity == 2) & (veg_type == 2)] = 0.5  # Shrub - moderate mortality
            mortality[(burn_severity == 2) & (veg_type == 3)] = 0.3  # Forest - moderate mortality

            # High severity (3)
            mortality[(burn_severity == 3) & (veg_type == 1)] = 0.9  # Grass - very high mortality
            mortality[(burn_severity == 3) & (veg_type == 2)] = 0.8  # Shrub - high mortality
            mortality[(burn_severity == 3) & (veg_type == 3)] = 0.6  # Forest - high mortality

            # Store mortality in state
            state.set_variable("fire_mortality", mortality)

        # Calculate soil effects
        soil_heating = np.zeros_like(burn_times, dtype=np.float32)

        # Simple model based on burn severity
        soil_heating[burn_severity == 1] = 100  # Low soil heating (°C)
        soil_heating[burn_severity == 2] = 300  # Moderate soil heating (°C)
        soil_heating[burn_severity == 3] = 600  # High soil heating (°C)

        state.set_variable("soil_heating", soil_heating)

        # Calculate emissions
        if "fuel_loading" in state.state_variables:
            fuel_loading = state.get_variable("fuel_loading")

            # Initialize emissions arrays
            co2_emissions = np.zeros_like(burn_times, dtype=np.float32)
            pm25_emissions = np.zeros_like(burn_times, dtype=np.float32)

            # Simple model: emissions ~ fuel loading * combustion factor * emission factor
            burned_mask = burn_severity > 0

            # CO2 emissions - tons/hectare
            co2_ef = 1.6  # Emission factor for CO2 (kg/kg)
            co2_emissions[burned_mask] = (
                fuel_loading[burned_mask] * co2_ef * burn_severity[burned_mask] / 3.0
            )

            # PM2.5 emissions - kg/hectare
            pm25_ef = 0.01  # Emission factor for PM2.5 (kg/kg)
            pm25_emissions[burned_mask] = (
                fuel_loading[burned_mask] * 1000 * pm25_ef * burn_severity[burned_mask] / 3.0
            )

            state.set_variable("co2_emissions", co2_emissions)
            state.set_variable("pm25_emissions", pm25_emissions)

    def reset_cache(self) -> None:
        """Reset data conversion caches."""
        self._landscape_data_cache = None
        self._weather_data_cache = None
        self._fuel_models_cache = []
