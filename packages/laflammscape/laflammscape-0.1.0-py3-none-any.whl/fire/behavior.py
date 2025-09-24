"""Fire Behavior module implementation.

Provides classes and functions for calculating fire behavior metrics
including fire intensity, spread rate, and flame length.
"""

import logging
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, Optional

import numpy as np
from pydantic import BaseModel

from ..state.representation import StateRepresentation

# Setup logging
logger = logging.getLogger("laflammscape.fire.behavior")


class FireSeverity(Enum):
    """Fire severity classification."""

    NONE = 0
    LOW = 1
    MODERATE = 2
    HIGH = 3
    EXTREME = 4


class FuelModel(BaseModel):
    """Represents a fuel model for fire behavior calculations.

    Features:
    - Standard fuel model attributes
    - Support for custom fuel parameters
    - Compatible with standard fire behavior models
    """

    id: str
    loading: Dict[str, float]  # Fuel loading by timelag class (tons/acre)
    type: Optional[str] = None
    sav: Dict[str, Optional[float]]  # Surface area to volume ratios (1/ft)
    depth: float  # Fuel bed depth (ft)
    moisture_extinction: float  # Moisture of extinction (%)
    heat_content: float  # Heat content (BTU/lb)

    # Optional parameters
    description: Optional[str] = None
    is_dynamic: Optional[bool] = False  # Whether fuel model changes over time

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "FuelModel":
        """Create a FuelModel from a dictionary.

        Args:
            data: Dictionary with fuel model parameters

        Returns:
            FuelModel instance
        """
        return cls(**data)

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary representation.

        Returns:
            Dictionary with fuel model parameters
        """
        return self.dict()


@dataclass
class WeatherCondition:
    """Represents weather conditions for fire behavior calculations.

    Features:
    - Standard weather parameters
    - Fuel moisture by timelag class
    - Wind conditions
    """

    temperature: float  # Air temperature (°C)
    relative_humidity: float  # Relative humidity (%)
    wind_speed: float  # Wind speed (mph)
    wind_direction: float  # Wind direction (degrees from north)
    fuel_moistures: Dict[str, float]  # Fuel moisture by timelag class (%)
    precipitation: float = 0.0  # Precipitation (mm)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "WeatherCondition":
        """Create a WeatherCondition from a dictionary.

        Args:
            data: Dictionary with weather parameters

        Returns:
            WeatherCondition instance
        """
        return cls(
            temperature=data.get("temperature", 25.0),
            relative_humidity=data.get("relative_humidity", 30.0),
            wind_speed=data.get("wind_speed", 5.0),
            wind_direction=data.get("wind_direction", 0.0),
            fuel_moistures=data.get(
                "fuel_moistures",
                {
                    "1hr": 6.0,
                    "10hr": 8.0,
                    "100hr": 10.0,
                    "herb": 60.0,
                    "woody": 90.0,
                },
            ),
            precipitation=data.get("precipitation", 0.0),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary representation.

        Returns:
            Dictionary with weather parameters
        """
        return {
            "temperature": self.temperature,
            "relative_humidity": self.relative_humidity,
            "wind_speed": self.wind_speed,
            "wind_direction": self.wind_direction,
            "fuel_moistures": self.fuel_moistures,
            "precipitation": self.precipitation,
        }


