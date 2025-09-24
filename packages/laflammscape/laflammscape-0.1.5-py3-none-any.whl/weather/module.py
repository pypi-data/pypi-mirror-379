"""Weather & Fuel Moisture Module implementation.

Provides classes and functions for simulating weather conditions and
calculating fuel moistures with Nelson model support, topographic
corrections, and climate scenario integration.
"""

import json
import logging
import os
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple, Union

import numpy as np

from ..fire.behavior import WeatherCondition
from ..state.representation import StateRepresentation

# Setup logging
logger = logging.getLogger("laflammscape.weather")

# Try to import rasterio for NEX-GDDP-CMIP6 support
try:
    import rasterio
    from rasterio.windows import Window

    RASTERIO_AVAILABLE = True
except ImportError:
    RASTERIO_AVAILABLE = False
    logger.warning("rasterio not available - NEX-GDDP-CMIP6 data loading will be disabled")


@dataclass
class WeatherScenario:
    """Represents a weather scenario for simulation."""

    name: str
    daily_conditions: List[Dict[str, Any]]
    metadata: Dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "WeatherScenario":
        """Create a weather scenario from dictionary data.

        Args:
            data: Dictionary containing scenario data

        Returns:
            WeatherScenario instance
        """
        return cls(
            name=data["name"],
            daily_conditions=data["daily_conditions"],
            metadata=data.get("metadata", {}),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary representation.

        Returns:
            Dictionary representation of scenario
        """
        return {
            "name": self.name,
            "daily_conditions": self.daily_conditions,
            "metadata": self.metadata,
        }


@dataclass
class WeatherModule:
    """Simulates weather conditions and calculates fuel moistures.

    Features:
    - Nelson fuel moisture model
    - Topographic corrections
    - Climate scenario integration
    """

    # State variables
    temperature_var: str = "weather_temperature"
    humidity_var: str = "weather_humidity"
    wind_speed_var: str = "weather_wind_speed"
    wind_direction_var: str = "weather_wind_direction"
    precipitation_var: str = "precipitation"
    fuel_moisture_var: str = "fuel_moisture"

    # Topographic variables
    elevation_var: str = "elevation"
    slope_var: str = "slope"
    aspect_var: str = "aspect"

    # Weather scenarios
    scenarios: Dict[str, Union[WeatherScenario, "LazyNEXGDDPScenario"]] = field(
        default_factory=dict
    )
    current_scenario: Optional[str] = None

    # Simulation state
    _current_day: int = 0
    _current_period: int = 0  # For 8-hour increments (0-2 within a day)
    _use_8hour_periods: bool = False  # Toggle for 8-hour vs daily resolution
    _random_seed: Optional[int] = None
    rng: np.random.Generator = field(init=False)

    # Nelson model parameters
    nelson_params: Dict[str, Any] = field(
        default_factory=lambda: {
            "adsorption_rate": 0.05,
            "desorption_rate": 0.1,
            "timelag_1hr": 1.0,
            "timelag_10hr": 10.0,
            "timelag_100hr": 100.0,
        }
    )

    def __post_init__(self):
        """Initialize after dataclass creation."""
        # Initialize random number generator
        self.rng = np.random.default_rng(self._random_seed)

    def load_scenarios(self, scenarios_path: str) -> None:
        """Load weather scenarios from a JSON file.

        Args:
            scenarios_path: Path to scenarios file

        Raises:
            FileNotFoundError: If the file doesn't exist
        """
        if not os.path.exists(scenarios_path):
            raise FileNotFoundError(f"Scenarios file not found: {scenarios_path}")

        with open(scenarios_path, "r") as f:
            scenarios_data = json.load(f)

        # Clear existing scenarios
        self.scenarios.clear()

        # Process scenarios data
        if isinstance(scenarios_data, list):
            # List of scenarios
            for scenario_data in scenarios_data:
                try:
                    scenario = WeatherScenario.from_dict(scenario_data)
                    self.scenarios[scenario.name] = scenario
                except KeyError as e:
                    logger.warning(f"Missing required field in scenario: {e}")
        elif isinstance(scenarios_data, dict):
            # Handle case where scenarios are under a key
            if "scenarios" in scenarios_data:
                for scenario_data in scenarios_data["scenarios"]:
                    try:
                        scenario = WeatherScenario.from_dict(scenario_data)
                        self.scenarios[scenario.name] = scenario
                    except KeyError as e:
                        logger.warning(f"Missing required field in scenario: {e}")
            else:
                # Direct mapping of name -> scenario
                for name, scenario_data in scenarios_data.items():
                    try:
                        # Add name to scenario data if not present
                        if "name" not in scenario_data:
                            scenario_data["name"] = name
                        scenario = WeatherScenario.from_dict(scenario_data)
                        self.scenarios[scenario.name] = scenario
                    except KeyError as e:
                        logger.warning(f"Missing required field in scenario: {e}")

        logger.info(f"Loaded {len(self.scenarios)} weather scenarios")

    def set_random_seed(self, seed: int) -> None:
        """Set the random seed for weather simulation.

        Args:
            seed: Random seed to use
        """
        self._random_seed = seed
        self.rng = np.random.default_rng(seed)

    def generate_default_scenario(self, num_intervals: int = 30) -> WeatherScenario:
        """Generate a default weather scenario with realistic variations.

        Args:
            num_intervals: Number of intervals to generate

        Returns:
            Generated weather scenario
        """
        # Generate seasonal patterns
        days = np.arange(num_intervals)

        # Temperature: seasonal pattern with realistic daily variation
        # Base temperature varies from 40°F in winter to 90°F in summer
        seasonal_temp = 65.0 + 25.0 * np.sin(2 * np.pi * days / 365)  # Annual cycle
        # Daily temperature range: cooler at night, warmer during day
        daily_pattern = np.sin(2 * np.pi * days)  # Daily cycle
        daily_temp = 10.0 * daily_pattern + self.rng.normal(
            0, 3.0, num_intervals
        )  # Daily variation
        base_temps = seasonal_temp + daily_temp

        # Relative humidity: inverse relationship with temperature
        # Higher in early morning, lower in afternoon
        seasonal_rh = 70.0 - 30.0 * np.sin(2 * np.pi * days / 365)  # Annual cycle
        daily_rh_pattern = -np.sin(2 * np.pi * days)  # Inverse of temperature
        daily_rh = 15.0 * daily_rh_pattern + self.rng.normal(0, 5.0, num_intervals)
        base_rh = seasonal_rh + daily_rh

        # Wind: more realistic patterns
        # Higher during day, lower at night
        # Higher in spring/fall, lower in summer/winter
        seasonal_wind = 10.0 + 5.0 * np.sin(2 * np.pi * days / 365)  # Annual cycle
        daily_wind_pattern = np.sin(2 * np.pi * days)  # Daily cycle
        daily_wind = 5.0 * daily_wind_pattern + self.rng.normal(0, 2.0, num_intervals)
        base_wind = seasonal_wind + daily_wind

        # Wind direction: seasonal and daily patterns
        # Example: prevailing wind direction is westerly (270°) in summer, southerly (180°) in winter
        seasonal_dir = 225 + 45 * np.sin(2 * np.pi * days / 365)  # 225±45° annual cycle
        # Daily: small oscillation (e.g., 10° amplitude) for land/sea breeze effect
        daily_dir_pattern = np.sin(2 * np.pi * days)
        daily_dir = 10.0 * daily_dir_pattern
        # Add random noise (±15°)
        dir_noise = self.rng.normal(0, 15.0, num_intervals)
        base_wind_dir = (seasonal_dir + daily_dir + dir_noise) % 360

        # Generate daily conditions
        daily_conditions = []
        for i in range(num_intervals):
            # Add correlated variations
            # Temperature and humidity are inversely correlated
            temp_variation = self.rng.normal(0, 5.0)  # ±5°F
            rh_variation = -0.5 * temp_variation + self.rng.normal(0, 5.0)  # Correlated with temp

            # Wind variations are independent but bounded
            wind_variation = self.rng.normal(0, 5.0)  # ±5 mph

            # Calculate final values
            temp = base_temps[i] + temp_variation
            rh = base_rh[i] + rh_variation
            wind = base_wind[i] + wind_variation
            wind_dir = base_wind_dir[i]  # Use the generated wind direction

            # Realistic precipitation with seasonal patterns
            # Moderate probability during wet season (winter/spring)
            base_precip_prob = 0.08 + 0.12 * np.sin(
                2 * np.pi * (i + 90) / 365
            )  # Peak in winter/spring
            humidity_factor = (rh - 60.0) / 40.0  # Higher humidity = more likely to rain
            precip_prob = np.clip(base_precip_prob * (1.0 + humidity_factor * 0.5), 0.0, 0.3)

            precip = 0.0
            if self.rng.random() < precip_prob:
                # Create realistic precipitation events
                # 80% chance of light rain (0.05-0.3"), 15% moderate (0.3-0.8"), 5% heavy (0.8-2.0")
                rain_type = self.rng.random()
                if rain_type < 0.8:
                    # Light rain
                    precip = self.rng.uniform(0.05, 0.3)
                elif rain_type < 0.95:
                    # Moderate rain
                    precip = self.rng.uniform(0.3, 0.8)
                else:
                    # Heavy rain/storm
                    precip = self.rng.uniform(0.8, 2.0)

                # Apply modest seasonal and humidity modifiers
                seasonal_factor = 1.0 + 0.2 * np.sin(
                    2 * np.pi * (i + 90) / 365
                )  # Modest seasonal effect
                humidity_factor = 1.0 + max(0, (rh - 70.0) / 30.0) * 0.3  # Modest humidity effect
                precip *= seasonal_factor * humidity_factor

            # Calculate fuel moistures based on weather conditions
            # Base moistures vary with season and recent precipitation
            base_1hr = 6.0 + 4.0 * np.sin(
                2 * np.pi * (i + 90) / 365
            )  # Seasonal variation, drier in summer
            base_10hr = 8.0 + 3.0 * np.sin(2 * np.pi * (i + 90) / 365)
            base_100hr = 10.0 + 2.0 * np.sin(2 * np.pi * (i + 90) / 365)

            # Adjust for recent weather with stronger effects
            temp_factor = 1.0 - 0.02 * (temp - 65.0)  # Doubled temperature effect
            rh_factor = 1.0 + 0.03 * (rh - 50.0)  # Increased humidity effect

            # Moderate precipitation effects
            if precip > 0:
                # Precipitation has moderate effect on fuel moisture
                if precip < 0.3:
                    # Light rain: small increase
                    precip_factor = 1.0 + precip * 3.0  # Up to 1.9x increase
                elif precip < 0.8:
                    # Moderate rain: moderate increase
                    precip_factor = 1.0 + 0.9 + (precip - 0.3) * 4.0  # 1.9x to 3.9x increase
                else:
                    # Heavy rain: larger increase
                    precip_factor = 1.0 + 2.9 + (precip - 0.8) * 6.0  # 3.9x to 11.1x increase
            else:
                precip_factor = 1.0

            # Apply factors to base moistures
            base_1hr *= temp_factor * rh_factor * precip_factor
            base_10hr *= temp_factor * rh_factor * precip_factor
            base_100hr *= temp_factor * rh_factor * precip_factor

            # Live fuel moistures have strong seasonal patterns
            # Peak in spring, lowest in late summer/fall
            herb_moisture = 60.0 + 80.0 * np.sin(
                2 * np.pi * (i - 30) / 365
            )  # Peak in spring (140%), low in fall (20%)
            woody_moisture = 80.0 + 60.0 * np.sin(
                2 * np.pi * (i - 45) / 365
            )  # Peak slightly later (140%), low in fall (20%)

            # Live fuels are moderately responsive to precipitation
            if precip > 0:
                # Live fuels absorb water moderately
                live_precip_factor = 1.0 + precip * 5.0  # Moderate response
            else:
                live_precip_factor = 1.0

            # Adjust live moistures for recent weather
            herb_moisture *= rh_factor * live_precip_factor
            woody_moisture *= rh_factor * live_precip_factor

            # Create daily condition
            daily = {
                "temperature": float(temp),
                "relative_humidity": float(max(5.0, min(95.0, rh))),
                "wind_speed": float(max(0.0, min(50.0, wind))),  # Cap wind speed at 50 mph
                "wind_direction": float(wind_dir),  # Use the generated wind direction
                "precipitation": float(precip),
                "fuel_moistures": {
                    "1hr": float(max(2.0, min(30.0, base_1hr))),
                    "10hr": float(max(3.0, min(35.0, base_10hr))),
                    "100hr": float(max(5.0, min(40.0, base_100hr))),
                    "live_herbaceous": float(max(30.0, min(300.0, herb_moisture))),
                    "live_woody": float(max(60.0, min(200.0, woody_moisture))),
                },
            }
            daily_conditions.append(daily)

        # Create and return scenario
        return WeatherScenario(
            name="default",
            daily_conditions=daily_conditions,
            metadata={
                "description": "Generated default weather scenario with realistic seasonal patterns",
                "num_intervals": num_intervals,
                "generated_at": datetime.now().isoformat(),
                "base_temperature": float(np.mean(base_temps)),
                "base_humidity": float(np.mean(base_rh)),
                "base_wind": float(np.mean(base_wind)),
            },
        )

    def set_scenario(self, scenario_name: Optional[str] = None) -> None:
        """Set active weather scenario.

        Args:
            scenario_name: Name of scenario to use. If None, generates a default scenario.

        Raises:
            ValueError: If scenario doesn't exist and no default is generated
        """
        if scenario_name is None:
            # Generate and set default scenario
            default_scenario = self.generate_default_scenario()
            self.scenarios["default"] = default_scenario
            scenario_name = "default"
            logger.info("No scenario provided, using generated default scenario")

        if scenario_name not in self.scenarios:
            raise ValueError(f"Weather scenario not found: {scenario_name}")

        self.current_scenario = scenario_name
        self._current_day = 0

        # Store daily conditions for easier access in tests - only for traditional scenarios
        scenario = self.scenarios[scenario_name]
        if isinstance(scenario, WeatherScenario):
            if isinstance(scenario.daily_conditions, list) and len(scenario.daily_conditions) > 0:
                self.daily_conditions = scenario.daily_conditions[0]
            else:
                self.daily_conditions = scenario.daily_conditions
        elif isinstance(scenario, LazyNEXGDDPScenario):
            # For lazy scenarios, we don't pre-load daily conditions
            self.daily_conditions = None

        logger.info(f"Set active weather scenario to '{scenario_name}'")

    def set_8hour_mode(self, enabled: bool = True) -> None:
        """Enable or disable 8-hour period mode.

        Args:
            enabled: If True, weather will advance in 8-hour increments
        """
        self._use_8hour_periods = enabled
        self._current_period = 0
        logger.info(f"8-hour period mode {'enabled' if enabled else 'disabled'}")

    def advance_day(self) -> None:
        """Advance to the next simulation day or 8-hour period."""
        if self._use_8hour_periods:
            self._current_period += 1
            if self._current_period >= 3:  # 3 periods per day
                self._current_period = 0
                self._current_day += 1
            logger.debug(f"Advanced to day {self._current_day}, period {self._current_period}")
        else:
            self._current_day += 1
            logger.debug(f"Advanced to day {self._current_day}")

    def reset(self) -> None:
        """Reset weather simulation to day 0."""
        self._current_day = 0
        self._current_period = 0
        logger.debug("Reset weather simulation to day 0, period 0")

    def add_scenario(self, scenario: WeatherScenario) -> None:
        """Add a new weather scenario.

        Args:
            scenario: Weather scenario to add

        Raises:
            ValueError: If a scenario with the same name already exists
        """
        if scenario.name in self.scenarios:
            raise ValueError(f"Scenario '{scenario.name}' already exists")

        self.scenarios[scenario.name] = scenario
        logger.info(f"Added weather scenario '{scenario.name}'")

    def create_scenario_from_data(
        self,
        name: str,
        daily_data: List[Dict[str, Any]],
        metadata: Optional[Dict[str, Any]] = None,
    ) -> None:
        """Create and add a new weather scenario from daily data.

        Args:
            name: Name of the scenario
            daily_data: List of daily weather conditions
            metadata: Optional metadata for the scenario

        Raises:
            ValueError: If a scenario with the same name already exists
        """
        if name in self.scenarios:
            raise ValueError(f"Scenario '{name}' already exists")

        scenario = WeatherScenario(name=name, daily_conditions=daily_data, metadata=metadata or {})

        self.scenarios[name] = scenario
        logger.info(f"Created weather scenario '{name}' with {len(daily_data)} days")

    def get_current_weather(self) -> WeatherCondition:
        """Get weather conditions for the current day or 8-hour period.

        Returns:
            Weather conditions for the current time step

        Raises:
            ValueError: If no scenario is active or current day is out of range
        """
        if self.current_scenario is None:
            self.scenarios["default"] = self.generate_default_scenario(num_intervals=1000)
            self.current_scenario = "default"
            print("No current scenario. Using default scenario")

        scenario = self.scenarios[self.current_scenario]

        # Handle lazy NEX-GDDP scenarios
        if isinstance(scenario, LazyNEXGDDPScenario):
            try:
                if self._use_8hour_periods:
                    # Calculate global 8-hour period index
                    period_index = self._current_day * 3 + self._current_period
                    daily = scenario.get_8hour_weather(period_index)
                else:
                    daily = scenario.get_daily_weather(self._current_day)
            except (ValueError, IndexError):
                # If current day exceeds scenario, wrap around
                if self._use_8hour_periods:
                    total_periods = scenario.get_day_count() * 3
                    if total_periods > 0:
                        period_index = (
                            self._current_day * 3 + self._current_period
                        ) % total_periods
                        daily = scenario.get_8hour_weather(period_index)
                    else:
                        raise ValueError("No weather data available in lazy scenario")
                else:
                    total_days = scenario.get_day_count()
                    if total_days > 0:
                        day_index = self._current_day % total_days
                        daily = scenario.get_daily_weather(day_index)
                    else:
                        raise ValueError("No weather data available in lazy scenario")

        # Handle traditional scenarios
        elif hasattr(scenario, "daily_conditions"):
            # Traditional scenarios don't support 8-hour periods yet
            if self._use_8hour_periods:
                logger.warning(
                    "8-hour periods not supported for traditional scenarios, using daily data"
                )

            # Handle different formats of daily_conditions
            if isinstance(scenario.daily_conditions, list):
                # Handle case when current day exceeds scenario length
                day_index = self._current_day % len(scenario.daily_conditions)
                # Get daily conditions
                daily = scenario.daily_conditions[day_index]
            else:
                # Handle case where daily_conditions is a dictionary
                daily = scenario.daily_conditions
        else:
            raise ValueError(f"Unknown scenario type: {type(scenario)}")

        # Add some randomness to conditions
        temp = daily.get("temperature", 70.0)
        temp_variation = self.rng.normal(0, 3.0)  # +/- 3 degrees

        rh = daily.get("relative_humidity", 40.0)
        rh_variation = self.rng.normal(0, 5.0)  # +/- 5%
        rh = max(5.0, min(95.0, rh + rh_variation))  # Keep in realistic range

        wind_speed = daily.get("wind_speed", 5.0)
        wind_variation = self.rng.normal(0, 1.0)  # +/- 1 mph
        wind_speed = max(0.0, wind_speed + wind_variation)

        wind_dir = daily.get("wind_direction", 0.0)
        dir_variation = self.rng.normal(0, 15.0)  # +/- 15 degrees
        wind_dir = (wind_dir + dir_variation) % 360.0

        precip = daily.get("precipitation", 0.0)

        # Get fuel moistures or calculate defaults
        fuel_moistures = daily.get("fuel_moistures", {})

        # Create weather condition
        weather = WeatherCondition(
            temperature=temp + temp_variation,
            relative_humidity=rh,
            wind_speed=wind_speed,
            wind_direction=wind_dir,
            precipitation=precip,
            fuel_moistures=fuel_moistures,
        )

        return weather

    def apply_to_state(self, state: StateRepresentation) -> None:
        """Apply weather conditions to the landscape state.

        Args:
            state: State to modify

        Raises:
            ValueError: If no scenario is active
        """
        # Get current weather conditions
        weather = self.get_current_weather()

        # Get landscape dimensions from any existing state variable
        shape = next(iter(state.state_variables.values())).shape

        # Initialize weather variable arrays if they don't exist
        self._initialize_weather_vars(state, shape)

        # Get topographic variables if available
        elevation = self._get_topo_var(state, self.elevation_var)
        slope = self._get_topo_var(state, self.slope_var)
        aspect = self._get_topo_var(state, self.aspect_var)

        # Apply base weather conditions with topographic corrections
        self._apply_temperature(state, weather.temperature, elevation, aspect)
        self._apply_humidity(state, weather.relative_humidity, elevation, aspect)
        self._apply_wind(
            state,
            weather.wind_speed,
            weather.wind_direction,
            elevation,
            slope,
            aspect,
        )
        self._apply_precipitation(state, weather.precipitation, elevation)

        # Calculate fuel moistures
        self._calculate_fuel_moistures(state, weather.fuel_moistures)

        # Advance to next day for next application
        self.advance_day()

        logger.info(
            f"Applied weather conditions for day {self._current_day - 1}, advanced to day {self._current_day}"
        )

    def _initialize_weather_vars(self, state: StateRepresentation, shape: Tuple[int, int]) -> None:
        """Initialize weather variables in state if they don't exist.

        Args:
            state: State to modify
            shape: Shape for variable arrays
        """
        # Temperature
        if self.temperature_var not in state.state_variables:
            state.set_variable(self.temperature_var, np.zeros(shape, dtype=np.float32))

        # Humidity
        if self.humidity_var not in state.state_variables:
            state.set_variable(self.humidity_var, np.zeros(shape, dtype=np.float32))

        # Wind speed
        if self.wind_speed_var not in state.state_variables:
            state.set_variable(self.wind_speed_var, np.zeros(shape, dtype=np.float32))

        # Wind direction
        if self.wind_direction_var not in state.state_variables:
            state.set_variable(self.wind_direction_var, np.zeros(shape, dtype=np.float32))

        # Precipitation
        if self.precipitation_var not in state.state_variables:
            state.set_variable(self.precipitation_var, np.zeros(shape, dtype=np.float32))

        # Fuel moisture (multi-channel)
        if self.fuel_moisture_var not in state.state_variables:
            # Initialize with 5 channels: 1hr, 10hr, 100hr, live_herb, live_woody
            moisture_shape = shape + (5,)
            state.set_variable(
                self.fuel_moisture_var,
                np.zeros(moisture_shape, dtype=np.float32),
            )

    def _get_topo_var(self, state: StateRepresentation, var_name: str) -> Optional[np.ndarray]:
        """Get topographic variable if it exists.

        Args:
            state: Current state
            var_name: Name of topographic variable

        Returns:
            Variable array or None if not present
        """
        if var_name in state.state_variables:
            return state.get_variable(var_name)
        return None

    def _apply_temperature(
        self,
        state: StateRepresentation,
        temperature: float,
        elevation: Optional[np.ndarray],
        aspect: Optional[np.ndarray],
    ) -> None:
        """Apply temperature adjustments based on elevation and aspect.

        Args:
            state: State to update
            temperature: Base temperature
            elevation: Elevation array
            aspect: Aspect array
        """
        # Convert base temperature to array
        temp_grid = np.full(state.grid_shape, temperature)

        # Apply elevation adjustment (-6.5°C per 1000m)
        if elevation is not None:
            elevation_adjustment = (elevation / 1000.0) * -6.5
            temp_grid += elevation_adjustment

        # Apply aspect adjustment (south-facing slopes are warmer)
        # Convert aspect to radians and calculate southness
        if aspect is not None:
            aspect_radians = np.deg2rad(aspect - 180)
            southness = np.cos(aspect_radians)
            aspect_adjustment = southness * 2.0  # Up to 2°C warmer on south-facing slopes
            temp_grid += aspect_adjustment

        # Store adjusted temperature
        state.set_variable(self.temperature_var, temp_grid)

    def _apply_humidity(
        self,
        state: StateRepresentation,
        base_rh: float,
        elevation: Optional[np.ndarray] = None,
        aspect: Optional[np.ndarray] = None,
    ) -> None:
        """Apply relative humidity to landscape with topographic corrections.

        Args:
            state: State to modify
            base_rh: Base relative humidity (%)
            elevation: Elevation array (meters)
            aspect: Aspect array (degrees)
        """
        rh_grid = state.get_variable(self.humidity_var)

        # Start with base humidity
        rh_grid = np.full(rh_grid.shape, base_rh)

        # Apply elevation correction if available
        if elevation is not None:
            # Calculate reference elevation (mean)
            ref_elevation = np.mean(elevation)

            # RH often increases with elevation
            elevation_diff_m = elevation - ref_elevation
            rh_adjustment = 1.0 * (elevation_diff_m / 100.0)  # 1% per 100m
            rh_grid += rh_adjustment

        # Apply aspect correction if available
        if aspect is not None:
            # South-facing slopes are drier
            aspect_radians = np.deg2rad(aspect - 180)
            southness = np.cos(aspect_radians)
            rh_grid -= 10.0 * southness  # Up to 10% drier on south slopes

        # Ensure RH is within valid range (0-100%)
        rh_grid = np.clip(rh_grid, 0.0, 100.0)

        # Update state
        state.set_variable(self.humidity_var, rh_grid)

    def _apply_wind(
        self,
        state: StateRepresentation,
        base_speed: float,
        base_direction: float,
        elevation: Optional[np.ndarray] = None,
        slope: Optional[np.ndarray] = None,
        aspect: Optional[np.ndarray] = None,
    ) -> None:
        """Apply wind to landscape with topographic corrections.

        Args:
            state: State to modify
            base_speed: Base wind speed (mph)
            base_direction: Base wind direction (degrees)
            elevation: Elevation array (meters)
            slope: Slope array (degrees)
            aspect: Aspect array (degrees)
        """
        speed_grid = state.get_variable(self.wind_speed_var)
        direction_grid = state.get_variable(self.wind_direction_var)

        # Start with base values
        speed_grid = np.full(speed_grid.shape, base_speed)
        direction_grid = np.full(direction_grid.shape, base_direction)

        # Apply topographic corrections if slope and aspect are available
        if slope is not None and aspect is not None:
            # Wind speed tends to be higher on exposed ridges and lower in valleys
            # This is a simplified model - real wind models are much more complex

            # Calculate exposure index
            exposure = np.zeros_like(slope)

            # Calculate direction difference (wind direction vs. aspect)
            dir_diff = np.abs(base_direction - aspect)
            dir_diff = np.minimum(dir_diff, 360 - dir_diff)
            dir_diff_radians = np.deg2rad(dir_diff)

            # Upwind slopes (facing the wind) have reduced speed
            # Downwind slopes (facing away from wind) have increased speed
            wind_exposure = np.cos(dir_diff_radians)

            # Steeper slopes have stronger effect
            slope_radians = np.deg2rad(slope)
            slope_factor = np.sin(slope_radians)

            # Combine to get final exposure factor
            exposure = wind_exposure * slope_factor

            # Apply to wind speed (range: 0.7x to 1.3x)
            speed_grid *= 1.0 + 0.3 * exposure

            # Also adjust direction slightly on steep slopes
            # Wind tends to flow around obstacles and follow terrain
            steep_mask = slope > 15.0  # Only adjust on steep slopes
            if np.any(steep_mask):
                # Blend between base direction and aspect
                # Steeper slopes cause wind to follow terrain more
                blend_factor = np.clip(slope / 45.0, 0.0, 0.5)  # 0-0.5

                # Find all steep indices
                steep_indices = np.where(steep_mask)  # shape [N, 2]
                aspect_vals = aspect[steep_indices]
                blend_factors = blend_factor[steep_indices]

                # Compute base and aspect radians
                base_rad = np.deg2rad(base_direction)
                aspect_rad = np.deg2rad(aspect_vals)

                # Compute blended vectors and angles
                base_x = np.cos(base_rad)
                base_y = np.sin(base_rad)
                aspect_x = np.cos(aspect_rad)
                aspect_y = np.sin(aspect_rad)
                result_x = base_x * (1 - blend_factors) + aspect_x * blend_factors
                result_y = base_y * (1 - blend_factors) + aspect_y * blend_factors
                result_rad = np.arctan2(result_y, result_x)
                result_deg = np.rad2deg(result_rad) % 360

                # Batch update
                direction_grid = np.array(direction_grid)
                direction_grid[steep_indices] = result_deg

        # Ensure wind speed is non-negative
        speed_grid = np.maximum(speed_grid, 0.0)

        # Update state
        state.set_variable(self.wind_speed_var, speed_grid)
        state.set_variable(self.wind_direction_var, direction_grid)

    def _apply_precipitation(
        self,
        state: StateRepresentation,
        base_precip: float,
        elevation: Optional[np.ndarray] = None,
    ) -> None:
        """Apply precipitation to landscape with topographic corrections.

        Args:
            state: State to modify
            base_precip: Base precipitation (inches)
            elevation: Elevation array (meters)
        """
        precip_grid = state.get_variable(self.precipitation_var)

        # Start with base precipitation
        precip_grid = np.full(precip_grid.shape, base_precip)

        # Apply elevation correction if available
        if elevation is not None and base_precip > 0:
            # Calculate reference elevation (mean)
            ref_elevation = np.mean(elevation)

            # Precipitation often increases with elevation (orographic effect)
            elevation_diff_m = elevation - ref_elevation

            # Increase precipitation by up to 50% on higher elevations
            precip_factor = 1.0 + np.clip(elevation_diff_m / 1000.0, -0.25, 0.5)
            precip_grid *= precip_factor

        # Ensure precipitation is non-negative
        precip_grid = np.maximum(precip_grid, 0.0)

        # Update state
        state.set_variable(self.precipitation_var, precip_grid)

    def _calculate_fuel_moistures(
        self, state: StateRepresentation, base_moistures: Dict[str, float]
    ) -> None:
        """Calculate fuel moistures using the Nelson model.

        Args:
            state: State to modify
            base_moistures: Base moisture values for each fuel class
        """
        # Get temperature, humidity, and precipitation grids
        temp_grid = state.get_variable(self.temperature_var)
        rh_grid = state.get_variable(self.humidity_var)
        precip_grid = state.get_variable(self.precipitation_var)

        # Get fuel moisture grid
        moisture_grid = state.get_variable(self.fuel_moisture_var)

        # Get previous day's values (if this is not the first day)
        if self._current_day > 0:
            prev_moisture = moisture_grid
        else:
            # Initialize with realistic base values for first day
            prev_moisture = np.zeros_like(moisture_grid)
            # Set realistic initial moisture values
            prev_moisture[..., 0] = base_moistures.get("1hr", 6.0)  # 1hr fuels: 6%
            prev_moisture[..., 1] = base_moistures.get("10hr", 8.0)  # 10hr fuels: 8%
            prev_moisture[..., 2] = base_moistures.get("100hr", 10.0)  # 100hr fuels: 10%
            prev_moisture[..., 3] = base_moistures.get("live_herbaceous", 60.0)  # Live herb: 60%
            prev_moisture[..., 4] = base_moistures.get("live_woody", 90.0)  # Live woody: 90%

        # Calculate equilibrium moisture content (EMC)
        emc_grid = self.calculate_emc(temp_grid, rh_grid)

        # Apply Nelson model for each timelag class
        # 1-hour fuels
        moisture_1hr = self.apply_nelson_model(
            prev_moisture[..., 0],
            emc_grid,
            precip_grid,
            self.nelson_params["timelag_1hr"],
            self.nelson_params["adsorption_rate"],
            self.nelson_params["desorption_rate"],
        )
        # 10-hour fuels
        moisture_10hr = self.apply_nelson_model(
            prev_moisture[..., 1],
            emc_grid,
            precip_grid,
            self.nelson_params["timelag_10hr"],
            self.nelson_params["adsorption_rate"],
            self.nelson_params["desorption_rate"],
        )
        # 100-hour fuels
        moisture_100hr = self.apply_nelson_model(
            prev_moisture[..., 2],
            emc_grid,
            precip_grid,
            self.nelson_params["timelag_100hr"],
            self.nelson_params["adsorption_rate"],
            self.nelson_params["desorption_rate"],
        )
        # Live herbaceous fuels - extremely responsive to precipitation
        live_herb = np.full(
            moisture_grid[..., 3].shape,
            base_moistures.get("live_herbaceous", 60.0),
        )
        # Enhanced precipitation response for live fuels
        herb_rain_effect = np.zeros_like(precip_grid)
        light_rain_mask = (precip_grid > 0) & (precip_grid <= 0.5)
        moderate_rain_mask = (precip_grid > 0.5) & (precip_grid <= 1.5)
        heavy_rain_mask = precip_grid > 1.5

        herb_rain_effect[light_rain_mask] = precip_grid[light_rain_mask] * 30.0  # 30% per inch
        herb_rain_effect[moderate_rain_mask] = (
            15.0 + (precip_grid[moderate_rain_mask] - 0.5) * 50.0
        )  # 15% + 50% per additional inch
        herb_rain_effect[heavy_rain_mask] = (
            65.0 + (precip_grid[heavy_rain_mask] - 1.5) * 80.0
        )  # 65% + 80% per additional inch

        live_herb += herb_rain_effect

        # Live woody fuels - also very responsive but less than herbaceous
        live_woody = np.full(moisture_grid[..., 4].shape, base_moistures.get("live_woody", 90.0))
        woody_rain_effect = np.zeros_like(precip_grid)

        woody_rain_effect[light_rain_mask] = precip_grid[light_rain_mask] * 20.0  # 20% per inch
        woody_rain_effect[moderate_rain_mask] = (
            10.0 + (precip_grid[moderate_rain_mask] - 0.5) * 35.0
        )  # 10% + 35% per additional inch
        woody_rain_effect[heavy_rain_mask] = (
            45.0 + (precip_grid[heavy_rain_mask] - 1.5) * 60.0
        )  # 45% + 60% per additional inch

        live_woody += woody_rain_effect

        # Stack all channels into a single [H, W, 5] array
        new_moisture_grid = np.stack(
            [
                moisture_1hr,
                moisture_10hr,
                moisture_100hr,
                live_herb,
                live_woody,
            ],
            axis=-1,
        )

        # Ensure all moisture values are within realistic ranges
        new_moisture_grid = np.clip(new_moisture_grid, 0.0, 300.0)

        # Update state
        state.set_variable(self.fuel_moisture_var, new_moisture_grid)

    def get_weather_condition_at_point(
        self, state: StateRepresentation, row: int, col: int
    ) -> WeatherCondition:
        """Get weather condition at a specific point in the landscape.

        Args:
            state: Current landscape state
            row: Row index
            col: Column index

        Returns:
            Weather condition at that point

        Raises:
            ValueError: If required state variables don't exist
        """
        # Check required variables
        required_vars = [
            self.temperature_var,
            self.humidity_var,
            self.wind_speed_var,
            self.wind_direction_var,
            self.precipitation_var,
            self.fuel_moisture_var,
        ]

        for var in required_vars:
            if var not in state.state_variables:
                raise ValueError(f"Required variable not found: {var}")

        # Get weather values at point
        temp = state.get_variable(self.temperature_var)[row, col]
        rh = state.get_variable(self.humidity_var)[row, col]
        wind_speed = state.get_variable(self.wind_speed_var)[row, col]
        wind_dir = state.get_variable(self.wind_direction_var)[row, col]
        precip = state.get_variable(self.precipitation_var)[row, col]

        # Get fuel moistures at point
        moisture_grid = state.get_variable(self.fuel_moisture_var)
        fuel_moistures = {
            "1hr": moisture_grid[row, col, 0],
            "10hr": moisture_grid[row, col, 1],
            "100hr": moisture_grid[row, col, 2],
            "live_herbaceous": moisture_grid[row, col, 3],
            "live_woody": moisture_grid[row, col, 4],
        }

        # Create and return weather condition
        return WeatherCondition(
            temperature=temp,
            relative_humidity=rh,
            wind_speed=wind_speed,
            wind_direction=wind_dir,
            precipitation=precip,
            fuel_moistures=fuel_moistures,
        )

    def export_scenario(self, scenario_name: str, output_path: str) -> None:
        """Export a weather scenario to a JSON file.

        Args:
            scenario_name: Name of scenario to export
            output_path: Path to write scenario to

        Raises:
            ValueError: If scenario doesn't exist
        """
        if scenario_name not in self.scenarios:
            raise ValueError(f"Weather scenario not found: {scenario_name}")

        scenario = self.scenarios[scenario_name]

        # Only traditional WeatherScenario objects can be exported to JSON
        if isinstance(scenario, WeatherScenario):
            # Convert to dictionary
            scenario_dict = scenario.to_dict()

            # Write to file
            with open(output_path, "w") as f:
                json.dump(scenario_dict, f, indent=2)

            logger.info(f"Exported weather scenario '{scenario_name}' to {output_path}")
        elif isinstance(scenario, LazyNEXGDDPScenario):
            raise ValueError(
                f"Cannot export lazy scenario '{scenario_name}' - lazy scenarios cannot be exported to JSON"
            )
        else:
            raise ValueError(f"Unknown scenario type for '{scenario_name}': {type(scenario)}")

    def summarize_weather(self, state: StateRepresentation) -> Dict[str, Any]:
        """Summarize current weather conditions on the landscape.

        Args:
            state: Current landscape state

        Returns:
            Dictionary with summary statistics

        Raises:
            ValueError: If required variables don't exist
        """
        # Check required variables
        required_vars = [
            self.temperature_var,
            self.humidity_var,
            self.wind_speed_var,
            self.wind_direction_var,
            self.precipitation_var,
            self.fuel_moisture_var,
        ]

        for var in required_vars:
            if var not in state.state_variables:
                raise ValueError(f"Required variable not found: {var}")

        # Get data
        temp = state.get_variable(self.temperature_var)
        rh = state.get_variable(self.humidity_var)
        wind_speed = state.get_variable(self.wind_speed_var)
        wind_dir = state.get_variable(self.wind_direction_var)
        precip = state.get_variable(self.precipitation_var)
        moisture = state.get_variable(self.fuel_moisture_var)

        # Calculate statistics
        summary = {
            "day": self._current_day,
            "scenario": self.current_scenario,
            "temperature": {
                "mean": float(np.mean(temp)),
                "min": float(np.min(temp)),
                "max": float(np.max(temp)),
            },
            "relative_humidity": {
                "mean": float(np.mean(rh)),
                "min": float(np.min(rh)),
                "max": float(np.max(rh)),
            },
            "wind_speed": {
                "mean": float(np.mean(wind_speed)),
                "min": float(np.min(wind_speed)),
                "max": float(np.max(wind_speed)),
            },
            "wind_direction": {
                "mean": float(np.mean(wind_dir)),
                "min": float(np.min(wind_dir)),
                "max": float(np.max(wind_dir)),
            },
            "precipitation": {
                "mean": float(np.mean(precip)),
                "max": float(np.max(precip)),
            },
            "fuel_moisture": {
                "1hr": {
                    "mean": float(np.mean(moisture[..., 0])),
                    "min": float(np.min(moisture[..., 0])),
                    "max": float(np.max(moisture[..., 0])),
                },
                "10hr": {
                    "mean": float(np.mean(moisture[..., 1])),
                    "min": float(np.min(moisture[..., 1])),
                    "max": float(np.max(moisture[..., 1])),
                },
                "100hr": {
                    "mean": float(np.mean(moisture[..., 2])),
                    "min": float(np.min(moisture[..., 2])),
                    "max": float(np.max(moisture[..., 2])),
                },
                "live_herbaceous": {
                    "mean": float(np.mean(moisture[..., 3])),
                    "min": float(np.min(moisture[..., 3])),
                    "max": float(np.max(moisture[..., 3])),
                },
                "live_woody": {
                    "mean": float(np.mean(moisture[..., 4])),
                    "min": float(np.min(moisture[..., 4])),
                    "max": float(np.max(moisture[..., 4])),
                },
            },
        }

        return summary

    def calculate_emc(self, temperature: np.ndarray, relative_humidity: np.ndarray) -> np.ndarray:
        """Calculate equilibrium moisture content (EMC) using Simard equation (NumPy version)."""
        rh = np.clip(relative_humidity, 0.1, 100.0) / 100.0
        W = (
            0.18
            * (21.1 - 0.39 * temperature + 0.0183 * np.square(temperature))
            * (1.0 - np.exp(-0.115 * rh * 100))
        )
        E = 0.0056 * (100 - temperature)
        emc = np.where(rh >= 0.5, W + E * (rh * 100 - 50), W)
        return np.clip(emc, 0.0, 35.0)

    def apply_nelson_model(
        self,
        prev_moisture: np.ndarray,
        emc: np.ndarray,
        precipitation: np.ndarray,
        timelag: float,
        adsorption_rate: float,
        desorption_rate: float,
    ) -> np.ndarray:
        """Apply Nelson moisture model for a specific timelag class with enhanced precipitation effects."""
        k = 1.0 - np.exp(-24.0 / timelag)
        k_adsorption = k * adsorption_rate
        k_desorption = k * desorption_rate
        wetting_mask = prev_moisture < emc
        wetting_result = prev_moisture + k_adsorption * (emc - prev_moisture)
        drying_result = prev_moisture + k_desorption * (emc - prev_moisture)
        new_moisture = np.where(wetting_mask, wetting_result, drying_result)

        # Enhanced precipitation effects based on intensity
        rain_effect = np.zeros_like(precipitation)
        light_rain_mask = (precipitation > 0) & (precipitation <= 0.5)
        moderate_rain_mask = (precipitation > 0.5) & (precipitation <= 1.5)
        heavy_rain_mask = precipitation > 1.5

        # Light rain: moderate effect
        rain_effect[light_rain_mask] = 10.0 * (1.0 - np.exp(-precipitation[light_rain_mask] * 2.0))

        # Moderate rain: strong effect
        rain_effect[moderate_rain_mask] = 20.0 * (
            1.0 - np.exp(-precipitation[moderate_rain_mask] * 1.5)
        )

        # Heavy rain: extreme effect
        rain_effect[heavy_rain_mask] = 40.0 * (1.0 - np.exp(-precipitation[heavy_rain_mask] * 1.0))

        new_moisture += rain_effect
        return new_moisture

    def generate_dry_scenario(self, num_intervals: int = 30) -> WeatherScenario:
        """Generate a dry weather scenario conducive to fire spread.

        Args:
            num_intervals: Number of intervals to generate

        Returns:
            Generated dry weather scenario
        """
        # Generate seasonal patterns
        days = np.arange(num_intervals)

        # Temperature: higher base temperatures, more extreme summer heat
        # Base temperature varies from 50°F in winter to 105°F in summer
        seasonal_temp = 75.0 + 30.0 * np.sin(2 * np.pi * days / 365)  # Annual cycle (45-105°F)
        # Daily temperature range: cooler at night, warmer during day
        daily_pattern = np.sin(2 * np.pi * days)  # Daily cycle
        daily_temp = 12.0 * daily_pattern + self.rng.normal(
            0, 4.0, num_intervals
        )  # Daily variation
        base_temps = seasonal_temp + daily_temp

        # Relative humidity: much lower base values for dry conditions
        # Lower in summer (fire season), slightly higher in winter
        seasonal_rh = 25.0 - 15.0 * np.sin(2 * np.pi * days / 365)  # Annual cycle (10-40%)
        daily_rh_pattern = -np.sin(2 * np.pi * days)  # Inverse of temperature
        daily_rh = 8.0 * daily_rh_pattern + self.rng.normal(0, 3.0, num_intervals)
        base_rh = seasonal_rh + daily_rh

        # Wind: higher wind speeds to promote fire spread
        # Higher during day, lower at night
        # Higher in spring/fall, lower in summer/winter
        seasonal_wind = 15.0 + 8.0 * np.sin(2 * np.pi * days / 365)  # Annual cycle
        daily_wind_pattern = np.sin(2 * np.pi * days)  # Daily cycle
        daily_wind = 8.0 * daily_wind_pattern + self.rng.normal(0, 3.0, num_intervals)
        base_wind = seasonal_wind + daily_wind

        # Wind direction: seasonal and daily patterns
        # Example: prevailing wind direction is westerly (270°) in summer, southerly (180°) in winter
        seasonal_dir = 225 + 45 * np.sin(2 * np.pi * days / 365)  # 225±45° annual cycle
        # Daily: small oscillation (e.g., 10° amplitude) for land/sea breeze effect
        daily_dir_pattern = np.sin(2 * np.pi * days)
        daily_dir = 10.0 * daily_dir_pattern
        # Add random noise (±15°)
        dir_noise = self.rng.normal(0, 15.0, num_intervals)
        base_wind_dir = (seasonal_dir + daily_dir + dir_noise) % 360

        # Generate daily conditions
        daily_conditions = []
        for i in range(num_intervals):
            # Add correlated variations
            # Temperature and humidity are inversely correlated
            temp_variation = self.rng.normal(0, 6.0)  # ±6°F (more variation)
            rh_variation = -0.8 * temp_variation + self.rng.normal(
                0, 3.0
            )  # Stronger correlation with temp

            # Wind variations are independent but bounded
            wind_variation = self.rng.normal(0, 6.0)  # ±6 mph (more variation)

            # Calculate final values
            temp = base_temps[i] + temp_variation
            rh = base_rh[i] + rh_variation
            wind = base_wind[i] + wind_variation
            wind_dir = base_wind_dir[i]  # Use the generated wind direction

            # Much reduced precipitation for dry conditions
            # Very low probability during any season
            base_precip_prob = 0.02 + 0.03 * np.sin(
                2 * np.pi * (i + 90) / 365
            )  # Peak in winter/spring (2-5%)
            humidity_factor = max(0, (rh - 30.0) / 20.0)  # Only increase if RH > 30%
            precip_prob = np.clip(
                base_precip_prob * (1.0 + humidity_factor * 0.3), 0.0, 0.08
            )  # Max 8% chance

            precip = 0.0
            if self.rng.random() < precip_prob:
                # Create light precipitation events only
                # 90% chance of very light rain (0.01-0.1"), 10% light rain (0.1-0.2")
                rain_type = self.rng.random()
                if rain_type < 0.9:
                    # Very light rain
                    precip = self.rng.uniform(0.01, 0.1)
                else:
                    # Light rain
                    precip = self.rng.uniform(0.1, 0.2)

                # Apply minimal seasonal and humidity modifiers
                seasonal_factor = 1.0 + 0.1 * np.sin(
                    2 * np.pi * (i + 90) / 365
                )  # Minimal seasonal effect
                humidity_factor = 1.0 + max(0, (rh - 40.0) / 40.0) * 0.2  # Minimal humidity effect
                precip *= seasonal_factor * humidity_factor

            # Calculate fuel moistures based on weather conditions - much drier
            # Base moistures vary with season and recent precipitation - lower base values
            base_1hr = 3.0 + 2.0 * np.sin(
                2 * np.pi * (i + 90) / 365
            )  # Seasonal variation, very dry in summer (1-5%)
            base_10hr = 4.0 + 2.0 * np.sin(2 * np.pi * (i + 90) / 365)  # (2-6%)
            base_100hr = 6.0 + 2.0 * np.sin(2 * np.pi * (i + 90) / 365)  # (4-8%)

            # Adjust for recent weather with stronger drying effects
            temp_factor = 1.0 - 0.03 * (temp - 65.0)  # Stronger temperature effect for drying
            rh_factor = 1.0 + 0.02 * (
                rh - 25.0
            )  # Reduced humidity effect (base 25% instead of 50%)

            # Minimal precipitation effects
            if precip > 0:
                # Precipitation has minimal effect on fuel moisture in dry scenario
                if precip < 0.1:
                    # Very light rain: minimal increase
                    precip_factor = 1.0 + precip * 2.0  # Up to 1.2x increase
                else:
                    # Light rain: small increase
                    precip_factor = 1.0 + 0.2 + (precip - 0.1) * 3.0  # 1.2x to 1.5x increase
            else:
                precip_factor = 1.0

            # Apply factors to base moistures
            base_1hr *= temp_factor * rh_factor * precip_factor
            base_10hr *= temp_factor * rh_factor * precip_factor
            base_100hr *= temp_factor * rh_factor * precip_factor

            # Live fuel moistures have strong seasonal patterns but much lower base values
            # Peak in spring, lowest in late summer/fall
            herb_moisture = 40.0 + 60.0 * np.sin(
                2 * np.pi * (i - 30) / 365
            )  # Peak in spring (100%), low in fall (20%)
            woody_moisture = 60.0 + 40.0 * np.sin(
                2 * np.pi * (i - 45) / 365
            )  # Peak slightly later (100%), low in fall (20%)

            # Live fuels are minimally responsive to precipitation in dry scenario
            if precip > 0:
                # Live fuels absorb water minimally
                live_precip_factor = 1.0 + precip * 2.0  # Minimal response
            else:
                live_precip_factor = 1.0

            # Adjust live moistures for recent weather
            herb_moisture *= rh_factor * live_precip_factor
            woody_moisture *= rh_factor * live_precip_factor

            # Create daily condition
            daily = {
                "temperature": float(temp),
                "relative_humidity": float(
                    max(5.0, min(60.0, rh))
                ),  # Cap RH at 60% for dry conditions
                "wind_speed": float(max(5.0, min(50.0, wind))),  # Minimum 5 mph wind
                "wind_direction": float(wind_dir),  # Use the generated wind direction
                "precipitation": float(precip),
                "fuel_moistures": {
                    "1hr": float(max(1.0, min(15.0, base_1hr))),  # Very dry 1hr fuels (1-15%)
                    "10hr": float(max(2.0, min(20.0, base_10hr))),  # Dry 10hr fuels (2-20%)
                    "100hr": float(max(3.0, min(25.0, base_100hr))),  # Dry 100hr fuels (3-25%)
                    "live_herbaceous": float(
                        max(20.0, min(150.0, herb_moisture))
                    ),  # Dry live herbs (20-150%)
                    "live_woody": float(
                        max(30.0, min(120.0, woody_moisture))
                    ),  # Dry live woody (30-120%)
                },
            }
            daily_conditions.append(daily)

        # Create and return scenario
        return WeatherScenario(
            name="dry",
            daily_conditions=daily_conditions,
            metadata={
                "description": "Generated dry weather scenario conducive to fire spread",
                "num_intervals": num_intervals,
                "generated_at": datetime.now().isoformat(),
                "base_temperature": float(np.mean(base_temps)),
                "base_humidity": float(np.mean(base_rh)),
                "base_wind": float(np.mean(base_wind)),
                "fire_conducive": True,
            },
        )

    def generate_moderate_scenario(self, num_intervals: int = 30) -> WeatherScenario:
        """Generate a moderate weather scenario with balanced fire activity.

        Args:
            num_intervals: Number of intervals to generate

        Returns:
            Generated moderate weather scenario
        """
        # Generate seasonal patterns
        days = np.arange(num_intervals)

        # Temperature: moderate temperatures with seasonal variation
        # Base temperature varies from 45°F in winter to 85°F in summer
        seasonal_temp = 65.0 + 20.0 * np.sin(2 * np.pi * days / 365)  # Annual cycle (45-85°F)
        # Daily temperature range: cooler at night, warmer during day
        daily_pattern = np.sin(2 * np.pi * days)  # Daily cycle
        daily_temp = 8.0 * daily_pattern + self.rng.normal(0, 3.0, num_intervals)  # Daily variation
        base_temps = seasonal_temp + daily_temp

        # Relative humidity: moderate values with fire season drying
        # Lower in summer (fire season), higher in winter
        seasonal_rh = 45.0 - 20.0 * np.sin(2 * np.pi * days / 365)  # Annual cycle (25-65%)
        daily_rh_pattern = -np.sin(2 * np.pi * days)  # Inverse of temperature
        daily_rh = 10.0 * daily_rh_pattern + self.rng.normal(0, 4.0, num_intervals)
        base_rh = seasonal_rh + daily_rh

        # Wind: moderate speeds with more consistent patterns
        # Higher during day, lower at night
        # Higher in spring/fall, lower in summer/winter
        seasonal_wind = 12.0 + 6.0 * np.sin(2 * np.pi * days / 365)  # Annual cycle (6-18 mph)
        daily_wind_pattern = np.sin(2 * np.pi * days)  # Daily cycle
        daily_wind = 4.0 * daily_wind_pattern + self.rng.normal(0, 2.0, num_intervals)
        base_wind = seasonal_wind + daily_wind

        # Wind direction: seasonal and daily patterns
        seasonal_dir = 225 + 45 * np.sin(2 * np.pi * days / 365)  # 225±45° annual cycle
        daily_dir_pattern = np.sin(2 * np.pi * days)
        daily_dir = 10.0 * daily_dir_pattern
        dir_noise = self.rng.normal(0, 15.0, num_intervals)
        base_wind_dir = (seasonal_dir + daily_dir + dir_noise) % 360

        # Generate daily conditions
        daily_conditions = []
        for i in range(num_intervals):
            # Add correlated variations
            temp_variation = self.rng.normal(0, 4.0)  # ±4°F
            rh_variation = -0.6 * temp_variation + self.rng.normal(
                0, 4.0
            )  # Moderate correlation with temp

            # Wind variations
            wind_variation = self.rng.normal(0, 4.0)  # ±4 mph

            # Calculate final values
            temp = base_temps[i] + temp_variation
            rh = base_rh[i] + rh_variation
            wind = base_wind[i] + wind_variation
            wind_dir = base_wind_dir[i]

            # Balanced precipitation for realistic fire-weather cycles
            base_precip_prob = 0.08 + 0.12 * np.sin(
                2 * np.pi * (i + 90) / 365
            )  # Peak in winter/spring (8-20%)
            humidity_factor = max(0, (rh - 40.0) / 30.0)  # Only increase if RH > 40%
            precip_prob = np.clip(
                base_precip_prob * (1.0 + humidity_factor * 0.4), 0.0, 0.25
            )  # Max 25% chance

            precip = 0.0
            if self.rng.random() < precip_prob:
                # Create moderate precipitation events
                # 70% chance of light rain (0.02-0.2"), 25% moderate (0.2-0.6"), 5% heavy (0.6-1.2")
                rain_type = self.rng.random()
                if rain_type < 0.7:
                    # Light rain
                    precip = self.rng.uniform(0.02, 0.2)
                elif rain_type < 0.95:
                    # Moderate rain
                    precip = self.rng.uniform(0.2, 0.6)
                else:
                    # Heavy rain
                    precip = self.rng.uniform(0.6, 1.2)

                # Apply moderate seasonal and humidity modifiers
                seasonal_factor = 1.0 + 0.15 * np.sin(2 * np.pi * (i + 90) / 365)
                humidity_factor = 1.0 + max(0, (rh - 50.0) / 30.0) * 0.25
                precip *= seasonal_factor * humidity_factor

            # Calculate fuel moistures - moderate values
            base_1hr = 4.0 + 3.0 * np.sin(2 * np.pi * (i + 90) / 365)  # Seasonal variation (1-7%)
            base_10hr = 6.0 + 3.0 * np.sin(2 * np.pi * (i + 90) / 365)  # (3-9%)
            base_100hr = 8.0 + 3.0 * np.sin(2 * np.pi * (i + 90) / 365)  # (5-11%)

            # Adjust for weather conditions
            temp_factor = 1.0 - 0.025 * (temp - 65.0)  # Moderate temperature effect
            rh_factor = 1.0 + 0.025 * (rh - 40.0)  # Moderate humidity effect

            # Balanced precipitation effects for realistic fire-weather cycles
            if precip > 0:
                if precip < 0.2:
                    # Light rain: moderate increase
                    precip_factor = 1.0 + precip * 4.0  # Up to 1.8x increase
                elif precip < 0.6:
                    # Moderate rain: strong increase
                    precip_factor = 1.0 + 0.8 + (precip - 0.2) * 6.0  # 1.8x to 4.2x increase
                else:
                    # Heavy rain: very strong increase
                    precip_factor = 1.0 + 3.2 + (precip - 0.6) * 8.0  # 4.2x to 7.4x increase
            else:
                precip_factor = 1.0

            # Apply factors to base moistures
            base_1hr *= temp_factor * rh_factor * precip_factor
            base_10hr *= temp_factor * rh_factor * precip_factor
            base_100hr *= temp_factor * rh_factor * precip_factor

            # Live fuel moistures - moderate seasonal patterns
            herb_moisture = 50.0 + 70.0 * np.sin(
                2 * np.pi * (i - 30) / 365
            )  # Peak in spring (120%), low in fall (30%)
            woody_moisture = 70.0 + 50.0 * np.sin(
                2 * np.pi * (i - 45) / 365
            )  # Peak slightly later (120%), low in fall (20%)

            # Live fuels respond moderately to precipitation
            if precip > 0:
                live_precip_factor = 1.0 + precip * 3.0  # Moderate response
            else:
                live_precip_factor = 1.0

            # Adjust live moistures
            herb_moisture *= rh_factor * live_precip_factor
            woody_moisture *= rh_factor * live_precip_factor

            # Create daily condition
            daily = {
                "temperature": float(temp),
                "relative_humidity": float(
                    max(10.0, min(80.0, rh))
                ),  # Cap RH at 80% for moderate conditions
                "wind_speed": float(max(3.0, min(25.0, wind))),  # Minimum 3 mph wind, max 25 mph
                "wind_direction": float(wind_dir),
                "precipitation": float(precip),
                "fuel_moistures": {
                    "1hr": float(max(2.0, min(20.0, base_1hr))),  # Moderate 1hr fuels (2-20%)
                    "10hr": float(max(3.0, min(25.0, base_10hr))),  # Moderate 10hr fuels (3-25%)
                    "100hr": float(max(5.0, min(30.0, base_100hr))),  # Moderate 100hr fuels (5-30%)
                    "live_herbaceous": float(
                        max(30.0, min(200.0, herb_moisture))
                    ),  # Moderate live herbs (30-200%)
                    "live_woody": float(
                        max(50.0, min(150.0, woody_moisture))
                    ),  # Moderate live woody (50-150%)
                },
            }
            daily_conditions.append(daily)

        # Create and return scenario
        return WeatherScenario(
            name="moderate",
            daily_conditions=daily_conditions,
            metadata={
                "description": "Generated moderate weather scenario with balanced fire activity",
                "num_intervals": num_intervals,
                "generated_at": datetime.now().isoformat(),
                "base_temperature": float(np.mean(base_temps)),
                "base_humidity": float(np.mean(base_rh)),
                "base_wind": float(np.mean(base_wind)),
                "fire_conducive": "balanced",
            },
        )

    def generate_conservative_scenario(self, num_intervals: int = 30) -> WeatherScenario:
        """Generate a conservative weather scenario with limited fire activity.

        Args:
            num_intervals: Number of intervals to generate

        Returns:
            Generated conservative weather scenario
        """
        # Calculate number of years and days
        num_years = max(1, num_intervals // 365)
        remaining_days = num_intervals % 365

        daily_conditions = []

        # Generate weather year by year for inter-annual variability
        for year in range(num_years):
            # Use different random seed for each year to create variability
            year_rng = np.random.default_rng(
                self._random_seed + year if self._random_seed else year
            )

            # Generate 365 days for this year
            days_in_year = 365
            days = np.arange(days_in_year)

            # Add inter-annual variability to base patterns
            # Each year can be slightly warmer/cooler, wetter/drier
            annual_temp_anomaly = year_rng.normal(0, 2.0)  # ±2°F year-to-year variation
            annual_precip_factor = year_rng.uniform(0.7, 1.3)  # 70-130% of normal precipitation
            annual_humidity_anomaly = year_rng.normal(0, 3.0)  # ±3% humidity variation

            # Temperature: closer to default but slightly warmer
            # Base temperature varies from 50°F in winter to 80°F in summer
            seasonal_temp = 65.0 + 15.0 * np.sin(2 * np.pi * days / 365) + annual_temp_anomaly
            # Daily temperature range: cooler at night, warmer during day
            daily_pattern = np.sin(2 * np.pi * days)  # Daily cycle
            daily_temp = 8.0 * daily_pattern + year_rng.normal(0, 3.0, days_in_year)
            base_temps = seasonal_temp + daily_temp

            # Relative humidity: closer to default but slightly lower during fire season
            seasonal_rh = 60.0 - 25.0 * np.sin(2 * np.pi * days / 365) + annual_humidity_anomaly
            daily_rh_pattern = -np.sin(2 * np.pi * days)  # Inverse of temperature
            daily_rh = 12.0 * daily_rh_pattern + year_rng.normal(0, 4.0, days_in_year)
            base_rh = seasonal_rh + daily_rh

            # Wind: similar to default
            seasonal_wind = 10.0 + 4.0 * np.sin(2 * np.pi * days / 365)
            daily_wind_pattern = np.sin(2 * np.pi * days)
            daily_wind = 4.0 * daily_wind_pattern + year_rng.normal(0, 2.0, days_in_year)
            base_wind = seasonal_wind + daily_wind

            # Wind direction: seasonal and daily patterns
            seasonal_dir = 225 + 45 * np.sin(2 * np.pi * days / 365)
            daily_dir_pattern = np.sin(2 * np.pi * days)
            daily_dir = 10.0 * daily_dir_pattern
            dir_noise = year_rng.normal(0, 15.0, days_in_year)
            base_wind_dir = (seasonal_dir + daily_dir + dir_noise) % 360

            # Generate daily conditions for this year
            for i in range(days_in_year):
                # Add correlated variations
                temp_variation = year_rng.normal(0, 4.0)  # ±4°F
                rh_variation = -0.4 * temp_variation + year_rng.normal(0, 4.0)

                # Wind variations
                wind_variation = year_rng.normal(0, 3.0)  # ±3 mph

                # Calculate final values
                temp = base_temps[i] + temp_variation
                rh = base_rh[i] + rh_variation
                wind = base_wind[i] + wind_variation
                wind_dir = base_wind_dir[i]

                # Precipitation similar to default but slightly less, with annual variability
                base_precip_prob = (
                    0.06 + 0.10 * np.sin(2 * np.pi * (i + 90) / 365)
                ) * annual_precip_factor
                humidity_factor = max(0, (rh - 50.0) / 30.0)
                precip_prob = np.clip(base_precip_prob * (1.0 + humidity_factor * 0.4), 0.0, 0.20)

                precip = 0.0
                if year_rng.random() < precip_prob:
                    # Create precipitation events similar to default
                    rain_type = year_rng.random()
                    if rain_type < 0.75:
                        # Light rain
                        precip = year_rng.uniform(0.05, 0.25)
                    elif rain_type < 0.95:
                        # Moderate rain
                        precip = year_rng.uniform(0.25, 0.7)
                    else:
                        # Heavy rain
                        precip = year_rng.uniform(0.7, 1.5)

                    # Apply seasonal and humidity modifiers
                    seasonal_factor = 1.0 + 0.18 * np.sin(2 * np.pi * (i + 90) / 365)
                    humidity_factor = 1.0 + max(0, (rh - 60.0) / 30.0) * 0.3
                    precip *= seasonal_factor * humidity_factor * annual_precip_factor

                # Calculate fuel moistures - closer to default but slightly drier
                base_1hr = 5.5 + 3.5 * np.sin(2 * np.pi * (i + 90) / 365)
                base_10hr = 7.0 + 3.0 * np.sin(2 * np.pi * (i + 90) / 365)
                base_100hr = 9.0 + 3.0 * np.sin(2 * np.pi * (i + 90) / 365)

                # Adjust for weather conditions
                temp_factor = 1.0 - 0.02 * (temp - 65.0)
                rh_factor = 1.0 + 0.025 * (rh - 45.0)

                # Precipitation effects similar to default
                if precip > 0:
                    if precip < 0.25:
                        precip_factor = 1.0 + precip * 3.5
                    elif precip < 0.7:
                        precip_factor = 1.0 + 0.9 + (precip - 0.25) * 4.5
                    else:
                        precip_factor = 1.0 + 2.9 + (precip - 0.7) * 6.5
                else:
                    precip_factor = 1.0

                # Apply factors to base moistures
                base_1hr *= temp_factor * rh_factor * precip_factor
                base_10hr *= temp_factor * rh_factor * precip_factor
                base_100hr *= temp_factor * rh_factor * precip_factor

                # Live fuel moistures - closer to default values
                herb_moisture = 65.0 + 75.0 * np.sin(2 * np.pi * (i - 30) / 365)
                woody_moisture = 85.0 + 55.0 * np.sin(2 * np.pi * (i - 45) / 365)

                # Live fuels respond to precipitation
                if precip > 0:
                    live_precip_factor = 1.0 + precip * 4.0
                else:
                    live_precip_factor = 1.0

                # Adjust live moistures
                herb_moisture *= rh_factor * live_precip_factor
                woody_moisture *= rh_factor * live_precip_factor

                # Create daily condition
                daily = {
                    "temperature": float(temp),
                    "relative_humidity": float(max(15.0, min(90.0, rh))),
                    "wind_speed": float(max(1.0, min(35.0, wind))),
                    "wind_direction": float(wind_dir),
                    "precipitation": float(precip),
                    "fuel_moistures": {
                        "1hr": float(max(3.0, min(25.0, base_1hr))),
                        "10hr": float(max(4.0, min(30.0, base_10hr))),
                        "100hr": float(max(6.0, min(35.0, base_100hr))),
                        "live_herbaceous": float(max(40.0, min(250.0, herb_moisture))),
                        "live_woody": float(max(60.0, min(180.0, woody_moisture))),
                    },
                }
                daily_conditions.append(daily)

        # Handle remaining days if num_intervals is not a multiple of 365
        if remaining_days > 0:
            # Generate remaining days for partial year
            year_rng = np.random.default_rng(
                self._random_seed + num_years if self._random_seed else num_years
            )

            days = np.arange(remaining_days)
            annual_temp_anomaly = year_rng.normal(0, 2.0)
            annual_precip_factor = year_rng.uniform(0.7, 1.3)
            annual_humidity_anomaly = year_rng.normal(0, 3.0)

            seasonal_temp = 65.0 + 15.0 * np.sin(2 * np.pi * days / 365) + annual_temp_anomaly
            daily_pattern = np.sin(2 * np.pi * days)
            daily_temp = 8.0 * daily_pattern + year_rng.normal(0, 3.0, remaining_days)
            base_temps = seasonal_temp + daily_temp

            seasonal_rh = 60.0 - 25.0 * np.sin(2 * np.pi * days / 365) + annual_humidity_anomaly
            daily_rh_pattern = -np.sin(2 * np.pi * days)
            daily_rh = 12.0 * daily_rh_pattern + year_rng.normal(0, 4.0, remaining_days)
            base_rh = seasonal_rh + daily_rh

            seasonal_wind = 10.0 + 4.0 * np.sin(2 * np.pi * days / 365)
            daily_wind_pattern = np.sin(2 * np.pi * days)
            daily_wind = 4.0 * daily_wind_pattern + year_rng.normal(0, 2.0, remaining_days)
            base_wind = seasonal_wind + daily_wind

            seasonal_dir = 225 + 45 * np.sin(2 * np.pi * days / 365)
            daily_dir_pattern = np.sin(2 * np.pi * days)
            daily_dir = 10.0 * daily_dir_pattern
            dir_noise = year_rng.normal(0, 15.0, remaining_days)
            base_wind_dir = (seasonal_dir + daily_dir + dir_noise) % 360

            for i in range(remaining_days):
                temp_variation = year_rng.normal(0, 4.0)
                rh_variation = -0.4 * temp_variation + year_rng.normal(0, 4.0)
                wind_variation = year_rng.normal(0, 3.0)

                temp = base_temps[i] + temp_variation
                rh = base_rh[i] + rh_variation
                wind = base_wind[i] + wind_variation
                wind_dir = base_wind_dir[i]

                base_precip_prob = (
                    0.06 + 0.10 * np.sin(2 * np.pi * (i + 90) / 365)
                ) * annual_precip_factor
                humidity_factor = max(0, (rh - 50.0) / 30.0)
                precip_prob = np.clip(base_precip_prob * (1.0 + humidity_factor * 0.4), 0.0, 0.20)

                precip = 0.0
                if year_rng.random() < precip_prob:
                    rain_type = year_rng.random()
                    if rain_type < 0.75:
                        precip = year_rng.uniform(0.05, 0.25)
                    elif rain_type < 0.95:
                        precip = year_rng.uniform(0.25, 0.7)
                    else:
                        precip = year_rng.uniform(0.7, 1.5)

                    seasonal_factor = 1.0 + 0.18 * np.sin(2 * np.pi * (i + 90) / 365)
                    humidity_factor = 1.0 + max(0, (rh - 60.0) / 30.0) * 0.3
                    precip *= seasonal_factor * humidity_factor * annual_precip_factor

                base_1hr = 5.5 + 3.5 * np.sin(2 * np.pi * (i + 90) / 365)
                base_10hr = 7.0 + 3.0 * np.sin(2 * np.pi * (i + 90) / 365)
                base_100hr = 9.0 + 3.0 * np.sin(2 * np.pi * (i + 90) / 365)

                temp_factor = 1.0 - 0.02 * (temp - 65.0)
                rh_factor = 1.0 + 0.025 * (rh - 45.0)

                if precip > 0:
                    if precip < 0.25:
                        precip_factor = 1.0 + precip * 3.5
                    elif precip < 0.7:
                        precip_factor = 1.0 + 0.9 + (precip - 0.25) * 4.5
                    else:
                        precip_factor = 1.0 + 2.9 + (precip - 0.7) * 6.5
                else:
                    precip_factor = 1.0

                base_1hr *= temp_factor * rh_factor * precip_factor
                base_10hr *= temp_factor * rh_factor * precip_factor
                base_100hr *= temp_factor * rh_factor * precip_factor

                herb_moisture = 65.0 + 75.0 * np.sin(2 * np.pi * (i - 30) / 365)
                woody_moisture = 85.0 + 55.0 * np.sin(2 * np.pi * (i - 45) / 365)

                if precip > 0:
                    live_precip_factor = 1.0 + precip * 4.0
                else:
                    live_precip_factor = 1.0

                herb_moisture *= rh_factor * live_precip_factor
                woody_moisture *= rh_factor * live_precip_factor

                daily = {
                    "temperature": float(temp),
                    "relative_humidity": float(max(15.0, min(90.0, rh))),
                    "wind_speed": float(max(1.0, min(35.0, wind))),
                    "wind_direction": float(wind_dir),
                    "precipitation": float(precip),
                    "fuel_moistures": {
                        "1hr": float(max(3.0, min(25.0, base_1hr))),
                        "10hr": float(max(4.0, min(30.0, base_10hr))),
                        "100hr": float(max(6.0, min(35.0, base_100hr))),
                        "live_herbaceous": float(max(40.0, min(250.0, herb_moisture))),
                        "live_woody": float(max(60.0, min(180.0, woody_moisture))),
                    },
                }
                daily_conditions.append(daily)

        # Create and return scenario
        return WeatherScenario(
            name="conservative",
            daily_conditions=daily_conditions,
            metadata={
                "description": f"Generated conservative weather scenario with limited fire activity for {num_years} years + {remaining_days} days",  # noqa: E501
                "num_intervals": num_intervals,
                "num_years": num_years,
                "generated_at": datetime.now().isoformat(),
                "inter_annual_variability": True,
                "fire_conducive": "limited",
            },
        )

    def generate_year_weather(
        self, year: int, scenario_type: str = "conservative"
    ) -> List[Dict[str, Any]]:
        """Generate weather for a specific year with inter-annual variability.

        Args:
            year: Year number (0-based)
            scenario_type: Type of weather scenario ("conservative", "moderate", "dry", "default")

        Returns:
            List of daily weather conditions for the year (365 days)
        """
        # Use different random seed for each year to create variability
        year_rng = np.random.default_rng(self._random_seed + year if self._random_seed else year)

        # Generate 365 days for this year
        days_in_year = 365
        days = np.arange(days_in_year)

        # Add inter-annual variability to base patterns
        # Each year can be slightly warmer/cooler, wetter/drier
        annual_temp_anomaly = year_rng.normal(0, 2.0)  # ±2°F year-to-year variation
        annual_precip_factor = year_rng.uniform(0.7, 1.3)  # 70-130% of normal precipitation
        annual_humidity_anomaly = year_rng.normal(0, 3.0)  # ±3% humidity variation

        # Set base parameters based on scenario type
        if scenario_type == "conservative":
            base_temp = 65.0
            temp_range = 15.0
            base_humidity = 60.0
            humidity_range = 25.0
            base_precip_prob = 0.06
            precip_seasonal = 0.10
            fuel_1hr_base = 5.5
            fuel_1hr_range = 3.5
        elif scenario_type == "moderate":
            base_temp = 65.0
            temp_range = 20.0
            base_humidity = 45.0
            humidity_range = 20.0
            base_precip_prob = 0.05
            precip_seasonal = 0.08
            fuel_1hr_base = 4.0
            fuel_1hr_range = 3.0
        elif scenario_type == "dry":
            base_temp = 75.0
            temp_range = 30.0
            base_humidity = 25.0
            humidity_range = 15.0
            base_precip_prob = 0.02
            precip_seasonal = 0.03
            fuel_1hr_base = 3.0
            fuel_1hr_range = 2.0
        else:  # default
            base_temp = 65.0
            temp_range = 25.0
            base_humidity = 70.0
            humidity_range = 30.0
            base_precip_prob = 0.08
            precip_seasonal = 0.12
            fuel_1hr_base = 6.0
            fuel_1hr_range = 4.0

        # Temperature patterns
        seasonal_temp = (
            base_temp + temp_range * np.sin(2 * np.pi * days / 365) + annual_temp_anomaly
        )
        daily_pattern = np.sin(2 * np.pi * days)
        daily_temp = 8.0 * daily_pattern + year_rng.normal(0, 3.0, days_in_year)
        base_temps = seasonal_temp + daily_temp

        # Humidity patterns
        seasonal_rh = (
            base_humidity
            - humidity_range * np.sin(2 * np.pi * days / 365)
            + annual_humidity_anomaly
        )
        daily_rh_pattern = -np.sin(2 * np.pi * days)
        daily_rh = 12.0 * daily_rh_pattern + year_rng.normal(0, 4.0, days_in_year)
        base_rh = seasonal_rh + daily_rh

        # Wind patterns
        seasonal_wind = 10.0 + 4.0 * np.sin(2 * np.pi * days / 365)
        daily_wind_pattern = np.sin(2 * np.pi * days)
        daily_wind = 4.0 * daily_wind_pattern + year_rng.normal(0, 2.0, days_in_year)
        base_wind = seasonal_wind + daily_wind

        # Wind direction patterns
        seasonal_dir = 225 + 45 * np.sin(2 * np.pi * days / 365)
        daily_dir_pattern = np.sin(2 * np.pi * days)
        daily_dir = 10.0 * daily_dir_pattern
        dir_noise = year_rng.normal(0, 15.0, days_in_year)
        base_wind_dir = (seasonal_dir + daily_dir + dir_noise) % 360

        # Generate daily conditions for this year
        daily_conditions = []
        for i in range(days_in_year):
            # Add correlated variations
            temp_variation = year_rng.normal(0, 4.0)
            rh_variation = -0.4 * temp_variation + year_rng.normal(0, 4.0)
            wind_variation = year_rng.normal(0, 3.0)

            # Calculate final values
            temp = base_temps[i] + temp_variation
            rh = base_rh[i] + rh_variation
            wind = base_wind[i] + wind_variation
            wind_dir = base_wind_dir[i]

            # Precipitation with annual variability
            base_precip_prob_day = (
                base_precip_prob + precip_seasonal * np.sin(2 * np.pi * (i + 90) / 365)
            ) * annual_precip_factor
            humidity_factor = max(0, (rh - 50.0) / 30.0)
            precip_prob = np.clip(base_precip_prob_day * (1.0 + humidity_factor * 0.4), 0.0, 0.20)

            precip = 0.0
            if year_rng.random() < precip_prob:
                rain_type = year_rng.random()
                if rain_type < 0.75:
                    precip = year_rng.uniform(0.05, 0.25)
                elif rain_type < 0.95:
                    precip = year_rng.uniform(0.25, 0.7)
                else:
                    precip = year_rng.uniform(0.7, 1.5)

                seasonal_factor = 1.0 + 0.18 * np.sin(2 * np.pi * (i + 90) / 365)
                humidity_factor = 1.0 + max(0, (rh - 60.0) / 30.0) * 0.3
                precip *= seasonal_factor * humidity_factor * annual_precip_factor

            # Calculate fuel moistures
            base_1hr = fuel_1hr_base + fuel_1hr_range * np.sin(2 * np.pi * (i + 90) / 365)
            base_10hr = base_1hr + 1.5
            base_100hr = base_1hr + 3.5

            # Adjust for weather conditions
            temp_factor = 1.0 - 0.02 * (temp - 65.0)
            rh_factor = 1.0 + 0.025 * (rh - 45.0)

            # Precipitation effects
            if precip > 0:
                if precip < 0.25:
                    precip_factor = 1.0 + precip * 3.5
                elif precip < 0.7:
                    precip_factor = 1.0 + 0.9 + (precip - 0.25) * 4.5
                else:
                    precip_factor = 1.0 + 2.9 + (precip - 0.7) * 6.5
            else:
                precip_factor = 1.0

            # Apply factors to base moistures
            base_1hr *= temp_factor * rh_factor * precip_factor
            base_10hr *= temp_factor * rh_factor * precip_factor
            base_100hr *= temp_factor * rh_factor * precip_factor

            # Live fuel moistures
            herb_moisture = 65.0 + 75.0 * np.sin(2 * np.pi * (i - 30) / 365)
            woody_moisture = 85.0 + 55.0 * np.sin(2 * np.pi * (i - 45) / 365)

            if precip > 0:
                live_precip_factor = 1.0 + precip * 4.0
            else:
                live_precip_factor = 1.0

            herb_moisture *= rh_factor * live_precip_factor
            woody_moisture *= rh_factor * live_precip_factor

            # Create daily condition
            daily = {
                "temperature": float(temp),
                "relative_humidity": float(max(15.0, min(90.0, rh))),
                "wind_speed": float(max(1.0, min(35.0, wind))),
                "wind_direction": float(wind_dir),
                "precipitation": float(precip),
                "fuel_moistures": {
                    "1hr": float(max(3.0, min(25.0, base_1hr))),
                    "10hr": float(max(4.0, min(30.0, base_10hr))),
                    "100hr": float(max(6.0, min(35.0, base_100hr))),
                    "live_herbaceous": float(max(40.0, min(250.0, herb_moisture))),
                    "live_woody": float(max(60.0, min(180.0, woody_moisture))),
                },
            }
            daily_conditions.append(daily)

        return daily_conditions

    def update_scenario_for_year(self, year: int, scenario_type: str = "conservative") -> None:
        """Update the current scenario with weather for a specific year.

        Args:
            year: Year number (0-based)
            scenario_type: Type of weather scenario to generate
        """
        # Generate weather for this year
        year_weather = self.generate_year_weather(year, scenario_type)

        # Update the current scenario with this year's weather
        if self.current_scenario:
            scenario = self.scenarios[self.current_scenario]

            # Only update traditional WeatherScenario objects
            if isinstance(scenario, WeatherScenario):
                # Replace the daily conditions with this year's weather
                scenario.daily_conditions = year_weather
                # Update metadata
                scenario.metadata.update(
                    {
                        "current_year": year,
                        "scenario_type": scenario_type,
                        "generated_at": datetime.now().isoformat(),
                        "inter_annual_variability": True,
                    }
                )
            elif isinstance(scenario, LazyNEXGDDPScenario):
                raise ValueError(
                    f"Cannot update lazy scenario '{self.current_scenario}' - use load_nex_gddp_scenario_lazy() instead"
                )
            else:
                raise ValueError(f"Unknown scenario type: {type(scenario)}")

        # Reset current day to start of year
        self._current_day = 0

        logger.info(
            f"Updated scenario '{self.current_scenario}' with weather for year {year} ({scenario_type} type)"
        )

    def load_nex_gddp_scenario(
        self,
        data_directory: str,
        scenario_name: str,
        years: Optional[List[int]] = None,
        spatial_subset: Optional[Dict[str, Union[int, float]]] = None,
        model_name: str = "ACCESS-ESM1-5",
        experiment: str = "historical",
        variant: str = "r1i1p1f1",
    ) -> None:
        """Load weather scenario from NEX-GDDP-CMIP6 GeoTIFF files.

        This method loads multi-year weather data from NASA's NEX-GDDP-CMIP6
        downscaled climate projections, which provide daily weather variables
        at 0.25-degree spatial resolution.

        Args:
            data_directory: Path to directory containing NEX-GDDP-CMIP6 files
            scenario_name: Name for the created weather scenario
            years: List of years to load (if None, loads all available years)
            spatial_subset: Optional spatial subset definition:
                - For pixel coordinates: {"row_start": int, "row_end": int, "col_start": int, "col_end": int}
                - For geographic bounds: {"north": float, "south": float, "east": float, "west": float}
            model_name: Climate model name (default: ACCESS-ESM1-5)
            experiment: CMIP6 experiment name (default: historical)
            variant: Model variant identifier (default: r1i1p1f1)

        Raises:
            ImportError: If rasterio is not available
            FileNotFoundError: If required data files are not found
            ValueError: If data files are incompatible or malformed
        """
        if not RASTERIO_AVAILABLE:
            raise ImportError(
                "rasterio is required for NEX-GDDP-CMIP6 data loading. Install with: pip install rasterio"
            )

        logger.info(f"Loading NEX-GDDP-CMIP6 scenario '{scenario_name}' from {data_directory}")

        # Find available data files
        data_files = self._find_nex_gddp_files(data_directory, model_name, experiment, variant)

        if not data_files:
            raise FileNotFoundError(f"No NEX-GDDP-CMIP6 files found in {data_directory}")

        # Determine years to load
        available_years = sorted(data_files.keys())
        if years is None:
            years_to_load = available_years
        else:
            years_to_load = [y for y in years if y in available_years]
            if not years_to_load:
                raise ValueError(
                    f"None of the requested years {years} are available. Available years: {available_years}"
                )

        logger.info(f"Loading {len(years_to_load)} years: {years_to_load}")

        # Load data for each year
        all_daily_conditions = []
        metadata = {
            "description": f"NEX-GDDP-CMIP6 weather scenario from {model_name}",
            "data_source": "NEX-GDDP-CMIP6",
            "model": model_name,
            "experiment": experiment,
            "variant": variant,
            "years": years_to_load,
            "loaded_at": datetime.now().isoformat(),
            "spatial_subset": spatial_subset,
        }

        for year in years_to_load:
            logger.info(f"Loading year {year}...")
            year_files = data_files[year]

            # Load daily conditions for this year
            year_conditions = self._load_nex_gddp_year(year_files, spatial_subset)
            all_daily_conditions.extend(year_conditions)

            logger.info(f"Loaded {len(year_conditions)} days for year {year}")

        # Create and add scenario
        scenario = WeatherScenario(
            name=scenario_name,
            daily_conditions=all_daily_conditions,
            metadata=metadata,
        )

        self.scenarios[scenario_name] = scenario
        logger.info(
            f"Created NEX-GDDP-CMIP6 scenario '{scenario_name}' with {len(all_daily_conditions)} days"
        )

    def _find_nex_gddp_files(
        self,
        data_directory: str,
        model_name: str,
        experiment: str,
        variant: str,
    ) -> Dict[int, Dict[str, str]]:
        """Find and organize NEX-GDDP-CMIP6 files by year and variable.

        Expected filename format: {variable}_day_{model}_{experiment}_{variant}_gn_{year}.tif

        Args:
            data_directory: Directory containing data files
            model_name: Climate model name
            experiment: CMIP6 experiment name
            variant: Model variant identifier

        Returns:
            Dictionary mapping years to variable file paths
        """
        data_dir = Path(data_directory)
        if not data_dir.exists():
            raise FileNotFoundError(f"Data directory not found: {data_directory}")

        # Required variables for weather scenarios
        required_vars = ["tasmax", "tasmin", "hurs", "pr", "sfcWind"]

        # Pattern for NEX-GDDP-CMIP6 files
        pattern = f"*_day_{model_name}_{experiment}_{variant}_gn_*.tif"

        files_by_year = {}

        for file_path in data_dir.glob(pattern):
            filename = file_path.name

            # Parse filename: variable_day_model_experiment_variant_gn_year.tif
            parts = filename.replace(".ti", "").split("_")
            if len(parts) >= 7:
                variable = parts[0]
                year_str = parts[-1]

                try:
                    year = int(year_str)
                except ValueError:
                    logger.warning(f"Could not parse year from filename: {filename}")
                    continue

                if variable in required_vars:
                    if year not in files_by_year:
                        files_by_year[year] = {}
                    files_by_year[year][variable] = str(file_path)

        # Filter years that have all required variables
        complete_years = {}
        for year, var_files in files_by_year.items():
            if all(var in var_files for var in required_vars):
                complete_years[year] = var_files
            else:
                missing = [var for var in required_vars if var not in var_files]
                logger.warning(f"Year {year} missing variables: {missing}")

        logger.info(
            f"Found complete data for {len(complete_years)} years: {sorted(complete_years.keys())}"
        )
        return complete_years

    def _load_nex_gddp_year(
        self,
        year_files: Dict[str, str],
        spatial_subset: Optional[Dict[str, Union[int, float]]] = None,
    ) -> List[Dict[str, Any]]:
        """Load daily weather conditions for one year from NEX-GDDP-CMIP6 files.

        Args:
            year_files: Dictionary mapping variable names to file paths
            spatial_subset: Optional spatial subset specification

        Returns:
            List of daily weather condition dictionaries
        """
        # Open all files and get basic info
        datasets = {}
        spatial_window = None

        try:
            # Open each variable file
            for var, file_path in year_files.items():
                datasets[var] = rasterio.open(file_path)

            # Get a reference dataset for spatial info
            ref_dataset = datasets[list(datasets.keys())[0]]
            num_days = ref_dataset.count

            # Calculate spatial window if subset requested
            if spatial_subset is not None:
                spatial_window = self._calculate_spatial_window(ref_dataset, spatial_subset)

            # Load data for each day
            daily_conditions = []

            for day in range(1, num_days + 1):  # 1-indexed bands
                daily_data = {}

                # Load each variable for this day
                for var, dataset in datasets.items():
                    if spatial_window:
                        data = dataset.read(day, window=spatial_window)
                    else:
                        data = dataset.read(day)

                    # Calculate spatial average if we have spatial data
                    if data.size > 1:
                        # Use spatial average for point-based weather
                        daily_data[var] = float(np.nanmean(data))
                    else:
                        daily_data[var] = float(data.flat[0])

                # Convert units and create weather condition
                weather_condition = self._convert_nex_gddp_units(daily_data)
                daily_conditions.append(weather_condition)

            return daily_conditions

        finally:
            # Clean up datasets
            for dataset in datasets.values():
                dataset.close()

    def _calculate_spatial_window(
        self,
        dataset: "rasterio.DatasetReader",
        spatial_subset: Dict[str, Union[int, float]],
    ) -> Window:
        """Calculate spatial window for subsetting rasterio data.

        Args:
            dataset: Rasterio dataset
            spatial_subset: Spatial subset specification

        Returns:
            Rasterio Window object
        """
        if "row_start" in spatial_subset:
            # Pixel-based subset
            row_start = spatial_subset["row_start"]
            row_end = spatial_subset["row_end"]
            col_start = spatial_subset["col_start"]
            col_end = spatial_subset["col_end"]

            height = row_end - row_start
            width = col_end - col_start

            return Window(col_start, row_start, width, height)

        elif "north" in spatial_subset:
            # Geographic bounds subset
            north = spatial_subset["north"]
            south = spatial_subset["south"]
            east = spatial_subset["east"]
            west = spatial_subset["west"]

            # Convert geographic coordinates to pixel coordinates
            transform = dataset.transform

            # Get pixel coordinates
            col_start, row_start = ~transform * (west, north)
            col_end, row_end = ~transform * (east, south)

            # Ensure integer pixel coordinates
            col_start = max(0, int(col_start))
            row_start = max(0, int(row_start))
            col_end = min(dataset.width, int(col_end))
            row_end = min(dataset.height, int(row_end))

            width = col_end - col_start
            height = row_end - row_start

            return Window(col_start, row_start, width, height)

        else:
            raise ValueError(
                "Spatial subset must specify either pixel coordinates or geographic bounds"
            )

    def _convert_nex_gddp_units(self, daily_data: Dict[str, float]) -> Dict[str, Any]:
        """Convert NEX-GDDP-CMIP6 data units to weather module format.

        NEX-GDDP-CMIP6 units:
        - tasmax, tasmin: Kelvin
        - hurs: % (0-100)
        - pr: kg m-2 s-1
        - sfcWind: m/s

        Weather module units:
        - temperature: Fahrenheit
        - relative_humidity: % (0-100)
        - precipitation: inches
        - wind_speed: mph

        Args:
            daily_data: Raw daily data from NEX-GDDP-CMIP6

        Returns:
            Converted daily weather condition
        """
        # Temperature conversion: Kelvin to Fahrenheit
        # Note: We'll use tasmax as the daily temperature, could also average tasmax/tasmin
        temp_k = daily_data.get("tasmax", 288.15)  # Default ~15°C if missing
        temp_f = (temp_k - 273.15) * 9 / 5 + 32

        # Relative humidity (already in %)
        rh = daily_data.get("hurs", 50.0)
        rh = max(1.0, min(100.0, rh))  # Clamp to valid range

        # Precipitation: kg m-2 s-1 to inches/day
        # 1 kg/m² = 1 mm of water, and 1 inch = 25.4 mm
        # Rate is per second, so multiply by 86400 seconds/day
        pr_rate = daily_data.get("pr", 0.0)  # kg m-2 s-1
        pr_mm_per_day = pr_rate * 86400  # Convert to mm/day
        pr_inches = pr_mm_per_day / 25.4  # Convert to inches

        # Wind speed: m/s to mph
        wind_ms = daily_data.get("sfcWind", 2.0)  # Default 2 m/s if missing
        wind_mph = wind_ms * 2.237  # 1 m/s = 2.237 mph

        # Estimate wind direction (not provided in NEX-GDDP-CMIP6)
        # Use a simple seasonal pattern for now
        day_of_year = len(daily_data) % 365  # Rough estimate
        wind_dir = 225 + 45 * np.sin(2 * np.pi * day_of_year / 365)  # Seasonal variation

        # Calculate fuel moistures based on weather conditions
        fuel_moistures = self._estimate_fuel_moistures_from_weather(temp_f, rh, pr_inches, wind_mph)

        return {
            "temperature": float(temp_f),
            "relative_humidity": float(rh),
            "wind_speed": float(wind_mph),
            "wind_direction": float(wind_dir),
            "precipitation": float(pr_inches),
            "fuel_moistures": fuel_moistures,
        }

    def _estimate_fuel_moistures_from_weather(
        self,
        temperature: float,
        humidity: float,
        precipitation: float,
        wind_speed: float,
    ) -> Dict[str, float]:
        """Estimate fuel moistures from basic weather variables.

        This uses simplified relationships between weather and fuel moisture
        when detailed fuel moisture data is not available.

        Args:
            temperature: Temperature in Fahrenheit
            humidity: Relative humidity in %
            precipitation: Precipitation in inches
            wind_speed: Wind speed in mph

        Returns:
            Dictionary of estimated fuel moisture percentages
        """
        # Base fuel moistures from temperature and humidity using EMC relationships
        temp_c = (temperature - 32) * 5 / 9  # Convert to Celsius

        # Calculate equilibrium moisture content (simplified Simard equation)
        humidity / 100.0
        emc = 0.18 * (21.1 - 0.39 * temp_c + 0.0183 * temp_c**2) * (1.0 - np.exp(-0.115 * humidity))
        emc = max(2.0, min(30.0, emc))  # Reasonable bounds

        # Adjust for precipitation
        precip_factor = 1.0
        if precipitation > 0:
            if precipitation < 0.1:
                precip_factor = 1.0 + precipitation * 5.0  # Light rain
            elif precipitation < 0.5:
                precip_factor = 1.5 + (precipitation - 0.1) * 7.5  # Moderate rain
            else:
                precip_factor = 4.5 + (precipitation - 0.5) * 10.0  # Heavy rain

        # Base moistures scaled from EMC
        moisture_1hr = emc * precip_factor
        moisture_10hr = emc * 1.2 * precip_factor
        moisture_100hr = emc * 1.5 * precip_factor

        # Live fuel moistures - more responsive to recent precipitation and seasonal patterns
        # These are higher and more variable than dead fuels
        base_live_herb = 60.0 + 20.0 * (humidity - 50.0) / 50.0  # 40-80% base range
        base_live_woody = 80.0 + 15.0 * (humidity - 50.0) / 50.0  # 65-95% base range

        # Strong precipitation response for live fuels
        live_precip_factor = 1.0
        if precipitation > 0:
            live_precip_factor = 1.0 + precipitation * 8.0  # More responsive than dead fuels

        live_herb = base_live_herb * live_precip_factor
        live_woody = base_live_woody * live_precip_factor

        return {
            "1hr": float(max(1.0, min(40.0, moisture_1hr))),
            "10hr": float(max(2.0, min(45.0, moisture_10hr))),
            "100hr": float(max(3.0, min(50.0, moisture_100hr))),
            "live_herbaceous": float(max(20.0, min(300.0, live_herb))),
            "live_woody": float(max(40.0, min(200.0, live_woody))),
        }

    def list_available_nex_gddp_data(self, data_directory: str) -> Dict[str, Any]:
        """List available NEX-GDDP-CMIP6 data in a directory.

        Args:
            data_directory: Directory to scan for data files

        Returns:
            Dictionary with information about available data
        """
        data_dir = Path(data_directory)
        if not data_dir.exists():
            return {"error": f"Directory not found: {data_directory}"}

        # Find all .tif files that match NEX-GDDP-CMIP6 pattern
        tif_files = list(data_dir.glob("*.ti"))

        models = set()
        experiments = set()
        variables = set()
        years = set()

        valid_files = []

        for file_path in tif_files:
            filename = file_path.name

            # Parse filename: variable_day_model_experiment_variant_gn_year.tif
            parts = filename.replace(".ti", "").split("_")
            if len(parts) >= 7 and parts[1] == "day" and parts[-2] == "gn":
                variable = parts[0]
                model = parts[2]
                experiment = parts[3]
                year_str = parts[-1]

                try:
                    year = int(year_str)
                    variables.add(variable)
                    models.add(model)
                    experiments.add(experiment)
                    years.add(year)
                    valid_files.append(filename)
                except ValueError:
                    continue

        return {
            "directory": str(data_directory),
            "total_files": len(tif_files),
            "valid_nex_files": len(valid_files),
            "models": sorted(models),
            "experiments": sorted(experiments),
            "variables": sorted(variables),
            "years": sorted(years),
            "year_range": f"{min(years)}-{max(years)}" if years else "None",
            "sample_files": valid_files[:5],  # Show first 5 files as examples
        }

    def load_nex_gddp_spatial_scenario(
        self,
        data_directory: str,
        scenario_name: str,
        years: Optional[List[int]] = None,
        spatial_subset: Optional[Dict[str, Union[int, float]]] = None,
        model_name: str = "ACCESS-ESM1-5",
        experiment: str = "historical",
        variant: str = "r1i1p1f1",
    ) -> Dict[str, Any]:
        """Load spatially-explicit weather scenario from NEX-GDDP-CMIP6 data.

        Unlike the standard load_nex_gddp_scenario which creates point-based weather,
        this method preserves spatial structure for landscape-scale simulations.

        Args:
            data_directory: Path to directory containing NEX-GDDP-CMIP6 files
            scenario_name: Name for the created weather scenario
            years: List of years to load (if None, loads all available years)
            spatial_subset: Optional spatial subset specification
            model_name: Climate model name (default: ACCESS-ESM1-5)
            experiment: CMIP6 experiment name (default: historical)
            variant: Model variant identifier (default: r1i1p1f1)

        Returns:
            Dictionary containing spatial weather data and metadata

        Raises:
            ImportError: If rasterio is not available
            FileNotFoundError: If required data files are not found
        """
        if not RASTERIO_AVAILABLE:
            raise ImportError("rasterio is required for spatial NEX-GDDP-CMIP6 data loading")

        logger.info(
            f"Loading spatial NEX-GDDP-CMIP6 scenario '{scenario_name}' from {data_directory}"
        )

        # Find available data files
        data_files = self._find_nex_gddp_files(data_directory, model_name, experiment, variant)

        if not data_files:
            raise FileNotFoundError(f"No NEX-GDDP-CMIP6 files found in {data_directory}")

        # Determine years to load
        available_years = sorted(data_files.keys())
        if years is None:
            years_to_load = available_years[:1]  # Load first year by default for spatial data
        else:
            years_to_load = [y for y in years if y in available_years]
            if not years_to_load:
                raise ValueError(f"None of the requested years {years} are available")

        logger.info(f"Loading spatial data for {len(years_to_load)} years: {years_to_load}")

        # Load spatial data
        metadata = {
            "description": f"Spatial NEX-GDDP-CMIP6 weather data from {model_name}",
            "data_source": "NEX-GDDP-CMIP6",
            "model": model_name,
            "experiment": experiment,
            "variant": variant,
            "years": years_to_load,
            "loaded_at": datetime.now().isoformat(),
            "spatial_subset": spatial_subset,
        }

        # Load first year to get spatial structure
        year = years_to_load[0]
        year_files = data_files[year]

        # Load spatial weather data
        spatial_weather = self._load_nex_gddp_spatial_year(year_files, spatial_subset)

        return {
            "scenario_name": scenario_name,
            "spatial_data": spatial_weather,
            "metadata": metadata,
        }

    def _load_nex_gddp_spatial_year(
        self,
        year_files: Dict[str, str],
        spatial_subset: Optional[Dict[str, Union[int, float]]] = None,
    ) -> Dict[str, np.ndarray]:
        """Load spatial weather data for one year from NEX-GDDP-CMIP6 files.

        Args:
            year_files: Dictionary mapping variable names to file paths
            spatial_subset: Optional spatial subset specification

        Returns:
            Dictionary containing spatial arrays for each variable
        """
        datasets = {}
        spatial_window = None

        try:
            # Open each variable file
            for var, file_path in year_files.items():
                datasets[var] = rasterio.open(file_path)

            # Get reference dataset for spatial info
            ref_dataset = datasets[list(datasets.keys())[0]]

            # Calculate spatial window if subset requested
            if spatial_subset is not None:
                spatial_window = self._calculate_spatial_window(ref_dataset, spatial_subset)

            # Load spatial data for each variable
            spatial_data = {}

            for var, dataset in datasets.items():
                if spatial_window:
                    # Load subset of data (all days)
                    data = dataset.read(window=spatial_window)
                else:
                    # Load all data
                    data = dataset.read()

                # Convert units for this variable
                if var in ["tasmax", "tasmin"]:
                    # Convert Kelvin to Fahrenheit
                    data = (data - 273.15) * 9 / 5 + 32
                elif var == "pr":
                    # Convert kg m-2 s-1 to inches/day
                    data = data * 86400 / 25.4
                elif var == "sfcWind":
                    # Convert m/s to mph
                    data = data * 2.237
                # hurs (humidity) is already in %

                spatial_data[var] = data

            return spatial_data

        finally:
            # Clean up datasets
            for dataset in datasets.values():
                dataset.close()

    def load_nex_gddp_scenario_lazy(
        self,
        data_directory: str,
        scenario_name: str,
        years: Optional[List[int]] = None,
        spatial_subset: Optional[Dict[str, Union[int, float]]] = None,
        model_name: str = "ACCESS-ESM1-5",
        experiment: str = "historical",
        variant: str = "r1i1p1f1",
    ) -> None:
        """Load weather scenario from NEX-GDDP-CMIP6 GeoTIFF files using lazy loading.

        This method creates a lazy-loading scenario that reads daily data on demand
        instead of loading all days into memory at once. Much faster for large datasets.

        Args:
            data_directory: Path to directory containing NEX-GDDP-CMIP6 files
            scenario_name: Name for the created weather scenario
            years: List of years to load (if None, loads all available years)
            spatial_subset: Optional spatial subset definition
            model_name: Climate model name (default: ACCESS-ESM1-5)
            experiment: CMIP6 experiment name (default: historical)
            variant: Model variant identifier (default: r1i1p1f1)

        Raises:
            ImportError: If rasterio is not available
            FileNotFoundError: If required data files are not found
            ValueError: If data files are incompatible or malformed
        """
        if not RASTERIO_AVAILABLE:
            raise ImportError(
                "rasterio is required for NEX-GDDP-CMIP6 data loading. Install with: pip install rasterio"
            )

        logger.info(f"Loading lazy NEX-GDDP-CMIP6 scenario '{scenario_name}' from {data_directory}")

        # Find available data files
        data_files = self._find_nex_gddp_files(data_directory, model_name, experiment, variant)

        if not data_files:
            raise FileNotFoundError(f"No NEX-GDDP-CMIP6 files found in {data_directory}")

        # Determine years to load
        available_years = sorted(data_files.keys())
        if years is None:
            years_to_load = available_years
        else:
            years_to_load = [y for y in years if y in available_years]
            if not years_to_load:
                raise ValueError(
                    f"None of the requested years {years} are available. Available years: {available_years}"
                )

        # Filter data files to only include requested years
        filtered_files = {year: data_files[year] for year in years_to_load}

        logger.info(f"Setting up lazy loading for {len(years_to_load)} years: {years_to_load}")

        # Create lazy scenario
        lazy_scenario = LazyNEXGDDPScenario(
            name=scenario_name,
            year_files=filtered_files,
            spatial_subset=spatial_subset,
            metadata={
                "description": f"Lazy NEX-GDDP-CMIP6 weather scenario from {model_name}",
                "data_source": "NEX-GDDP-CMIP6",
                "model": model_name,
                "experiment": experiment,
                "variant": variant,
                "years": years_to_load,
                "loaded_at": datetime.now().isoformat(),
                "spatial_subset": spatial_subset,
                "lazy_loading": True,
            },
        )

        # Store the lazy scenario with a special marker
        self.scenarios[scenario_name] = lazy_scenario
        logger.info(
            f"Created lazy NEX-GDDP-CMIP6 scenario '{scenario_name}' with {lazy_scenario.get_day_count()} days"
        )

    def split_nex_gddp_files_to_daily(
        self,
        input_directory: str,
        output_directory: str,
        model_name: str = "ACCESS-ESM1-5",
        experiment: str = "historical",
        variant: str = "r1i1p1f1",
    ) -> None:
        """Split yearly NEX-GDDP-CMIP6 files into individual daily files for faster access.

        This is a one-time preprocessing step that dramatically improves performance
        for scenarios that need to access individual days frequently.

        Args:
            input_directory: Directory containing yearly NEX-GDDP-CMIP6 files
            output_directory: Directory to write daily files
            model_name: Climate model name
            experiment: CMIP6 experiment name
            variant: Model variant identifier

        Raises:
            ImportError: If rasterio is not available
            FileNotFoundError: If input files are not found
        """
        if not RASTERIO_AVAILABLE:
            raise ImportError("rasterio is required for file splitting")

        from pathlib import Path

        logger.info(f"Splitting NEX-GDDP-CMIP6 files from {input_directory} to {output_directory}")

        # Create output directory
        output_path = Path(output_directory)
        output_path.mkdir(parents=True, exist_ok=True)

        # Find input files
        data_files = self._find_nex_gddp_files(input_directory, model_name, experiment, variant)

        if not data_files:
            raise FileNotFoundError(f"No NEX-GDDP-CMIP6 files found in {input_directory}")

        total_files_created = 0

        for year, var_files in data_files.items():
            logger.info(f"Processing year {year}...")

            for variable, file_path in var_files.items():
                with rasterio.open(file_path) as src:
                    # Get metadata
                    profile = src.profile.copy()
                    profile.update(
                        {
                            "count": 1,  # Single band per daily file
                            "compress": "lzw",  # Add compression for smaller files
                        }
                    )

                    # Split each day into its own file
                    for day in range(1, src.count + 1):
                        # Create filename: variable_day_model_experiment_variant_gn_year_dayXXX.tif
                        day_filename = f"{variable}_day_{model_name}_{experiment}_{variant}_gn_{year}_day{day:03d}.ti"
                        day_path = output_path / day_filename

                        # Read and write single day
                        data = src.read(day)

                        with rasterio.open(day_path, "w", **profile) as dst:
                            dst.write(data, 1)

                        total_files_created += 1

            logger.info(f"Completed year {year}")

        logger.info(
            f"File splitting complete! Created {total_files_created} daily files in {output_directory}"
        )

    def load_nex_gddp_scenario_from_daily_files(
        self,
        data_directory: str,
        scenario_name: str,
        years: Optional[List[int]] = None,
        spatial_subset: Optional[Dict[str, Union[int, float]]] = None,
        model_name: str = "ACCESS-ESM1-5",
        experiment: str = "historical",
        variant: str = "r1i1p1f1",
    ) -> None:
        """Load weather scenario from daily NEX-GDDP-CMIP6 files for maximum performance.

        This method loads from daily files created by split_nex_gddp_files_to_daily(),
        which provides much faster access than reading bands from yearly files.

        Args:
            data_directory: Path to directory containing daily NEX-GDDP-CMIP6 files
            scenario_name: Name for the created weather scenario
            years: List of years to load (if None, loads all available years)
            spatial_subset: Optional spatial subset definition
            model_name: Climate model name (default: ACCESS-ESM1-5)
            experiment: CMIP6 experiment name (default: historical)
            variant: Model variant identifier (default: r1i1p1f1)

        Raises:
            ImportError: If rasterio is not available
            FileNotFoundError: If required data files are not found
        """
        if not RASTERIO_AVAILABLE:
            raise ImportError("rasterio is required for NEX-GDDP-CMIP6 data loading")

        logger.info(
            f"Loading NEX-GDDP-CMIP6 scenario from daily files '{scenario_name}' from {data_directory}"
        )

        # Find daily files
        daily_files = self._find_nex_gddp_daily_files(
            data_directory, model_name, experiment, variant
        )

        if not daily_files:
            raise FileNotFoundError(f"No daily NEX-GDDP-CMIP6 files found in {data_directory}")

        # Determine years to load
        available_years = sorted(daily_files.keys())
        if years is None:
            years_to_load = available_years
        else:
            years_to_load = [y for y in years if y in available_years]
            if not years_to_load:
                raise ValueError(
                    f"None of the requested years {years} are available. Available years: {available_years}"
                )

        # Filter files to only include requested years
        filtered_files = {year: daily_files[year] for year in years_to_load}

        logger.info(
            f"Setting up daily file loading for {len(years_to_load)} years: {years_to_load}"
        )

        # Create lazy scenario that uses daily files
        lazy_scenario = LazyNEXGDDPScenario(
            name=scenario_name,
            year_files={},  # Empty since we're using daily files
            daily_files=filtered_files,
            spatial_subset=spatial_subset,
            metadata={
                "description": f"Daily-file NEX-GDDP-CMIP6 weather scenario from {model_name}",
                "data_source": "NEX-GDDP-CMIP6",
                "model": model_name,
                "experiment": experiment,
                "variant": variant,
                "years": years_to_load,
                "loaded_at": datetime.now().isoformat(),
                "spatial_subset": spatial_subset,
                "lazy_loading": True,
                "uses_daily_files": True,
            },
        )

        # Mark this scenario as using daily files
        lazy_scenario._uses_daily_files = True

        self.scenarios[scenario_name] = lazy_scenario
        total_days = sum(len(year_data) for year_data in filtered_files.values())
        logger.info(
            f"Created daily-file NEX-GDDP-CMIP6 scenario '{scenario_name}' with {total_days} days"
        )

    def _find_nex_gddp_daily_files(
        self,
        data_directory: str,
        model_name: str,
        experiment: str,
        variant: str,
    ) -> Dict[int, Dict[int, Dict[str, str]]]:
        """Find and organize daily NEX-GDDP-CMIP6 files by year, day, and variable.

        Expected filename format: {variable}_day_{model}_{experiment}_{variant}_gn_{year}_day{day:03d}.tif

        Args:
            data_directory: Directory containing daily files
            model_name: Climate model name
            experiment: CMIP6 experiment name
            variant: Model variant identifier

        Returns:
            Dictionary mapping years -> days -> variables -> file paths
        """
        data_dir = Path(data_directory)
        if not data_dir.exists():
            raise FileNotFoundError(f"Data directory not found: {data_directory}")

        # Required variables
        required_vars = ["tasmax", "tasmin", "hurs", "pr", "sfcWind"]

        # Pattern for daily files
        pattern = f"*_day_{model_name}_{experiment}_{variant}_gn_*_day*.tif"

        files_by_year_day = {}

        for file_path in data_dir.glob(pattern):
            filename = file_path.name

            # Parse filename: variable_day_model_experiment_variant_gn_year_dayXXX.tif
            parts = filename.replace(".ti", "").split("_")
            if len(parts) >= 8:
                variable = parts[0]
                model = parts[2]
                parts[3]
                parts[4]
                year_str = parts[6]
                day_part = parts[7]  # dayXXX

                # Extract year and day numbers
                try:
                    year = int(year_str)
                    day = int(day_part[3:])  # Remove "day" prefix
                except ValueError:
                    logger.warning(f"Could not parse year/day from filename: {filename}")
                    continue

                if variable in required_vars and model == model_name:
                    if year not in files_by_year_day:
                        files_by_year_day[year] = {}
                    if day not in files_by_year_day[year]:
                        files_by_year_day[year][day] = {}
                    files_by_year_day[year][day][variable] = str(file_path)

        # Filter days that have all required variables
        complete_data = {}
        for year, days_data in files_by_year_day.items():
            complete_days = {}
            for day, var_files in days_data.items():
                if all(var in var_files for var in required_vars):
                    complete_days[day] = var_files
                else:
                    missing = [var for var in required_vars if var not in var_files]
                    logger.warning(f"Year {year}, day {day} missing variables: {missing}")

            if complete_days:
                complete_data[year] = complete_days

        total_days = sum(len(year_data) for year_data in complete_data.values())
        logger.info(
            f"Found complete daily data for {len(complete_data)} years, {total_days} total days"
        )
        return complete_data


@dataclass
class LazyNEXGDDPScenario:
    """Lazy-loading weather scenario for NEX-GDDP-CMIP6 data.

    Instead of loading all days into memory, this scenario opens the files
    and reads individual days on demand for much better performance.
    """

    name: str
    year_files: Dict[int, Dict[str, str]]  # year -> {variable: filepath} for yearly files
    metadata: Dict[str, Any] = field(default_factory=dict)
    spatial_subset: Optional[Dict[str, Union[int, float]]] = None

    # Support for daily files (much faster)
    daily_files: Optional[Dict[int, Dict[int, Dict[str, str]]]] = (
        None  # year -> day -> {variable: filepath}
    )
    _uses_daily_files: bool = False

    # Cache for recently accessed days
    _day_cache: Dict[Union[int, str], Dict[str, Any]] = field(default_factory=dict)
    _max_cache_size: int = 10

    def __post_init__(self):
        """Initialize after creation."""
        if not RASTERIO_AVAILABLE:
            raise ImportError("rasterio is required for NEX-GDDP-CMIP6 data loading")

    def get_day_count(self) -> int:
        """Get total number of days available."""
        if self._uses_daily_files and self.daily_files:
            return sum(len(year_data) for year_data in self.daily_files.values())
        elif self.year_files:
            # Check first year to get day count for yearly files
            first_year = min(self.year_files.keys())
            first_files = self.year_files[first_year]
            first_file = next(iter(first_files.values()))

            try:
                with rasterio.open(first_file) as src:
                    days_in_year = src.count
                return len(self.year_files) * days_in_year
            except Exception:
                return 365 * len(self.year_files)  # Fallback estimate
        else:
            return 0

    def get_daily_weather(self, day_index: int) -> Dict[str, Any]:
        """Get weather conditions for a specific day (0-indexed).

        Args:
            day_index: Day index (0-based, across all years)

        Returns:
            Daily weather condition dictionary
        """
        # Check cache first
        if day_index in self._day_cache:
            return self._day_cache[day_index]

        # Get the appropriate file paths and day info
        if self._uses_daily_files and self.daily_files:
            year_files, actual_day = self._get_daily_file_paths(day_index)
            day_band = 1  # Daily files always use band 1
        else:
            year_files, actual_day = self._get_yearly_file_paths(day_index)
            day_band = actual_day  # Use actual day as band number for yearly files

        # Load data for this day
        daily_data = self._load_single_day(year_files, day_band)

        # Convert units and format
        weather_condition = self._convert_nex_gddp_units(daily_data, day_index)

        # Cache the result
        self._cache_day(day_index, weather_condition)

        return weather_condition

    def _get_daily_file_paths(self, day_index: int) -> Tuple[Dict[str, str], int]:
        """Get file paths for a specific day using daily files.

        Args:
            day_index: Global day index

        Returns:
            Tuple of (variable_file_paths, day_number)
        """
        if not self.daily_files:
            raise ValueError("Daily files not available")

        # Find which year and day this index corresponds to
        current_index = 0
        for year in sorted(self.daily_files.keys()):
            year_data = self.daily_files[year]
            if current_index + len(year_data) > day_index:
                # This year contains our target day
                day_offset = day_index - current_index
                sorted_days = sorted(year_data.keys())
                target_day = sorted_days[day_offset]
                return year_data[target_day], target_day
            current_index += len(year_data)

        raise ValueError(f"Day index {day_index} exceeds available data")

    def _get_yearly_file_paths(self, day_index: int) -> Tuple[Dict[str, str], int]:
        """Get file paths for a specific day using yearly files.

        Args:
            day_index: Global day index

        Returns:
            Tuple of (variable_file_paths, day_band_number)
        """
        # Determine which year and day within year
        years = sorted(self.year_files.keys())
        if not years:
            raise ValueError("No years available in scenario")

        # Assume 365-366 days per year, check first year for exact count
        first_year = years[0]
        first_files = self.year_files[first_year]
        first_file = next(iter(first_files.values()))

        with rasterio.open(first_file) as src:
            days_per_year = src.count

        year_index = day_index // days_per_year
        day_in_year = (day_index % days_per_year) + 1  # 1-indexed for rasterio

        if year_index >= len(years):
            raise ValueError(f"Day index {day_index} exceeds available data")

        target_year = years[year_index]
        return self.year_files[target_year], day_in_year

    def get_8hour_weather(self, period_index: int) -> Dict[str, Any]:
        """Get weather conditions for a specific 8-hour period (0-indexed).

        There are 3 periods per day:
        - Period 0 (00:00-08:00): Uses tasmin (coolest part of day)
        - Period 1 (08:00-16:00): Uses tasmax (warmest part of day)
        - Period 2 (16:00-24:00): Uses average of tasmin/tasmax (transition)

        Args:
            period_index: 8-hour period index (0-based, across all years)

        Returns:
            Weather condition dictionary for the 8-hour period
        """
        # Calculate which day this period belongs to
        day_index = period_index // 3
        period_in_day = period_index % 3  # 0, 1, or 2

        # Check cache first (cache by period_index)
        cache_key = f"8hr_{period_index}"
        if cache_key in self._day_cache:
            return self._day_cache[cache_key]

        # Handle daily files vs yearly files
        if self._uses_daily_files and self.daily_files:
            # Get file paths for daily files
            year_files, actual_day = self._get_daily_file_paths(day_index)
            day_band = 1  # Daily files always use band 1
        else:
            # Get file paths for yearly files
            years = sorted(self.year_files.keys())
            if not years:
                raise ValueError("No years available in scenario")

            # Get days per year
            first_year = years[0]
            first_files = self.year_files[first_year]
            first_file = next(iter(first_files.values()))

            with rasterio.open(first_file) as src:
                days_per_year = src.count

            year_index = day_index // days_per_year
            day_in_year = (day_index % days_per_year) + 1  # 1-indexed for rasterio

            if year_index >= len(years):
                raise ValueError(f"Period index {period_index} exceeds available data")

            target_year = years[year_index]
            year_files = self.year_files[target_year]
            day_band = day_in_year

        # Load data for this day
        daily_data = self._load_single_day(year_files, day_band)

        # Convert units and create 8-hour weather condition
        weather_condition = self._convert_nex_gddp_units_8hour(
            daily_data, period_index, period_in_day
        )

        # Cache the result
        self._day_cache[cache_key] = weather_condition

        return weather_condition

    def _load_single_day(self, year_files: Dict[str, str], day_band: int) -> Dict[str, float]:
        """Load data for a single day from all variable files.

        Args:
            year_files: Dictionary mapping variable names to file paths
            day_band: Day band to read (1-indexed, ignored for daily files)

        Returns:
            Dictionary of raw variable values for the day
        """
        daily_data = {}

        for var, file_path in year_files.items():
            try:
                with rasterio.open(file_path) as src:
                    if self.spatial_subset:
                        window = self._calculate_spatial_window(src, self.spatial_subset)
                        if self._uses_daily_files:
                            # Daily files have only one band
                            data = src.read(1, window=window)
                        else:
                            # Yearly files have multiple bands
                            data = src.read(day_band, window=window)
                    else:
                        if self._uses_daily_files:
                            # Daily files have only one band
                            data = src.read(1)
                        else:
                            # Yearly files have multiple bands
                            data = src.read(day_band)

                    # Calculate spatial average if we have spatial data
                    if data.size > 1:
                        daily_data[var] = float(np.nanmean(data))
                    else:
                        daily_data[var] = float(data.flat[0])

            except Exception as e:
                logger.warning(f"Error reading {var} for day {day_band}: {e}")
                # Use default values for missing data
                defaults = {
                    "tasmax": 288.15,  # ~15°C in Kelvin
                    "tasmin": 283.15,  # ~10°C in Kelvin
                    "hurs": 50.0,  # 50% humidity
                    "pr": 0.0,  # No precipitation
                    "sfcWind": 2.0,  # 2 m/s wind
                }
                daily_data[var] = defaults.get(var, 0.0)

        return daily_data

    def _calculate_spatial_window(
        self,
        dataset: "rasterio.DatasetReader",
        spatial_subset: Dict[str, Union[int, float]],
    ) -> "Window":
        """Calculate spatial window for subsetting rasterio data."""
        if "row_start" in spatial_subset:
            # Pixel-based subset
            row_start = spatial_subset["row_start"]
            row_end = spatial_subset["row_end"]
            col_start = spatial_subset["col_start"]
            col_end = spatial_subset["col_end"]

            height = row_end - row_start
            width = col_end - col_start

            return Window(col_start, row_start, width, height)

        elif "north" in spatial_subset:
            # Geographic bounds subset
            north = spatial_subset["north"]
            south = spatial_subset["south"]
            east = spatial_subset["east"]
            west = spatial_subset["west"]

            # Convert geographic coordinates to pixel coordinates
            transform = dataset.transform

            # Get pixel coordinates
            col_start, row_start = ~transform * (west, north)
            col_end, row_end = ~transform * (east, south)

            # Ensure integer pixel coordinates
            col_start = max(0, int(col_start))
            row_start = max(0, int(row_start))
            col_end = min(dataset.width, int(col_end))
            row_end = min(dataset.height, int(row_end))

            width = col_end - col_start
            height = row_end - row_start

            return Window(col_start, row_start, width, height)

        else:
            raise ValueError(
                "Spatial subset must specify either pixel coordinates or geographic bounds"
            )

    def _convert_nex_gddp_units(
        self, daily_data: Dict[str, float], day_index: int
    ) -> Dict[str, Any]:
        """Convert NEX-GDDP-CMIP6 data units to weather module format."""
        # Temperature conversion: Kelvin to Fahrenheit
        # Use tasmax as the daily temperature
        temp_k = daily_data.get("tasmax", 288.15)  # Default ~15°C if missing
        temp_f = (temp_k - 273.15) * 9 / 5 + 32

        # Relative humidity (already in %)
        rh = daily_data.get("hurs", 50.0)
        rh = max(1.0, min(100.0, rh))  # Clamp to valid range

        # Precipitation: kg m-2 s-1 to inches/day
        pr_rate = daily_data.get("pr", 0.0)  # kg m-2 s-1
        pr_mm_per_day = pr_rate * 86400  # Convert to mm/day
        pr_inches = pr_mm_per_day / 25.4  # Convert to inches

        # Wind speed: m/s to mph
        wind_ms = daily_data.get("sfcWind", 2.0)  # Default 2 m/s if missing
        wind_mph = wind_ms * 2.237  # 1 m/s = 2.237 mph

        # Estimate wind direction (not provided in NEX-GDDP-CMIP6)
        # Use a simple seasonal pattern
        day_of_year = day_index % 365
        wind_dir = 225 + 45 * np.sin(2 * np.pi * day_of_year / 365)  # Seasonal variation

        # Calculate fuel moistures based on weather conditions
        fuel_moistures = self._estimate_fuel_moistures_from_weather(temp_f, rh, pr_inches, wind_mph)

        return {
            "temperature": float(temp_f),
            "relative_humidity": float(rh),
            "wind_speed": float(wind_mph),
            "wind_direction": float(wind_dir),
            "precipitation": float(pr_inches),
            "fuel_moistures": fuel_moistures,
        }

    def _estimate_fuel_moistures_from_weather(
        self,
        temperature: float,
        humidity: float,
        precipitation: float,
        wind_speed: float,
    ) -> Dict[str, float]:
        """Estimate fuel moistures from basic weather variables."""
        # Base fuel moistures from temperature and humidity using EMC relationships
        temp_c = (temperature - 32) * 5 / 9  # Convert to Celsius

        # Calculate equilibrium moisture content (simplified Simard equation)
        humidity / 100.0
        emc = 0.18 * (21.1 - 0.39 * temp_c + 0.0183 * temp_c**2) * (1.0 - np.exp(-0.115 * humidity))
        emc = max(2.0, min(30.0, emc))  # Reasonable bounds

        # Adjust for precipitation
        precip_factor = 1.0
        if precipitation > 0:
            if precipitation < 0.1:
                precip_factor = 1.0 + precipitation * 5.0  # Light rain
            elif precipitation < 0.5:
                precip_factor = 1.5 + (precipitation - 0.1) * 7.5  # Moderate rain
            else:
                precip_factor = 4.5 + (precipitation - 0.5) * 10.0  # Heavy rain

        # Base moistures scaled from EMC
        moisture_1hr = emc * precip_factor
        moisture_10hr = emc * 1.2 * precip_factor
        moisture_100hr = emc * 1.5 * precip_factor

        # Live fuel moistures - more responsive to recent precipitation and seasonal patterns
        base_live_herb = 60.0 + 20.0 * (humidity - 50.0) / 50.0  # 40-80% base range
        base_live_woody = 80.0 + 15.0 * (humidity - 50.0) / 50.0  # 65-95% base range

        # Strong precipitation response for live fuels
        live_precip_factor = 1.0
        if precipitation > 0:
            live_precip_factor = 1.0 + precipitation * 8.0  # More responsive than dead fuels

        live_herb = base_live_herb * live_precip_factor
        live_woody = base_live_woody * live_precip_factor

        return {
            "1hr": float(max(1.0, min(40.0, moisture_1hr))),
            "10hr": float(max(2.0, min(45.0, moisture_10hr))),
            "100hr": float(max(3.0, min(50.0, moisture_100hr))),
            "live_herbaceous": float(max(20.0, min(300.0, live_herb))),
            "live_woody": float(max(40.0, min(200.0, live_woody))),
        }

    def _cache_day(self, day_index: Union[int, str], weather_data: Dict[str, Any]) -> None:
        """Cache a day's weather data."""
        # Remove oldest entries if cache is full
        if len(self._day_cache) >= self._max_cache_size:
            oldest_key = min(self._day_cache.keys(), key=lambda x: str(x))
            del self._day_cache[oldest_key]

        self._day_cache[day_index] = weather_data

    def _convert_nex_gddp_units_8hour(
        self,
        daily_data: Dict[str, float],
        period_index: int,
        period_in_day: int,
    ) -> Dict[str, Any]:
        """Convert NEX-GDDP-CMIP6 data units to weather module format for 8-hour periods.

        Args:
            daily_data: Raw daily data from NEX-GDDP-CMIP6
            period_index: Global period index
            period_in_day: Period within day (0=early, 1=mid, 2=late)

        Returns:
            Converted 8-hour weather condition
        """
        # Temperature selection based on period
        if period_in_day == 0:
            # Early period (00:00-08:00): Use minimum temperature
            temp_k = daily_data.get("tasmin", 283.15)  # ~10°C if missing
        elif period_in_day == 1:
            # Mid period (08:00-16:00): Use maximum temperature
            temp_k = daily_data.get("tasmax", 293.15)  # ~20°C if missing
        else:
            # Late period (16:00-24:00): Use average temperature
            tasmin = daily_data.get("tasmin", 283.15)
            tasmax = daily_data.get("tasmax", 293.15)
            temp_k = (tasmin + tasmax) / 2

        # Convert temperature: Kelvin to Fahrenheit
        temp_f = (temp_k - 273.15) * 9 / 5 + 32

        # Relative humidity varies throughout the day
        base_rh = daily_data.get("hurs", 50.0)
        if period_in_day == 0:
            # Early morning: higher humidity
            rh = base_rh * 1.1
        elif period_in_day == 1:
            # Midday: lower humidity
            rh = base_rh * 0.85
        else:
            # Evening: moderate humidity
            rh = base_rh * 0.95

        rh = max(1.0, min(100.0, rh))  # Clamp to valid range

        # Precipitation: keep same for all periods in a day
        pr_rate = daily_data.get("pr", 0.0)  # kg m-2 s-1
        pr_mm_per_day = pr_rate * 86400  # Convert to mm/day
        pr_inches = pr_mm_per_day / 25.4  # Convert to inches

        # Wind speed varies throughout the day
        base_wind_ms = daily_data.get("sfcWind", 2.0)
        if period_in_day == 0:
            # Early morning: calmer winds
            wind_ms = base_wind_ms * 0.7
        elif period_in_day == 1:
            # Midday: stronger winds
            wind_ms = base_wind_ms * 1.2
        else:
            # Evening: moderate winds
            wind_ms = base_wind_ms * 0.9

        wind_mph = wind_ms * 2.237  # Convert to mph

        # Wind direction with diurnal variation
        day_of_year = (period_index // 3) % 365
        base_dir = 225 + 45 * np.sin(2 * np.pi * day_of_year / 365)

        # Add diurnal wind direction shift
        if period_in_day == 0:
            # Early morning: slight shift
            wind_dir = (base_dir + 15) % 360
        elif period_in_day == 1:
            # Midday: standard direction
            wind_dir = base_dir % 360
        else:
            # Evening: opposite shift
            wind_dir = (base_dir - 15) % 360

        # Calculate fuel moistures based on weather conditions
        fuel_moistures = self._estimate_fuel_moistures_from_weather(temp_f, rh, pr_inches, wind_mph)

        return {
            "temperature": float(temp_f),
            "relative_humidity": float(rh),
            "wind_speed": float(wind_mph),
            "wind_direction": float(wind_dir),
            "precipitation": float(pr_inches),
            "fuel_moistures": fuel_moistures,
            "period_in_day": period_in_day,  # Track which 8-hour period this is
            "time_of_day": ["early", "mid", "late"][period_in_day],
        }

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary representation.

        Note: Lazy scenarios cannot be easily serialized since they don't
        store all daily conditions in memory.

        Returns:
            Dictionary representation of scenario metadata

        Raises:
            NotImplementedError: Lazy scenarios cannot be fully serialized
        """
        raise NotImplementedError(
            "Lazy scenarios cannot be exported to JSON since they don't store "
            "all daily conditions in memory. Use the original load_nex_gddp_scenario() "
            "method if you need to export scenario data."
        )
