"""Annual State Tracker implementation.

Provides classes and functions for tracking landscape state over time
with transaction logging, integrity checks, and recovery mechanisms.
"""

import hashlib
import json
import os
import pickle
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple

import numpy as np

from .representation import StateRepresentation


@dataclass
class AnnualStateTracker:
    """Tracks landscape state across simulation years.

    Features:
    - Transaction logging
    - State integrity checks
    - Recovery mechanisms
    - Efficient state retrieval
    - Disk-backed state storage (only last and current state in memory)
    All in-memory state variables are NumPy arrays; all disk I/O is NumPy arrays.
    """

    initial_state: StateRepresentation
    current_year: int = 0
    states: Dict[int, StateRepresentation] = field(default_factory=dict)
    _transaction_log: List[Dict] = field(default_factory=list)
    _checkpoints: Set[int] = field(default_factory=set)
    _recovery_enabled: bool = True
    state_dir: str = "/tmp/laflammscape_states"
    ignition_points: Dict[int, List[Tuple[int, int]]] = field(default_factory=dict)

    def __post_init__(self):
        """Initialize after dataclass creation."""
        # Store initial state at year 0
        self.states[self.current_year] = self.initial_state
        os.makedirs(self.state_dir, exist_ok=True)
        self.ignition_points = {}  # year -> list of (row, col)

    def advance_year(self) -> None:
        """Advance to the next year by cloning the current state.
        This creates a new state representation for the next year.
        Writes the previous state to disk and only keeps last and current in memory.
        """
        prev_year = self.current_year
        next_year = self.current_year + 1
        self.states[next_year] = self.states[self.current_year].clone()
        self.current_year = next_year
        # Write previous state to disk
        prev_state = self.states[prev_year]
        with open(os.path.join(self.state_dir, f"state_{prev_year}.pkl"), "wb") as f:
            pickle.dump(prev_state, f)
        # Only keep last and current state in memory
        to_delete = [y for y in self.states if y not in (self.current_year, prev_year)]
        for y in to_delete:
            del self.states[y]
        self._log_transaction("advance_year", {"year": next_year})

    def get_state(self, year: Optional[int] = None) -> StateRepresentation:
        """Get the state for a specific year.
        Loads from disk if not in memory.
        Args:
            year: Year to get state for, or None for current year
        Returns:
            State representation for the requested year
        Raises:
            KeyError: If state for the requested year doesn't exist
        """
        target_year = year if year is not None else self.current_year
        if target_year in self.states:
            return self.states[target_year]
        # Otherwise, try to load from disk
        path = os.path.join(self.state_dir, f"state_{target_year}.pkl")
        if os.path.exists(path):
            with open(path, "rb") as f:
                return pickle.load(f)
        raise KeyError(f"No state exists for year {target_year}")

    def save_checkpoint(self, path: str, years: Optional[List[int]] = None) -> None:
        """Save a checkpoint of the current simulation state.
        Converts all state variables to NumPy arrays before saving.
        Args:
            path: Directory path to save checkpoint to
            years: List of years to save, or None for all years including current
        Raises:
            IOError: If directory creation fails
            pickle.PickleError: If serialization fails
        """
        checkpoint_dir = Path(path)
        checkpoint_dir.mkdir(parents=True, exist_ok=True)
        if years is None:
            years = list(self.states.keys())
        for year in years:
            if year not in self.states:
                continue
            year_dir = checkpoint_dir / f"year_{year}"
            year_dir.mkdir(exist_ok=True)
            state = self.states[year]
            for var_name, var_data in state.state_variables.items():
                var_file = year_dir / f"{var_name}.npy"
                # Ensure variable is a NumPy array
                if not isinstance(var_data, np.ndarray):
                    var_data = np.array(var_data)
                np.save(var_file, var_data)
            meta = {
                "grid_shape": state.grid_shape,
                "cell_size": state.cell_size,
                "variables": list(state.state_variables.keys()),
                "checkpoint_time": datetime.now().isoformat(),
            }
            with open(year_dir / "metadata.json", "w") as f:
                json.dump(meta, f, indent=2)
        tracker_meta = {
            "years": sorted(years),
            "current_year": self.current_year,
            "checkpoint_time": datetime.now().isoformat(),
            "transaction_count": len(self._transaction_log),
        }
        with open(checkpoint_dir / "tracker_metadata.json", "w") as f:
            json.dump(tracker_meta, f, indent=2)
        with open(checkpoint_dir / "transaction_log.json", "w") as f:
            json.dump(self._transaction_log, f, indent=2)
        for year in years:
            self._checkpoints.add(year)
        self._log_transaction("save_checkpoint", {"path": str(path), "years": years})

    def load_checkpoint(self, path: str, recovery_mode: bool = False) -> None:
        """Load a checkpoint of simulation state.
        Loads all variables as NumPy arrays.
        Args:
            path: Directory path to load checkpoint from
            recovery_mode: Whether to load in recovery mode (preserves transaction log)
        Raises:
            FileNotFoundError: If checkpoint directory or required files don't exist
            ValueError: If checkpoint data is invalid
        """
        checkpoint_dir = Path(path)
        if not checkpoint_dir.exists():
            raise FileNotFoundError(f"Checkpoint directory not found: {path}")
        meta_file = checkpoint_dir / "tracker_metadata.json"
        if not meta_file.exists():
            raise FileNotFoundError(f"Tracker metadata not found: {meta_file}")
        with open(meta_file, "r") as f:
            tracker_meta = json.load(f)
        if not recovery_mode:
            log_file = checkpoint_dir / "transaction_log.json"
            if log_file.exists():
                with open(log_file, "r") as f:
                    self._transaction_log = json.load(f)
            else:
                self._transaction_log = []
        years = tracker_meta.get("years", [])
        for year in years:
            year_dir = checkpoint_dir / f"year_{year}"
            if not year_dir.exists():
                continue
            with open(year_dir / "metadata.json", "r") as f:
                state_meta = json.load(f)
            state = StateRepresentation(
                grid_shape=tuple(state_meta["grid_shape"]),
                cell_size=state_meta["cell_size"],
            )
            for var_name in state_meta["variables"]:
                var_file = year_dir / f"{var_name}.npy"
                if var_file.exists():
                    var_data = np.load(var_file)
                    state.set_variable(var_name, var_data)
            self.states[year] = state
        if "current_year" in tracker_meta and tracker_meta["current_year"] in self.states:
            self.current_year = tracker_meta["current_year"]
        elif years:
            self.current_year = max(years)
        if 0 in self.states:
            self.initial_state = self.states[0]
        self._checkpoints.update(years)
        if not recovery_mode:
            self._log_transaction("load_checkpoint", {"path": str(path)})

    def _log_transaction(self, action: str, details: Dict) -> None:
        """Log a transaction for audit and recovery.
        Args:
            action: Name of the action performed
            details: Dictionary of action details
        """
        self._transaction_log.append(
            {
                "timestamp": datetime.now().isoformat(),
                "action": action,
                "details": details,
            }
        )

    def verify_integrity(self) -> List[str]:
        """Verify integrity of all states.
        Returns:
            List of integrity error messages, empty if all states are valid
        """
        errors = []
        years = sorted(self.states.keys())
        for i, year in enumerate(years):
            if i > 0 and year != years[i - 1] + 1:
                errors.append(f"Gap in state years: {years[i-1]} to {year}")
        if len(years) > 0:
            reference_shape = self.states[years[0]].grid_shape
            for year in years:
                if self.states[year].grid_shape != reference_shape:
                    errors.append(
                        f"State for year {year} has inconsistent grid shape: "
                        f"{self.states[year].grid_shape}, expected {reference_shape}"
                    )
        required_vars = ["vegetation_type"]  # Essential variables to check
        for year in years:
            state = self.states[year]
            for var in required_vars:
                if var not in state.state_variables:
                    errors.append(f"State for year {year} is missing required variable: {var}")
        if self.current_year not in self.states:
            errors.append(f"Current year {self.current_year} does not exist in states")
        return errors

    def enable_recovery(self, enabled: bool = True) -> None:
        """Enable or disable recovery mechanisms.
        Args:
            enabled: Whether recovery mechanisms should be enabled
        """
        self._recovery_enabled = enabled

    def create_recovery_point(self, path: str) -> None:
        """Create a recovery point by saving a checkpoint.
        Args:
            path: Directory path to save recovery point to
        """
        if not self._recovery_enabled:
            return
        self.save_checkpoint(path, years=[self.current_year])

    def recover_from_point(self, path: str) -> bool:
        """Recover from a previously saved recovery point.
        Args:
            path: Directory path of recovery point
        Returns:
            True if recovery was successful, False otherwise
        """
        if not self._recovery_enabled:
            return False
        try:
            self.load_checkpoint(path, recovery_mode=True)
            self._log_transaction("recover", {"path": str(path)})
            return True
        except (FileNotFoundError, ValueError, IOError):
            return False

    def get_checkpoint_years(self) -> List[int]:
        """Get list of years that have been checkpointed.
        Returns:
            List of years that have been saved as checkpoints
        """
        return sorted(self._checkpoints)

    def calculate_state_hash(self, year: Optional[int] = None) -> str:
        """Calculate a hash of the state for integrity verification.
        Converts all state variables to NumPy arrays before hashing.
        Args:
            year: Year to calculate hash for, or None for current year
        Returns:
            SHA-256 hash of the state
        Raises:
            KeyError: If state for the requested year doesn't exist
        """
        target_year = year if year is not None else self.current_year
        if target_year not in self.states:
            raise KeyError(f"No state exists for year {target_year}")
        state = self.states[target_year]
        hash_obj = hashlib.sha256()
        hash_obj.update(str(state.grid_shape).encode())
        hash_obj.update(str(state.cell_size).encode())
        var_names = sorted(state.state_variables.keys())
        for var_name in var_names:
            var_data = state.state_variables[var_name]
            # Ensure variable is a NumPy array
            if not isinstance(var_data, np.ndarray):
                var_data = np.array(var_data)
            sample = var_data.flatten()[:1000]
            hash_obj.update(sample.tobytes())
            hash_obj.update(str(var_data.shape).encode())
            hash_obj.update(str(var_data.dtype).encode())
            hash_obj.update(str(var_data.min()).encode())
            hash_obj.update(str(var_data.max()).encode())
        return hash_obj.hexdigest()