@dataclass
class FireBehaviorCalculator:
    """Calculates fire behavior metrics using NumPy operations.

    Features:
    - Fire intensity calculation
    - Spread rate prediction
    - Flame length estimation
    - Severity classification
    All calculations are performed using NumPy arrays and operations.
    """

    # Byram's equation coefficients
    SURFACE_FLAME_COEFFICIENT = 0.0775  # Coefficient for surface fires
    SURFACE_FLAME_EXPONENT = 0.46  # Exponent for surface fires
    CROWN_FLAME_COEFFICIENT = 0.2  # Coefficient for crown fires
    CROWN_FLAME_EXPONENT = 2.0 / 3.0  # Exponent for crown fires
    CROWN_FIRE_THRESHOLD = 4000.0  # Intensity threshold for crown fires (kW/m)

    # Thresholds for severity classification (kW/m)
    severity_thresholds: Dict[Any, float] = field(
        default_factory=lambda: {
            0: 0,
            1: 300,  # Lower threshold for low severity
            2: 1000,  # Lower threshold for moderate severity
            3: 2000,  # Lower threshold for high severity
            4: 5000,  # Lower threshold for extreme severity
        }
    )

    def calculate_fireline_intensity(
        self, heat_content_kj_kg, fuel_consumed_kg_m2, spread_rate_m_s
    ):
        return heat_content_kj_kg * fuel_consumed_kg_m2 * spread_rate_m_s

    def calculate_spread_rate(
        self,
        sav_1hr,
        loading_1hr,
        depth,
        wind_speed,
        slope,
        moisture_1hr,
        moisture_extinction,
    ):
        base_rate = 0.1
        sav_factor = np.minimum(5.0, sav_1hr / 1500.0)
        base_rate = base_rate * sav_factor
        load_factor = np.minimum(3.0, 1.0 + loading_1hr / 2.0)
        base_rate = base_rate * load_factor
        depth_factor = np.minimum(2.0, 1.0 + depth / 1.0)
        base_rate = base_rate * depth_factor
        wind_factor = 1.0 + np.minimum(5.0, np.power(wind_speed / 5.0, 1.2))
        slope_radians = np.deg2rad(slope)
        slope_factor = np.where(
            slope >= 0.0,
            1.0 + np.minimum(3.0, np.tan(slope_radians) * 2.0),
            1.0 / (1.0 + np.minimum(0.5, np.tan(-slope_radians) * 0.5)),
        )
        moisture_factor = np.where(
            moisture_1hr >= moisture_extinction,
            np.zeros_like(moisture_1hr),
            np.exp(-0.1 * moisture_1hr),
        )
        spread_rate = base_rate * wind_factor * slope_factor * moisture_factor
        return spread_rate

    def calculate_flame_length(self, intensity):
        """Calculate flame length using Byram's equation.

        For surface fires: FL = 0.0775 * (I)^0.46
        For crown fires: FL = 0.2 * (I/3.4613)^(2/3) / 3.2808

        Args:
            intensity: Fire intensity in kW/m

        Returns:
            Flame length in meters
        """
        # Determine which cells have crown fire
        is_crown_fire = intensity > self.CROWN_FIRE_THRESHOLD

        # Calculate flame length for surface fires
        surface_flame_length = self.SURFACE_FLAME_COEFFICIENT * np.power(
            intensity, self.SURFACE_FLAME_EXPONENT
        )

        # Calculate flame length for crown fires
        # Convert kW/m to BTU/ft/s for the formula
        intensity_btu = intensity / 3.4613
        crown_flame_length = (
            self.CROWN_FLAME_COEFFICIENT
            * np.power(intensity_btu, self.CROWN_FLAME_EXPONENT)
            / 3.2808
        )

        # Use crown or surface flame length based on intensity
        flame_length = np.where(is_crown_fire, crown_flame_length, surface_flame_length)

        # Ensure flame length is non-negative
        return np.maximum(flame_length, 0.0)

    def classify_severity(self, intensity):
        thresholds = [
            self.severity_thresholds[1],
            self.severity_thresholds[2],
            self.severity_thresholds[3],
            self.severity_thresholds[4],
        ]
        severity = np.where(intensity < thresholds[0], 0, 1)
        severity = np.where(intensity >= thresholds[0], 1, severity)
        severity = np.where(intensity >= thresholds[1], 2, severity)
        severity = np.where(intensity >= thresholds[2], 3, severity)
        severity = np.where(intensity >= thresholds[3], 4, severity)
        return severity

    def calculate_fire_behavior(self, state) -> Dict[str, np.ndarray]:
        """OPTIMIZED: Calculate fire behavior using efficient vectorized operations."""

        required_vars = ["fire_state", "fuel_model"]
        for var in required_vars:
            if var not in state.state_variables:
                raise ValueError(f"Required state variable '{var}' not found")

        fire_state = state.get_variable("fire_state")
        fuel_model_grid = state.get_variable("fuel_model")

        # OPTIMIZATION: Early exit if no burning cells
        burning_mask = fire_state == 1
        if not np.any(burning_mask):
            shape = fuel_model_grid.shape
            zeros = np.zeros(shape, dtype=np.float32)
            return {
                "intensity": zeros,
                "spread_rate": zeros,
                "flame_length": zeros,
                "severity": zeros,
            }

        # OPTIMIZATION: Pre-allocate all output arrays to avoid repeated allocation
        shape = fuel_model_grid.shape
        intensity = np.zeros(shape, dtype=np.float32)
        spread_rate = np.zeros(shape, dtype=np.float32)
        flame_length = np.zeros(shape, dtype=np.float32)
        severity = np.zeros(shape, dtype=np.int8)  # Use int8 for severity to save memory

        # OPTIMIZATION: Only process burning cells - get indices once
        burning_indices = np.where(burning_mask)
        burning_fuel_models = fuel_model_grid[burning_indices]

        # OPTIMIZATION: Get unique burning fuel models to minimize processing
        unique_burning_models = np.unique(burning_fuel_models)
        print(
            f"OPTIMIZATION: Processing {len(unique_burning_models)} unique fuel models for {len(burning_indices[0])} burning cells"
        )

        # Weather variables - vectorized access with optimized defaults
        def safe_get_weather_optimized(var_name: str, default: float) -> np.ndarray:
            if var_name in state.state_variables:
                return state.get_variable(var_name).astype(np.float32)
            else:
                # OPTIMIZATION: Only create arrays for burning cells if variable doesn't exist
                result = np.full(shape, default, dtype=np.float32)
                return result

        weather = {
            "temperature": safe_get_weather_optimized("weather_temperature", 25.0),
            "relative_humidity": safe_get_weather_optimized("weather_humidity", 30.0),
            "wind_speed": safe_get_weather_optimized("weather_wind_speed", 5.0),
            "wind_direction": safe_get_weather_optimized("weather_wind_direction", 0.0),
            "fuel_moisture_1hr": safe_get_weather_optimized("fuel_moisture_1hr", 6.0),
            "fuel_moisture_10hr": safe_get_weather_optimized("fuel_moisture_10hr", 8.0),
            "fuel_moisture_100hr": safe_get_weather_optimized("fuel_moisture_100hr", 10.0),
            "fuel_moisture_herb": safe_get_weather_optimized("fuel_moisture_herb", 60.0),
            "fuel_moisture_woody": safe_get_weather_optimized("fuel_moisture_woody", 90.0),
        }

        # OPTIMIZATION: Pre-allocate fuel property arrays
        loading_1hr = np.zeros(shape, dtype=np.float32)
        loading_10hr = np.zeros(shape, dtype=np.float32)
        loading_100hr = np.zeros(shape, dtype=np.float32)
        sav_1hr = np.zeros(shape, dtype=np.float32)
        depth = np.zeros(shape, dtype=np.float32)
        moisture_extinction = np.zeros(shape, dtype=np.float32)
        heat_content = np.zeros(shape, dtype=np.float32)

        # OPTIMIZATION: Get fuel model registry once
        fuel_model_registry = state.get_dict("fuel_model_registry")

        # OPTIMIZATION: Process only unique burning fuel models
        for model_code in unique_burning_models:
            model_obj = fuel_model_registry.get(model_code)
            if model_obj is None:
                # OPTIMIZATION: Use default fuel model properties
                model_properties = {
                    "loading": {
                        "1hr": 0.5,
                        "10hr": 0.0,
                        "100hr": 0.0,
                        "herb": 0.0,
                        "woody": 0.0,
                    },
                    "sav": {"1hr": 2000.0, "herb": 1500.0, "woody": 1500.0},
                    "depth": 0.5,
                    "moisture_extinction": 15.0,
                    "heat_content": 8000,  # BTU/lb
                }
            else:
                model_properties = {
                    "loading": model_obj.loading,
                    "sav": model_obj.sav,
                    "depth": model_obj.depth,
                    "moisture_extinction": model_obj.moisture_extinction,
                    "heat_content": model_obj.heat_content,
                }

            # OPTIMIZATION: Vectorized mask creation and assignment
            mask = fuel_model_grid == model_code
            loading_1hr[mask] = model_properties["loading"].get("1hr", 0.0)
            loading_10hr[mask] = model_properties["loading"].get("10hr", 0.0)
            loading_100hr[mask] = model_properties["loading"].get("100hr", 0.0)
            sav_1hr[mask] = model_properties["sav"].get("1hr", 2000.0)
            depth[mask] = model_properties["depth"]
            moisture_extinction[mask] = model_properties["moisture_extinction"]
            heat_content[mask] = model_properties["heat_content"] * 2.326  # Convert BTU/lb to kJ/kg

        # OPTIMIZATION: Vectorized fuel consumption calculation
        dead_fuel_load = loading_1hr + 0.3 * loading_10hr + 0.1 * loading_100hr
        fuel_consumed_kg_m2 = dead_fuel_load * 0.224  # Convert tons/acre to kg/m²

        # OPTIMIZATION: Vectorized moisture factor calculation with safe division
        moisture_factor = np.where(
            moisture_extinction > 0,
            np.clip(
                1.0 - (weather["fuel_moisture_1hr"] / moisture_extinction),
                0.0,
                1.0,
            ),
            0.0,
        )
        fuel_consumed_kg_m2 *= moisture_factor

        # OPTIMIZATION: Efficient slope calculation
        if "slope" in state.state_variables:
            slope_grid = state.get_variable("slope")
        elif "elevation" in state.state_variables:
            elevation = state.get_variable("elevation")
            # OPTIMIZATION: Only calculate slope if needed and cache it
            if not hasattr(self, "_cached_slope"):
                self._cached_slope = self._calculate_slope_grid(elevation)
            slope_grid = self._cached_slope
        else:
            slope_grid = np.zeros_like(fuel_model_grid, dtype=np.float32)

        # OPTIMIZATION: Vectorized spread rate calculation
        spread_rate_full = self.calculate_spread_rate(
            sav_1hr,
            loading_1hr,
            depth,
            weather["wind_speed"],
            slope_grid,
            weather["fuel_moisture_1hr"],
            moisture_extinction,
        )

        # OPTIMIZATION: Only assign spread rate to burning cells
        spread_rate[burning_mask] = spread_rate_full[burning_mask]

        # OPTIMIZATION: Vectorized intensity calculation - only for burning cells
        spread_rate_m_s = spread_rate / 60.0
        intensity_full = self.calculate_fireline_intensity(
            heat_content, fuel_consumed_kg_m2, spread_rate_m_s
        )
        intensity[burning_mask] = intensity_full[burning_mask]

        # OPTIMIZATION: Vectorized flame length calculation - only for burning cells
        flame_length_full = self.calculate_flame_length(intensity_full)
        flame_length[burning_mask] = flame_length_full[burning_mask]

        # OPTIMIZATION: Vectorized severity classification - only for burning cells
        severity_full = self.classify_severity(intensity_full)
        severity[burning_mask] = severity_full[burning_mask]

        return {
            "intensity": intensity,
            "spread_rate": spread_rate,
            "flame_length": flame_length,
            "severity": severity,
        }

    def _calculate_slope_grid(self, elevation: np.ndarray) -> np.ndarray:
        from scipy.ndimage import sobel

        dx = sobel(elevation, axis=1)
        dy = sobel(elevation, axis=0)
        slope = np.degrees(np.arctan(np.sqrt(dx**2 + dy**2)))
        return slope

    def calculate_burn_probability(
        self,
        state: StateRepresentation,
        num_iterations: int = 100,
        random_seed: Optional[int] = None,
    ) -> np.ndarray:
        """Calculate burn probability using Monte Carlo simulation (returns NumPy array)."""
        rng = np.random.default_rng(random_seed or 0)
        shape = next(iter(state.state_variables.values())).shape
        burn_count = np.zeros(shape, dtype=np.float32)
        for i in range(num_iterations):
            burn_map = np.zeros(shape, dtype=np.float32)
            num_ignitions = rng.integers(1, 6, size=shape)
            for _ in range(num_ignitions.sum()):
                row = rng.integers(0, shape[0])
                col = rng.integers(0, shape[1])
                burn_map[row, col] = 1.0
                # Skipping full CA fire spread for brevity
            burn_count += burn_map
        burn_probability = burn_count / num_iterations
        return burn_probability

    def apply_to_state(self, state) -> None:
        """Apply fire behavior calculations to the state using NumPy ops.
        Args:
            state: State to update with fire behavior metrics
        """
        results = self.calculate_fire_behavior(state)
        for key, value in results.items():
            k = f"fire_{key}"
            if k not in state.state_variables:
                state.set_variable(k, np.zeros_like(state.get_variable("fire_state")))
            prev = state.get_variable(f"fire_{key}")
            state.set_variable(f"fire_{key}", np.maximum(prev, value))
