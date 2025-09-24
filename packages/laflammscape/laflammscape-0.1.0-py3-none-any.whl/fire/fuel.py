"""Fuel Mapping Module implementation.

Provides classes and functions for mapping vegetation types to fire behavior
fuel models with NumPy optimization and custom fuel model support.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Set

import numpy as np

from ..state.representation import StateRepresentation


@dataclass
class FuelMappingModule:
    """Maps vegetation to fire behavior fuel models.

    Features:
    - NumPy optimization
    - Custom fuel models
    - Nonburnable persistence
    """

    nonburnable_values: Set[int] = field(default_factory=lambda: {91, 92, 93, 98, 99})
    state_id_to_idx: Dict[int, str] = field(default_factory=dict)
    states_data: List[StateRepresentation] = field(default_factory=list)
    fuel_model_id_to_idx: Dict[int, str] = field(default_factory=dict)
    state_idx_to_fuel_model_idx: Dict[int, int] = field(default_factory=dict)

    def __post_init__(self):
        # Convert each state dict to StateRepresentation
        for state in self.states_data:
            # Map state ID to fuel type
            if state.fuel_type in self.fuel_model_id_to_idx:
                self.state_idx_to_fuel_model_idx[self.state_id_to_idx[state.state_id]] = (
                    self.fuel_model_id_to_idx[state.fuel_type]
                )
            else:
                print(f"missing fuel model: {state.fuel_type} for state: {state.state_id}")
                self.state_idx_to_fuel_model_idx[self.state_id_to_idx[state.state_id]] = (
                    99  # nonburnable
                )
        print(f"state_idx_to_fuel_model_idx: {self.state_idx_to_fuel_model_idx}")

    def map_fuels(self, state: StateRepresentation, output_variable: str = "fuel_model") -> None:
        """Map vegetation to fuel models in the state using NumPy ops.
        Args:
            state: State to update with fuel models
            output_variable: Name to use for the fuel model variable in state
        """
        state_data = state.get_variable("eco_state")
        if not isinstance(state_data, np.ndarray):
            state_data = np.array(state_data)
        # Vectorized mapping
        vectorized_map = np.vectorize(lambda x: self.state_idx_to_fuel_model_idx[x])
        fuel_models = vectorized_map(state_data)
        state.set_variable(output_variable, fuel_models)

    def apply_to_state(self, state, **_kwargs):
        """Orchestrator-compatible method to map fuels in the state."""
        # First map the fuel models to the grid
        self.map_fuels(state)
