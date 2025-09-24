from typing import Optional

import numpy as np
import pandas as pd
import rasterio

from ..state.representation import StateRepresentation


class SpatiotemporalIgnitionModule:
    """
    Advanced ignition module using spatiotemporal distributions:
    - Annual ignition count from probability distribution
    - Julian day distribution for temporal placement
    - Kernel density GeoTIFF for spatial placement
    - Optionally resample to avoid duplicate ignitions in the same cell
    """

    def __init__(
        self,
        julian_day_csv: str,
        count_dist_csv: str,
        spatial_tif: str,
        random_seed: Optional[int] = None,
        resample_on_duplicate: bool = True,
    ):
        self.julian_day_df = pd.read_csv(julian_day_csv)
        self.count_dist_df = pd.read_csv(count_dist_csv)
        self.spatial_tif_path = spatial_tif
        self.random_seed = random_seed
        self.resample_on_duplicate = resample_on_duplicate
        self._rng = np.random.default_rng(random_seed)
        # Load spatial probability surface
        with rasterio.open(spatial_tif) as src:
            self.spatial_prob = src.read(1)
            self.spatial_transform = src.transform
            self.spatial_shape = self.spatial_prob.shape
        # Normalize spatial probability
        total = self.spatial_prob.sum()
        if total > 0:
            self.spatial_prob = self.spatial_prob / total
        else:
            self.spatial_prob = np.ones_like(self.spatial_prob) / np.prod(self.spatial_prob.shape)
        # Prepare temporal probability
        self.julian_probs = self.julian_day_df["probability"].values
        self.julian_days = self.julian_day_df["DISCOVERY_DOY"].values
        # Prepare count probability
        self.counts = self.count_dist_df["ignitions"].values
        self.count_probs = self.count_dist_df["probability"].values

    def generate_ignitions(self, state: StateRepresentation) -> np.ndarray:
        """
        Generate ignitions for the year and set in the state.
        Returns an integer array: 0 = no ignition, N = Julian day of ignition.
        """
        grid_shape = state.grid_shape
        ignitions = np.zeros(grid_shape, dtype=np.int16)
        # Sample number of ignitions
        n_ignitions = self._rng.choice(self.counts, p=self.count_probs)
        if n_ignitions == 0:
            state.set_variable("ignitions", ignitions)
            return ignitions
        # Sample Julian days
        sampled_days = self._rng.choice(self.julian_days, size=n_ignitions, p=self.julian_probs)
        # Sample spatial locations
        prob_flat = self.spatial_prob.flatten()
        n_cells = self.spatial_prob.size
        if self.resample_on_duplicate:
            # Resample until all locations are unique
            max_attempts = 1000
            for _ in range(max_attempts):
                flat_indices = self._rng.choice(
                    n_cells, size=n_ignitions, replace=False, p=prob_flat
                )
                if len(set(flat_indices)) == n_ignitions:
                    break
            else:
                raise RuntimeError(
                    "Could not sample unique ignition locations after many attempts."
                )
        else:
            flat_indices = self._rng.choice(n_cells, size=n_ignitions, replace=True, p=prob_flat)
        row_indices, col_indices = np.unravel_index(flat_indices, self.spatial_shape)
        # Assign ignitions: if duplicate, keep earliest day
        for r, c, day in zip(row_indices, col_indices, sampled_days):
            if ignitions[r, c] == 0:
                ignitions[r, c] = day
            else:
                if not self.resample_on_duplicate:
                    ignitions[r, c] = min(ignitions[r, c], day)
        state.set_variable("ignitions", ignitions)
        return ignitions

    def apply_to_state(self, state: StateRepresentation, **kwargs):
        """
        Drop-in compatible method to generate and record ignitions for the current year.
        """
        return self.generate_ignitions(state)
