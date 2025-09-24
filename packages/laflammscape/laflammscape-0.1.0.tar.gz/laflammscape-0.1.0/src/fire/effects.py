"""Fire Effects Module implementation.

Provides classes and functions for modeling fire effects including:
- Fuel consumption and emissions
- Soil burn severity
- Species response modeling
- Ecological effects assessment
"""

import logging
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Tuple

import numpy as np

from ..state.representation import StateRepresentation

# Setup logging
logger = logging.getLogger("laflammscape.fire.effects")


@dataclass
class SoilBurnSeverity:
    """Represents soil burn severity levels.
    
    Based on USDA Forest Service soil burn severity categories:
    - Unburned: No visible soil effects
    - Low: Minimal soil heating, some organic matter consumption
    - Moderate: Moderate soil heating, significant organic matter loss
    - High: Severe soil heating, complete organic matter consumption
    """
    
    UNBURNED = 0
    LOW = 1
    MODERATE = 2
    HIGH = 3
    
    @classmethod
    def from_flame_length(cls, flame_length: float) -> int:
        """Determine soil burn severity from flame length.
        
        Args:
            flame_length: Flame length in meters
            
        Returns:
            Soil burn severity level (0-3)
        """
        if flame_length <= 0:
            return cls.UNBURNED
        elif flame_length <= 0.5:
            return cls.LOW
        elif flame_length <= 1.5:
            return cls.MODERATE
        else:
            return cls.HIGH


@dataclass
class FuelEmissionsModel:
    """Models fuel consumption and emissions from fire.
    
    Features:
    - Fuel type-specific consumption rates
    - Emission factors for various pollutants
    - Carbon accounting
    - Smoke production estimates
    """
    
    # Fuel consumption rates (kg/m²) by fuel type
    consumption_rates: Dict[str, float] = field(default_factory=lambda: {
        "grass": 0.5,
        "shrub": 1.2,
        "timber": 2.0,
        "litter": 0.3,
        "duff": 1.5
    })
    
    # Emission factors (g/kg fuel consumed)
    emission_factors: Dict[str, Dict[str, float]] = field(default_factory=lambda: {
        "CO2": {"grass": 1500, "shrub": 1600, "timber": 1700, "litter": 1400, "duff": 1500},
        "CO": {"grass": 50, "shrub": 60, "timber": 80, "litter": 40, "duff": 50},
        "CH4": {"grass": 2, "shrub": 3, "timber": 4, "litter": 1, "duff": 2},
        "PM2.5": {"grass": 8, "shrub": 12, "timber": 15, "litter": 6, "duff": 8}
    })
    
    def calculate_emissions(self, fuel_type: str, burned_area: float, 
                            flame_length: float) -> Dict[str, float]:
        """Calculate emissions for a given fuel type and burned area.
        
        Args:
            fuel_type: Type of fuel burned
            burned_area: Area burned in m²
            flame_length: Flame length in meters
            
        Returns:
            Dictionary of emissions by pollutant (kg)
        """
        if fuel_type not in self.consumption_rates:
            logger.warning(f"Unknown fuel type: {fuel_type}")
            return {}
        
        # Adjust consumption based on flame length (higher flames = more consumption)
        base_consumption = self.consumption_rates[fuel_type]
        flame_factor = min(2.0, max(0.5, flame_length / 1.0))  # 0.5x to 2.0x multiplier
        adjusted_consumption = base_consumption * flame_factor
        
        # Calculate total fuel consumed
        total_fuel_consumed = adjusted_consumption * burned_area
        
        # Calculate emissions
        emissions = {}
        for pollutant, factors in self.emission_factors.items():
            if fuel_type in factors:
                emissions[pollutant] = total_fuel_consumed * factors[fuel_type] / 1000  # Convert to kg
        
        return emissions


