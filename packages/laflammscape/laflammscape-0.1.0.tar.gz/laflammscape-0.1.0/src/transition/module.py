"""State Transition Module implementation.

Provides classes and functions for state transitions with probabilistic
transitions, rule validation, and TensorFlow optimization.
"""

import enum
import logging
from typing import Any, Dict, Optional

import numpy as np
from pydantic import BaseModel, Field, field_validator, model_validator

from ..fire.behavior import FuelModel
from ..state.representation import StateRepresentation

# Setup logging
logger = logging.getLogger("laflammscape.transition")


class Severity(enum.Enum):
    VERY_LOW = 0
    LOW = 1
    MEDIUM = 2
    HIGH = 3


class Thresholds(BaseModel):
    very_low_max: Optional[float] = Field(
        None, description="Max flame length for VERY_LOW severity."
    )
    low_max: Optional[float] = Field(None, description="Max flame length for LOW severity.")
    medium_max: Optional[float] = Field(
        None,
        description="Max flame length for MEDIUM severity. Anything above this is considered HIGH.",
    )

    @field_validator("very_low_max", "low_max", "medium_max", mode="before")
    @classmethod
    def check_threshold_values(cls, v: Any):
        if v is None:
            return v
        if isinstance(v, (int, float)) and v < 0:
            raise ValueError("Threshold values must be non-negative")
        return v

    @model_validator(mode="after")
    def check_threshold_order(self) -> "Thresholds":
        if (
            self.low_max is not None
            and self.very_low_max is not None
            and self.low_max <= self.very_low_max
        ):
            raise ValueError("low_max must be greater than very_low_max")
        if (
            self.medium_max is not None
            and self.low_max is not None
            and self.medium_max < self.low_max
        ):
            raise ValueError("medium_max must be greater than or equal to low_max")
        return self


class StateConfiguration(BaseModel):
    state_id: str = Field(..., description="Unique identifier for the state (e.g., 'CDC-2A')")
    pathway: str = Field(..., description="Pathway group ('CDC' or 'CMC')")
    state_label: str = Field(..., description="State label ('1A', '2B', etc.)")
    description: Optional[str] = Field(
        None,
        description="Full description from Figure 4 (e.g., 'PFBG (NB9)', 'SI (TL4)')",
    )
    fuel_type: Optional[str] = Field(
        None,
        description="Fuel type code (e.g., NB9, TL4, GS1) extracted from description.",
    )
    canopy_cover: Optional[float] = Field(None, alias="CC", description="Canopy Cover (%)")
    canopy_height: Optional[float] = Field(
        None, alias="CH", description="Canopy Height (e.g., meters)"
    )
    canopy_base_height: Optional[float] = Field(
        None, alias="CBH", description="Canopy Base Height (e.g., meters)"
    )
    canopy_bulk_density: Optional[float] = Field(
        None, alias="CBD", description="Canopy Bulk Density (e.g., kg/m^3)"
    )
    min_age: Optional[int] = Field(
        None, description="Minimum age (years) for this state in this pathway"
    )
    max_age: Optional[int] = Field(
        None, description="Maximum age (years) for this state in this pathway"
    )
    thresholds: Thresholds = Field(
        ...,
        description="Flame length thresholds defining severity levels for fire transitions.",
    )
    fire_destinations: Dict[Severity, Optional[str]] = Field(
        default_factory=dict,
        description="Destination state_id for LOW, MEDIUM, HIGH severity fire transitions.",
    )
    non_fire_succession_destination: Optional[str] = Field(
        None,
        description="Destination state_id if age > max_age and no fire occurs.",
    )
    burned_state_succession_destination: Optional[str] = Field(
        None,
        description="Destination state_id if age > max_age and Very Low fire occurs.",
    )

    @field_validator("fire_destinations", mode="before")
    @classmethod
    def convert_fire_destination_keys(cls, v: Any):
        if not isinstance(v, dict):
            return v
        converted_dict = {}
        name_map = {member.name: member for member in Severity}
        value_map = {str(member.value): member for member in Severity}
        for key_str, dest_id in v.items():
            if key_str in name_map:
                converted_dict[name_map[key_str]] = dest_id
            elif key_str in value_map:
                converted_dict[value_map[key_str]] = dest_id
            else:
                converted_dict[key_str] = dest_id
        return converted_dict

    @model_validator(mode="after")
    def check_state_and_age(self) -> "StateConfiguration":
        if not isinstance(self.state_id, str) or "-" not in self.state_id:
            raise ValueError("state_id format 'PATHWAY-LABEL' required")
        if "-" in self.state_id:
            pathway_from_id = self.state_id.split("-", 1)[0]
            if self.pathway is not None and self.pathway != pathway_from_id:
                raise ValueError(
                    f"Pathway in state_id '{pathway_from_id}' does not match pathway field '{self.pathway}'"
                )
        if self.max_age is not None and self.min_age is not None and self.max_age < self.min_age:
            raise ValueError("max_age must be >= min_age")
        return self


