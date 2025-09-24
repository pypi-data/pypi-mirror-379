"""Ignition Module implementation.

Provides classes and functions for simulating fire ignitions
with multiple ignition sources, escape probability, and TensorFlow sampling.
"""

from dataclasses import dataclass, field
from typing import Any, Dict, Optional

import numpy as np

from ..state.representation import StateRepresentation


@dataclass
class IgnitionModule:
    """Simulates fire ignitions across the landscape.

    Features:
    - Multiple ignition sources
    - Escape probability
    - Spatial and temporal patterns (daily distribution)
    """

    ignition_sources: Dict[str, Dict[str, Any]] = field(default_factory=dict)
    escape_probability: float = 0.2
    random_seed: Optional[int] = None
    _rng: np.random.Generator = field(init=False)

    def __post_init__(self):
        """Initialize after dataclass creation."""
        self._rng = np.random.default_rng(self.random_seed)

    def add_ignition_source(
        self,
        name: str,
        annual_count: int,
        probability_surface: Optional[Any] = None,
        daily_distribution: Optional[Dict[int, float]] = None,
    ) -> None:
        """Add an ignition source.

        Args:
            name: Name of the ignition source
            annual_count: Average annual number of ignitions
            probability_surface: Spatial probability surface for ignitions (optional, NumPy array)
            daily_distribution: Daily distribution of ignitions (dict mapping day-of-year to fraction, optional)
        """
        self.ignition_sources[name] = {
            "annual_count": annual_count,
            "probability_surface": probability_surface,
            "daily_distribution": daily_distribution or {},
        }

    def generate_ignitions(
        self, state: StateRepresentation, day_of_year: Optional[int] = None
    ) -> np.ndarray:
        """Generate ignitions for a time period.

        Args:
            state: Landscape state
            day_of_year: Day of year for ignition generation (1-366), or None for annual

        Returns:
            Boolean NumPy array indicating ignition locations
        """
        grid_shape = state.grid_shape
        ignitions = np.zeros(grid_shape, dtype=bool)

        for source_name, source in self.ignition_sources.items():
            annual_count = source["annual_count"]
            # Adjust count based on day_of_year if specified
            if day_of_year is not None and source["daily_distribution"]:
                daily_fraction = source["daily_distribution"].get(day_of_year, 1.0 / 366.0)
                count = int(annual_count * daily_fraction)
            else:
                count = annual_count
            # Convert probability_surface to numpy if needed
            prob_surface = source["probability_surface"]
            if hasattr(prob_surface, "numpy"):
                prob_surface = prob_surface.numpy()
            # Generate ignitions for this source
            source_ignitions = self._generate_source_ignitions(state, count, prob_surface)
            ignitions = ignitions | source_ignitions
        # Apply escape probability
        ignitions = self._apply_escape_probability(ignitions)
        # Set ignitions as a state variable (as np.ndarray)
        state.set_variable("ignitions", ignitions.astype(np.int8))
        return ignitions

    def _generate_source_ignitions(
        self,
        state: StateRepresentation,
        count: int,
        probability_surface: Optional[Any],
    ) -> np.ndarray:
        """Generate ignitions for a single source.

        Args:
            state: Landscape state
            count: Number of ignitions to generate
            probability_surface: Spatial probability surface (optional, NumPy array)

        Returns:
            Boolean array indicating ignition locations
        """
        grid_shape = state.grid_shape
        ignitions = np.zeros(grid_shape, dtype=bool)
        if count <= 0:
            return ignitions
        # If probability_surface is a tf.Tensor, convert to numpy
        if hasattr(probability_surface, "numpy"):
            probability_surface = probability_surface.numpy()
        # If no probability surface, use uniform distribution
        if probability_surface is None:
            flat_indices = self._rng.choice(
                grid_shape[0] * grid_shape[1], size=count, replace=False
            )
            row_indices, col_indices = np.unravel_index(flat_indices, grid_shape)
        else:
            if probability_surface.shape != grid_shape:
                raise ValueError(
                    f"Probability surface shape {probability_surface.shape} "
                    f"doesn't match grid shape {grid_shape}"
                )
            prob_flat = probability_surface.flatten()
            prob_sum = prob_flat.sum()
            if prob_sum > 0:
                prob_flat = prob_flat / prob_sum
            else:
                prob_flat = np.ones_like(prob_flat) / len(prob_flat)
            flat_indices = self._rng.choice(len(prob_flat), size=count, replace=False, p=prob_flat)
            row_indices, col_indices = np.unravel_index(flat_indices, grid_shape)
        ignitions[row_indices, col_indices] = True
        return ignitions

    def _apply_escape_probability(self, ignitions: np.ndarray) -> np.ndarray:
        """Apply escape probability to ignitions.

        Args:
            ignitions: Boolean array of ignition locations

        Returns:
            Boolean array of escaped ignition locations
        """
        if self.escape_probability >= 1.0:
            return ignitions
        if self.escape_probability <= 0.0:
            return np.zeros_like(ignitions)
        ignition_indices = np.where(ignitions)
        n_ignitions = len(ignition_indices[0])
        if n_ignitions == 0:
            return ignitions
        escapes = self._rng.random(n_ignitions) < self.escape_probability
        escaped_ignitions = np.zeros_like(ignitions)
        escaped_ignitions[ignition_indices[0][escapes], ignition_indices[1][escapes]] = True
        return escaped_ignitions

    def apply_to_state(self, state, state_tracker=None, day_of_year=None):
        """Orchestrator-compatible method to generate and record ignitions for the current year.
        Args:
            state: Landscape state
            state_tracker: AnnualStateTracker instance (required)
            day_of_year: Day of year for ignition generation (1-366), or None for annual
        """
        return self.generate_ignitions(state, day_of_year)