@dataclass
class SoilEffectsModel:
    """Models soil effects from fire including heating and organic matter loss.
    
    Features:
    - Soil temperature modeling
    - Organic matter consumption
    - Nutrient cycling effects
    - Erosion risk assessment
    """
    
    # Soil heating parameters
    max_soil_temp: float = 200.0  # Maximum soil temperature (°C)
    heating_depth: float = 0.1  # Depth of significant heating (m)
    
    # Organic matter loss rates by burn severity
    organic_matter_loss: Dict[int, float] = field(default_factory=lambda: {
        0: 0.0,      # Unburned
        1: 0.1,      # Low severity
        2: 0.3,      # Moderate severity  
        3: 0.6       # High severity
    })
    
    def calculate_soil_effects(self, burn_severity: int, soil_depth: float = 0.1) -> Dict[str, float]:
        """Calculate soil effects from burn severity.
        
        Args:
            burn_severity: Soil burn severity level (0-3)
            soil_depth: Depth of soil layer (m)
            
        Returns:
            Dictionary of soil effects
        """
        effects = {
            "organic_matter_loss": self.organic_matter_loss.get(burn_severity, 0.0),
            "max_temperature": self.max_soil_temp * (burn_severity / 3.0),
            "heating_depth": self.heating_depth * (1 + burn_severity * 0.2),
            "nutrient_loss": burn_severity * 0.2,  # Simplified nutrient loss
            "erosion_risk": min(1.0, burn_severity * 0.3)  # Erosion risk factor
        }
        
        return effects


@dataclass
class SpeciesResponseModel:
    """Models species response to fire effects.
    
    Features:
    - Species-specific fire tolerance
    - Mortality and regeneration rates
    - Habitat suitability changes
    - Community composition shifts
    """
    
    # Species fire tolerance levels (0-1, where 1 = highly fire tolerant)
    species_tolerance: Dict[str, float] = field(default_factory=lambda: {
        "ponderosa_pine": 0.8,
        "douglas_fir": 0.3,
        "lodgepole_pine": 0.9,
        "whitebark_pine": 0.7,
        "aspen": 0.6,
        "oak": 0.8,
        "grass": 0.9,
        "shrub": 0.5
    })
    
    # Mortality rates by burn severity and species
    mortality_rates: Dict[str, Dict[int, float]] = field(default_factory=lambda: {
        "ponderosa_pine": {0: 0.0, 1: 0.1, 2: 0.3, 3: 0.7},
        "douglas_fir": {0: 0.0, 1: 0.2, 2: 0.6, 3: 0.9},
        "lodgepole_pine": {0: 0.0, 1: 0.05, 2: 0.2, 3: 0.5},
        "whitebark_pine": {0: 0.0, 1: 0.1, 2: 0.4, 3: 0.8},
        "aspen": {0: 0.0, 1: 0.1, 2: 0.3, 3: 0.6},
        "oak": {0: 0.0, 1: 0.05, 2: 0.2, 3: 0.5},
        "grass": {0: 0.0, 1: 0.1, 2: 0.3, 3: 0.8},
        "shrub": {0: 0.0, 1: 0.2, 2: 0.5, 3: 0.9}
    })
    
    def calculate_species_mortality(self, species: str, burn_severity: int) -> float:
        """Calculate mortality rate for a species given burn severity.
        
        Args:
            species: Species name
            burn_severity: Soil burn severity level (0-3)
            
        Returns:
            Mortality rate (0-1)
        """
        if species not in self.mortality_rates:
            logger.warning(f"Unknown species: {species}")
            return 0.0
        
        return self.mortality_rates[species].get(burn_severity, 0.0)
    
    def calculate_habitat_suitability(self, species: str, burn_severity: int, 
                                   time_since_fire: int) -> float:
        """Calculate habitat suitability for a species after fire.
        
        Args:
            species: Species name
            burn_severity: Soil burn severity level (0-3)
            time_since_fire: Years since fire
            
        Returns:
            Habitat suitability (0-1)
        """
        if species not in self.species_tolerance:
            return 0.5  # Default moderate suitability
        
        base_tolerance = self.species_tolerance[species]
        
        # Adjust for burn severity (high severity reduces suitability)
        severity_factor = 1.0 - (burn_severity * 0.2)
        
        # Adjust for time since fire (recovery over time)
        recovery_factor = min(1.0, time_since_fire / 10.0)  # Full recovery in 10 years
        
        suitability = base_tolerance * severity_factor * recovery_factor
        return max(0.0, min(1.0, suitability))


