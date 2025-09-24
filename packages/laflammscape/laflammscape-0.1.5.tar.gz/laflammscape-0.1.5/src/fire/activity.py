"""Fire Activity Tracker implementation.

Provides classes and functions for tracking fire activity with simulation
window optimization, containment modeling, and vectorized outputs.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Tuple

import numpy as np

from ..state.representation import StateRepresentation


@dataclass
class FireEvent:
    """Represents a single fire event with progression tracking.
    
    Features:
    - Fire identification and metadata
    - Progression tracking by day
    - Burn state recording
    - Serialization support
    """
    
    id: str
    start_day: int
    start_location: Tuple[int, int]
    ignition_source: str = "unknown"
    progression: Dict[int, np.ndarray] = field(default_factory=dict)
    
    def update(self, day: int, burn_state: np.ndarray) -> None:
        """Update fire progression for a specific day.
        
        Args:
            day: Day of year
            burn_state: 2D array where 1 = burned, 0 = unburned
        """
        self.progression[day] = burn_state.copy()
    
    def get_burned_area(self, day: int) -> int:
        """Get burned area for a specific day.
        
        Args:
            day: Day of year
            
        Returns:
            Number of burned cells
        """
        if day not in self.progression:
            return 0
        return int(np.sum(self.progression[day]))
    
    def get_total_burned_area(self) -> int:
        """Get total burned area across all days.
        
        Returns:
            Total number of burned cells
        """
        if not self.progression:
            return 0
        
        # Combine all progression days to get total burned area
        total_burned = np.zeros_like(list(self.progression.values())[0], dtype=np.int8)
        for burn_state in self.progression.values():
            total_burned = np.logical_or(total_burned, burn_state)
        
        return int(np.sum(total_burned))
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert fire event to dictionary for serialization.
        
        Returns:
            Dictionary representation of the fire event
        """
        return {
            "id": self.id,
            "start_day": self.start_day,
            "start_location": self.start_location,
            "ignition_source": self.ignition_source,
            "progression": {str(day): state.tolist() for day, state in self.progression.items()}
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "FireEvent":
        """Create fire event from dictionary.
        
        Args:
            data: Dictionary representation
            
        Returns:
            FireEvent instance
        """
        progression = {}
        if "progression" in data:
            progression = {
                int(day): np.array(state, dtype=np.int8) 
                for day, state in data["progression"].items()
            }
        
        return cls(
            id=data["id"],
            start_day=data["start_day"],
            start_location=tuple(data["start_location"]),
            ignition_source=data.get("ignition_source", "unknown"),
            progression=progression
        )


@dataclass
class FireActivityTracker:
    """Tracks fire activity across the landscape.

    Features:
    - Simulation window optimization
    - Containment modeling
    - Vectorized outputs
    - Fire progression tracking
    All state variable interactions use NumPy arrays for consistency.
    """

    active_fires: Dict[int, Dict[str, Any]] = field(default_factory=dict)
    _next_fire_id: int = 1
    _activity_history: List[Dict[str, Any]] = field(default_factory=list)

    def initialize_from_ignitions(self, state: StateRepresentation, day_of_year: int) -> None:
        """Initialize fire activity from ignitions in the state.

        Args:
            state: Landscape state with ignitions
            day_of_year: Current day of year (1-366)
        """
        ignitions = state.get_variable("ignitions")
        ignitions_np = np.asarray(ignitions)

        # Find ignition locations
        ignition_coords = np.where(ignitions_np > 0)
        n_ignitions = len(ignition_coords[0])

        # Initialize fire objects for each ignition
        for i in range(n_ignitions):
            row, col = ignition_coords[0][i], ignition_coords[1][i]
            fire_id = self._next_fire_id
            self._next_fire_id += 1

            # Create fire object
            self.active_fires[fire_id] = {
                "id": fire_id,
                "start_day": day_of_year,
                "current_day": day_of_year,
                "origin": (row, col),
                "perimeter": {(row, col)},
                "area": 1,
                "contained": False,
                "containment_day": None,
            }

            # Log ignition event
            self._log_event(fire_id, "ignition", day_of_year, {"location": (row, col)})

    def update_burn_map(self, state: StateRepresentation) -> None:
        """Update the burn map in the state based on active fires.

        Args:
            state: Landscape state to update
        """
        grid_shape = state.grid_shape

        # Initialize burn map if it doesn't exist
        if "burn_map" not in state.state_variables:
            burn_map_np = np.zeros(grid_shape, dtype=np.int32)
            state.set_variable("burn_map", burn_map_np)
        else:
            burn_map = state.get_variable("burn_map")
            burn_map_np = np.asarray(burn_map).copy()

        # Update burn map with active fires
        for fire_id, fire in self.active_fires.items():
            if not fire["contained"]:
                for row, col in fire["perimeter"]:
                    if 0 <= row < grid_shape[0] and 0 <= col < grid_shape[1]:
                        burn_map_np[row, col] = fire_id

        # Update state with new burn map as NumPy array
        state.set_variable("burn_map", burn_map_np)

    def advance_fires(self, state: StateRepresentation, day_of_year: int) -> None:
        """Advance fire spread for active fires.

        Args:
            state: Landscape state
            day_of_year: Current day of year (1-366)
        """
        # TODO: Implement fire spread logic
        # This is a placeholder that advances fire day and checks containment
        for fire_id, fire in list(self.active_fires.items()):
            if fire["contained"]:
                continue

            # Update fire day
            fire["current_day"] = day_of_year

            # Check for containment (simplified logic)
            fire_duration = day_of_year - fire["start_day"]
            if fire_duration > 14:  # Simplified containment after 14 days
                self._contain_fire(fire_id, day_of_year)

    def _contain_fire(self, fire_id: int, day_of_year: int) -> None:
        """Mark a fire as contained.

        Args:
            fire_id: ID of the fire to contain
            day_of_year: Day of containment
        """
        if fire_id in self.active_fires:
            fire = self.active_fires[fire_id]
            fire["contained"] = True
            fire["containment_day"] = day_of_year

            # Log containment event
            self._log_event(
                fire_id,
                "containment",
                day_of_year,
                {
                    "duration": day_of_year - fire["start_day"],
                    "area": fire["area"],
                },
            )

    def _log_event(
        self,
        fire_id: int,
        event_type: str,
        day_of_year: int,
        details: Dict[str, Any],
    ) -> None:
        """Log a fire activity event.

        Args:
            fire_id: ID of the fire
            event_type: Type of event
            day_of_year: Day of the event
            details: Event details
        """
        self._activity_history.append(
            {
                "fire_id": fire_id,
                "event": event_type,
                "day": day_of_year,
                "details": details,
                "timestamp": datetime.now().isoformat(),
            }
        )

    def get_active_fire_count(self) -> int:
        """Get count of active fires.

        Returns:
            Number of active fires
        """
        return sum(1 for fire in self.active_fires.values() if not fire["contained"])

    def get_total_burned_area(self) -> int:
        """Get total area burned by all fires.

        Returns:
            Total burned area in grid cells
        """
        return sum(fire["area"] for fire in self.active_fires.values())

    def get_fire_summary(self) -> Dict[str, Any]:
        """Get a summary of fire activity.

        Returns:
            Dictionary with fire activity summary
        """
        active_count = self.get_active_fire_count()
        contained_count = len(self.active_fires) - active_count

        return {
            "total_fires": len(self.active_fires),
            "active_fires": active_count,
            "contained_fires": contained_count,
            "total_burned_area": self.get_total_burned_area(),
        }