class StateTransitionModel(BaseModel):
    states: Dict[str, StateConfiguration] = Field(
        ..., description="Dictionary mapping state_id to its configuration."
    )

    def get_state_config(self, state_id: str) -> Optional[StateConfiguration]:
        return self.states.get(state_id)


def get_severity_level(flame_length: float, thresholds: Thresholds) -> Severity:
    if thresholds.very_low_max is None:
        return Severity.VERY_LOW
    if flame_length <= thresholds.very_low_max:
        return Severity.VERY_LOW
    if thresholds.low_max is None:
        return Severity.VERY_LOW
    if flame_length <= thresholds.low_max:
        return Severity.LOW
    if thresholds.medium_max is None:
        return Severity.VERY_LOW
    if thresholds.medium_max == thresholds.low_max:
        return Severity.HIGH
    else:
        if flame_length <= thresholds.medium_max:
            return Severity.MEDIUM
        else:
            return Severity.HIGH


class StateTransitionModule:
    """Manages transitions between landscape states using TensorFlow tensors for fast transitions."""

    def __init__(
        self,
        model: StateTransitionModel,
        state_variable: str = "eco_state",
        age_variable: str = "age",
        flame_length_variable: str = "fire_flame_length",
        fuel_models: Dict[str, FuelModel] = {},
    ):
        self.model = model
        self.state_variable = state_variable
        self.age_variable = age_variable
        self.flame_length_variable = flame_length_variable
        self.fuel_models = fuel_models
        self._random_seed = None
        self._rng = np.random.default_rng()
        # Build state ID <-> index mapping
        self.state_ids = list(model.states.keys())
        self.state_id_to_idx = {sid: i for i, sid in enumerate(self.state_ids)}
        self.idx_to_state_id = {i: sid for i, sid in enumerate(self.state_ids)}

        # Initialize spatial growth rate modifiers (will be set when first applied to state)
        self._growth_rate_modifiers = None
        self._growth_rate_initialized = False

        self.fire_dest_arr = np.full((len(self.idx_to_state_id), 4), -1, dtype=np.int32)
        for idx in range(len(self.idx_to_state_id)):
            config = self.model.get_state_config(self.idx_to_state_id[idx])
            if config:
                for sev in [Severity.LOW, Severity.MEDIUM, Severity.HIGH]:
                    dest_id = config.fire_destinations.get(sev, None)
                    if dest_id is not None and dest_id in self.state_id_to_idx:
                        self.fire_dest_arr[idx, sev.value] = self.state_id_to_idx[dest_id]

        self.burned_succ_arr = np.full(len(self.idx_to_state_id), -1, dtype=np.int32)
        self.nonfire_succ_arr = np.full(len(self.idx_to_state_id), -1, dtype=np.int32)
        for idx in range(len(self.idx_to_state_id)):
            config = self.model.get_state_config(self.idx_to_state_id[idx])
            if config:
                if (
                    config.burned_state_succession_destination
                    and config.burned_state_succession_destination in self.state_id_to_idx
                ):
                    self.burned_succ_arr[idx] = self.state_id_to_idx[
                        config.burned_state_succession_destination
                    ]
                else:
                    self.burned_succ_arr[idx] = idx
                if (
                    config.non_fire_succession_destination
                    and config.non_fire_succession_destination in self.state_id_to_idx
                ):
                    self.nonfire_succ_arr[idx] = self.state_id_to_idx[
                        config.non_fire_succession_destination
                    ]
                else:
                    self.nonfire_succ_arr[idx] = idx
            else:
                print("no config for idx", idx)
        print(self.fire_dest_arr)
        print(self.burned_succ_arr)
        print(self.nonfire_succ_arr)

        # Initialize NumPy functions for vectorized operations
        self._init_np_functions()

    def _init_np_functions(self):
        """Initialize NumPy functions for vectorized operations."""

        def process_state_np(
            state_idx,
            ages,
            flame_lengths,
            max_age_arr,
            fire_dest_arr,
            burned_succ_arr,
            nonfire_succ_arr,
            thresholds,
            burned_in_current_state,
        ):
            # Fire transition logic
            very_low_mask = (flame_lengths <= thresholds["very_low_max"]) & (flame_lengths > 0)
            low_mask = (flame_lengths > thresholds["very_low_max"]) & (
                flame_lengths <= thresholds["low_max"]
            )
            medium_mask = (flame_lengths > thresholds["low_max"]) & (
                flame_lengths <= thresholds["medium_max"]
            )
            high_mask = flame_lengths > thresholds["medium_max"]

            # Convert masks to severity indices
            severity_indices = np.full_like(state_idx, -1, dtype=np.int32)
            severity_indices = np.where(very_low_mask, 0, severity_indices)
            severity_indices = np.where(low_mask, 1, severity_indices)
            severity_indices = np.where(medium_mask, 2, severity_indices)
            severity_indices = np.where(high_mask, 3, severity_indices)
            print(f"severity_indices: {np.unique(flame_lengths)}")
            print(f"severity counts: {np.bincount(severity_indices[severity_indices >= 0])}")
            print(f"unique states: {np.unique(state_idx)}")

            # Clamp or mask invalid indices
            severity_indices = np.where(
                (severity_indices >= 0) & (severity_indices < fire_dest_arr.shape[1]),
                severity_indices,
                0,
            )
            vectorized_fire_destinations = np.vectorize(lambda x, y: fire_dest_arr[x, y])
            # Get fire destinations based on severity
            fire_destinations = vectorized_fire_destinations(state_idx, severity_indices)
            print(f"unique fire destinations: {np.unique(fire_destinations)}")

            # Succession logic - use burn state tracking instead of current flame length
            age_mask = ages > max_age_arr[state_idx]

            print(f"burned_succ: {np.sum(age_mask & burned_in_current_state)}")
            print(f"nonfire_succ: {np.sum(age_mask)}")
            print(f"fire_destinations: {np.sum(fire_destinations != -1)}")

            # Combine fire and succession transitions
            next_state = np.where(
                age_mask & burned_in_current_state,  # burned succession based on burn history
                burned_succ_arr[state_idx],
                np.where(
                    age_mask,  # any other age-out
                    nonfire_succ_arr[state_idx],
                    np.where(
                        fire_destinations != -1,
                        fire_destinations,
                        state_idx,  # fallback to current state
                    ),
                ),
            )
            return next_state

        self.process_state_np = process_state_np

    def _initialize_growth_rate_modifiers(self, state: StateRepresentation) -> None:
        """Initialize spatial growth rate modifiers based on environmental factors.

        Creates a persistent grid of growth rate modifiers that account for:
        - Elevation effects (slower growth at high elevations)
        - Slope effects (slower growth on steep slopes)
        - Aspect effects (north-facing slopes grow slower)
        - Random spatial variation (site quality differences)

        This creates realistic spatial heterogeneity in aging rates.
        """
        if self._growth_rate_initialized:
            return

        grid_shape = state.grid_shape

        # Get terrain data if available
        elevation = (
            state.get_variable("elevation")
            if state.has_variable("elevation")
            else np.zeros(grid_shape)
        )
        slope = state.get_variable("slope") if state.has_variable("slope") else np.zeros(grid_shape)
        aspect = (
            state.get_variable("aspect")
            if state.has_variable("aspect")
            else np.full(grid_shape, 180.0)
        )  # Default south-facing

        # Initialize growth rate modifiers (1.0 = normal growth rate)
        growth_modifiers = np.ones(grid_shape, dtype=np.float32)

        # Elevation effect: slower growth at high elevations
        if np.max(elevation) > np.min(elevation):
            elev_norm = (elevation - np.min(elevation)) / (np.max(elevation) - np.min(elevation))
            # High elevation penalty: 0.8-1.0 growth rate (20% slower at highest elevations)
            elevation_factor = 1.0 - 0.2 * elev_norm
            growth_modifiers *= elevation_factor

        # Slope effect: slower growth on steep slopes
        if np.max(slope) > 0:
            # Steep slope penalty: 0.9-1.0 growth rate (10% slower on steepest slopes)
            slope_factor = 1.0 - 0.1 * np.clip(slope / 45.0, 0, 1)  # Normalize to 45 degrees
            growth_modifiers *= slope_factor

        # Aspect effect: north-facing slopes grow slower in northern hemisphere
        # Convert aspect to growth modifier (south=180° is optimal)
        aspect_radians = np.deg2rad(aspect)
        # Cosine of difference from south (180°), scaled to 0.9-1.1 range
        south_radians = np.deg2rad(180.0)
        aspect_factor = 1.0 + 0.1 * np.cos(aspect_radians - south_radians)
        growth_modifiers *= aspect_factor

        # Add random spatial variation for site quality (±10% variation)
        # Use spatial autocorrelation to create realistic patches
        from scipy.ndimage import gaussian_filter

        random_variation = self._rng.normal(0.0, 0.1, grid_shape)
        # Smooth to create spatial patches of similar site quality
        smooth_variation = gaussian_filter(random_variation, sigma=2.0)
        site_quality_factor = 1.0 + smooth_variation
        growth_modifiers *= site_quality_factor

        # Ensure reasonable bounds: 0.6 to 1.4 (40% slower to 40% faster)
        growth_modifiers = np.clip(growth_modifiers, 0.6, 1.4)

        self._growth_rate_modifiers = growth_modifiers
        self._growth_rate_initialized = True

        print(
            f"Initialized growth rate modifiers: {np.min(growth_modifiers):.3f} to {np.max(growth_modifiers):.3f}"
        )
        print(f"Mean growth rate: {np.mean(growth_modifiers):.3f}")
        print(f"Growth rate std: {np.std(growth_modifiers):.3f}")

    def _apply_heterogeneous_aging(self, ages: np.ndarray) -> np.ndarray:
        """Apply spatially heterogeneous aging based on growth rate modifiers.

        Instead of adding 1 year to all cells, add variable amounts based on
        local growth rates to create natural spatial variation in aging.
        """
        if self._growth_rate_modifiers is None:
            # Fallback to uniform aging if modifiers not initialized
            return ages + 1

        # Calculate age increments: some cells age faster/slower than others
        # Base increment is 1 year, modified by growth rate
        age_increments = self._growth_rate_modifiers

        # Add random annual variation (±5% year-to-year variation)
        annual_variation = self._rng.normal(1.0, 0.05, ages.shape)
        age_increments = age_increments * annual_variation

        # Apply age increments (most cells get ~1 year, but with variation)
        new_ages = ages + age_increments

        # Ensure ages are positive and reasonable
        new_ages = np.maximum(new_ages, 0)

        return new_ages

    def _compute_thresholds(self, state_idx_grid):
        """Compute threshold arrays for each severity level based on the state configuration of each pixel."""
        # Create arrays for each threshold
        very_low_max = np.zeros_like(state_idx_grid, dtype=np.float32)
        low_max = np.zeros_like(state_idx_grid, dtype=np.float32)
        medium_max = np.zeros_like(state_idx_grid, dtype=np.float32)

        # For each unique state index, get the thresholds from the state configuration
        for state_idx in np.unique(state_idx_grid):
            mask = state_idx_grid == state_idx
            state_id = self.idx_to_state_id[state_idx]
            state_config = self.model.get_state_config(state_id)
            if state_config and state_config.thresholds:
                very_low_max[mask] = (
                    state_config.thresholds.very_low_max
                    if state_config.thresholds.very_low_max is not None
                    else (
                        state_config.thresholds.low_max
                        if state_config.thresholds.low_max is not None
                        else (
                            state_config.thresholds.medium_max
                            if state_config.thresholds.medium_max is not None
                            else 0.0
                        )
                    )
                )
                low_max[mask] = (
                    state_config.thresholds.low_max
                    if state_config.thresholds.low_max is not None
                    else (
                        state_config.thresholds.medium_max
                        if state_config.thresholds.medium_max is not None
                        else 1.0
                    )
                )
                medium_max[mask] = (
                    state_config.thresholds.medium_max
                    if state_config.thresholds.medium_max is not None
                    else 2.0
                )
            else:
                print(f"no thresholds for state {state_id}")
                # Default values if state config not found
                very_low_max[mask] = 0.0
                low_max[mask] = 1.0
                medium_max[mask] = 2.0
        return {
            "very_low_max": very_low_max,
            "low_max": low_max,
            "medium_max": medium_max,
        }

    def apply_to_state(self, state: StateRepresentation) -> None:
        # Initialize growth rate modifiers on first call
        if not self._growth_rate_initialized:
            self._initialize_growth_rate_modifiers(state)

        # Initialize burn state tracking if not present
        state.initialize_burn_state_tracking()

        # Get current state, age, and flame length arrays as numpy arrays
        state_idx_grid = state.get_variable(self.state_variable)
        ages = state.get_variable(self.age_variable)
        flame_lengths = (
            state.get_variable(self.flame_length_variable)
            if self.flame_length_variable in state.state_variables
            else None
        )
        burned_in_current_state = state.get_variable("burned_in_current_state")

        # Mark cells that have burned (any flame length > 0)
        if flame_lengths is not None:
            fire_mask = flame_lengths > 0
            state.mark_burned_cells(fire_mask)
            burned_in_current_state = state.get_variable("burned_in_current_state")

        # Prepare lookup tables for thresholds and destinations
        max_age_arr = np.array(
            [
                (
                    self.model.get_state_config(self.idx_to_state_id[idx]).max_age
                    if self.model.get_state_config(self.idx_to_state_id[idx])
                    and self.model.get_state_config(self.idx_to_state_id[idx]).max_age is not None
                    else np.iinfo(np.int32).max
                )
                for idx in range(len(self.idx_to_state_id))
            ],
            dtype=np.int32,
        )
        min_age_arr = np.array(
            [
                (
                    self.model.get_state_config(self.idx_to_state_id[idx]).min_age
                    if self.model.get_state_config(self.idx_to_state_id[idx])
                    and self.model.get_state_config(self.idx_to_state_id[idx]).min_age is not None
                    else 0
                )
                for idx in range(len(self.idx_to_state_id))
            ],
            dtype=np.int32,
        )

        # Debug logging for age thresholds
        print("\nAge debug:")
        print(f"Current ages range: {np.min(ages):.1f} to {np.max(ages):.1f}")
        print(f"Max ages for states: {max_age_arr}")
        print(f"Min ages for states: {min_age_arr}")

        # Compute thresholds based on state configuration
        thresholds = self._compute_thresholds(state_idx_grid)

        if flame_lengths is not None:
            flame_lengths_np = flame_lengths
        else:
            flame_lengths_np = np.zeros_like(state_idx_grid, dtype=np.float32)

        # Process the entire grid using NumPy vectorization
        next_state_idx_grid = self.process_state_np(
            state_idx_grid,
            ages,
            flame_lengths_np,
            max_age_arr,
            self.fire_dest_arr,
            self.burned_succ_arr,
            self.nonfire_succ_arr,
            thresholds,
            burned_in_current_state,
        )
        next_state_idx_grid = np.where(
            next_state_idx_grid == -1, state_idx_grid, next_state_idx_grid
        )

        # Apply heterogeneous aging instead of uniform +1 increment
        ages = self._apply_heterogeneous_aging(ages)

        # Reset age for cells that are transitioning to new states
        transition_mask = next_state_idx_grid != state_idx_grid
        if np.any(transition_mask):
            # Reset their age to the min age of their new state
            updated_ages = np.where(transition_mask, min_age_arr[next_state_idx_grid], ages)
        else:
            updated_ages = ages

        # Reset burn state tracking for cells that are transitioning to new states
        transition_mask = next_state_idx_grid != state_idx_grid
        if np.any(transition_mask):
            state.reset_burn_state_tracking(transition_mask)

        # Debug logging for transitions
        print(f"Cells transitioning: {np.sum(next_state_idx_grid != state_idx_grid)}")
        print(f"Updated ages range: {np.min(updated_ages):.1f} to {np.max(updated_ages):.1f}")
        print(f"New states: {np.unique(next_state_idx_grid)}")

        # Set the new state grid and updated ages
        state.set_variable(self.state_variable, next_state_idx_grid)
        state.set_variable(self.age_variable, updated_ages)

    def indices_to_state_ids(self, grid):
        # Map integer indices to state ID strings using NumPy vectorization
        state_id_array = np.array(
            [self.idx_to_state_id[i] for i in range(len(self.idx_to_state_id))],
            dtype=object,
        )
        return state_id_array[grid]

    def state_ids_to_indices(self, grid):
        # Map state ID strings to integer indices using NumPy vectorization
        # Build a mapping from state ID string to index
        state_id_to_idx = self.state_id_to_idx
        # Vectorize the mapping
        vectorized_map = np.vectorize(lambda x: state_id_to_idx.get(x, -1))
        return vectorized_map(grid)

    def get_state_id_grid(self, state: StateRepresentation):
        idx_grid = state.get_variable(self.state_variable)
        return self.indices_to_state_ids(idx_grid)

    def set_random_seed(self, seed: int) -> None:
        self._random_seed = seed
        self._rng = np.random.default_rng(seed)