class FireEffectsModule:
    """Main module for calculating fire effects across the landscape.
    
    Features:
    - Integrated effects modeling
    - Landscape-scale calculations
    - State variable updates
    - Effects reporting
    """
    
    def __init__(self):
        """Initialize the fire effects module."""
        self.emissions_model = FuelEmissionsModel()
        self.soil_model = SoilEffectsModel()
        self.species_model = SpeciesResponseModel()
        
    def calculate_effects(self, state: StateRepresentation, 
                         flame_lengths: np.ndarray,
                         fuel_types: np.ndarray) -> Dict[str, Any]:
        """Calculate fire effects for the entire landscape.
        
        Args:
            state: Landscape state
            flame_lengths: 2D array of flame lengths
            fuel_types: 2D array of fuel type codes
            
        Returns:
            Dictionary of calculated effects
        """
        effects = {
            "emissions": {},
            "soil_effects": {},
            "species_effects": {},
            "total_burned_area": 0.0,
            "average_flame_length": 0.0
        }
        
        # Find burned areas
        burned_mask = flame_lengths > 0
        if not np.any(burned_mask):
            return effects
        
        # Calculate total burned area
        cell_area = 1.0  # Assume 1 m² per cell for now
        total_burned_area = np.sum(burned_mask) * cell_area
        effects["total_burned_area"] = total_burned_area
        effects["average_flame_length"] = np.mean(flame_lengths[burned_mask])
        
        # Calculate emissions by fuel type
        unique_fuel_types = np.unique(fuel_types[burned_mask])
        for fuel_type in unique_fuel_types:
            fuel_mask = (fuel_types == fuel_type) & burned_mask
            fuel_burned_area = np.sum(fuel_mask) * cell_area
            avg_flame_length = np.mean(flame_lengths[fuel_mask])
            
            emissions = self.emissions_model.calculate_emissions(
                str(fuel_type), fuel_burned_area, avg_flame_length
            )
            effects["emissions"][str(fuel_type)] = emissions
        
        # Calculate soil effects by burn severity
        burn_severities = np.zeros_like(flame_lengths, dtype=np.int32)
        for i in range(flame_lengths.shape[0]):
            for j in range(flame_lengths.shape[1]):
                if burned_mask[i, j]:
                    burn_severities[i, j] = SoilBurnSeverity.from_flame_length(flame_lengths[i, j])
        
        unique_severities = np.unique(burn_severities[burned_mask])
        for severity in unique_severities:
            severity_mask = (burn_severities == severity) & burned_mask
            severity_area = np.sum(severity_mask) * cell_area
            
            soil_effects = self.soil_model.calculate_soil_effects(severity)
            effects["soil_effects"][f"severity_{severity}"] = {
                "area": severity_area,
                "effects": soil_effects
            }
        
        return effects
    
    def update_state_variables(self, state: StateRepresentation, 
                              effects: Dict[str, Any]) -> None:
        """Update state variables based on calculated effects.
        
        Args:
            state: Landscape state to update
            effects: Calculated fire effects
        """
        # Update soil organic matter if not already present
        if "soil_organic_matter" not in state.state_variables:
            grid_shape = state.grid_shape
            initial_organic_matter = np.full(grid_shape, 0.5, dtype=np.float32)
            state.set_variable("soil_organic_matter", initial_organic_matter)
        
        # Update habitat suitability if not already present
        if "habitat_suitability" not in state.state_variables:
            grid_shape = state.grid_shape
            initial_suitability = np.full(grid_shape, 0.8, dtype=np.float32)
            state.set_variable("habitat_suitability", initial_suitability)
        
        # Log effects for monitoring
        logger.info(f"Fire effects calculated: {effects['total_burned_area']:.1f} m² burned")
        logger.info(f"Average flame length: {effects['average_flame_length']:.2f} m")
