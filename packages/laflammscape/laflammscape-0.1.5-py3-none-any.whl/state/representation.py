"""State Representation implementation.

Provides classes and functions for representing landscape state with
NumPy array-based state variables, tiling support, and derived property calculation.
"""

from dataclasses import dataclass, field
from typing import (
    Any,
    Callable,
    Dict,
    Iterator,
    List,
    Optional,
    Set,
    Tuple,
    Union,
)

import numpy as np


@dataclass
class StateRepresentation:
    """Represents the landscape state at a point in time.

    Features:
    - NumPy array-based state variables
    - Tiling support for large landscapes
    - Derived property calculation
    - Efficient state updates
    """

    grid_shape: Tuple[int, int]
    cell_size: float
    state_variables: Dict[str, np.ndarray] = field(default_factory=dict)
    _derived_cache: Dict[str, np.ndarray] = field(default_factory=dict)
    _modified_variables: Set[str] = field(default_factory=set)
    _derived_functions: Dict[str, Callable] = field(default_factory=dict)
    _tile_size: Optional[int] = None

    def __post_init__(self):
        """Initialize after dataclass creation."""
        # Convert any non-numpy arrays to numpy arrays
        for name, data in self.state_variables.items():
            if not isinstance(data, np.ndarray):
                self.state_variables[name] = data  # leave as is for dicts/objects
        # Validate shape consistency for any preset state variables
        for name, data in self.state_variables.items():
            if isinstance(data, np.ndarray):
                if data.shape[:2] != self.grid_shape:
                    raise ValueError(
                        f"State variable '{name}' has shape {data.shape}, "
                        f"expected first dimensions to be {self.grid_shape}"
                    )
        # Register default derived properties
        self.register_derived_property("slope", self._calculate_slope, depends_on=["elevation"])
        self.register_derived_property("aspect", self._calculate_aspect, depends_on=["elevation"])

    def set_variable(self, name: str, data: Union[np.ndarray, Any]) -> None:
        """Set a state variable.

        Args:
            name: Variable name
            data: Variable data array (numpy array or convertible)
        """
        if isinstance(data, np.ndarray):
            if data.shape[:2] != self.grid_shape:
                raise ValueError(
                    f"Data shape {data.shape} does not match grid shape {self.grid_shape}"
                )
        self.state_variables[name] = data
        self._modified_variables.add(name)
        self._clear_derived_cache()

    def set_dict(self, name: str, data: Dict[str, Any]) -> None:
        """Set a dictionary variable in the state.

        Args:
            name: Variable name
            data: Dictionary data
        """
        self.state_variables[name] = data

    def get_dict(self, name: str) -> Dict[str, Any]:
        """Get a dictionary variable from the state.

        Args:
            name: Variable name

        Returns:
            Dictionary data

        Raises:
            KeyError: If variable doesn't exist
        """
        if name not in self.state_variables:
            raise KeyError(f"Variable {name} not found in state")
        return self.state_variables[name]

    def get_variable(self, name: str) -> np.ndarray:
        """Get a state variable.

        Args:
            name: Name of the variable to get

        Returns:
            Numpy array data for the variable

        Raises:
            KeyError: If the variable doesn't exist
        """
        if name not in self.state_variables:
            raise KeyError(f"State variable '{name}' not found")
        return self.state_variables[name]

    def get_variable_numpy(self, name: str) -> np.ndarray:
        """Get a state variable as a numpy array.

        Args:
            name: Name of the variable to get

        Returns:
            Numpy array data for the variable

        Raises:
            KeyError: If the variable doesn't exist
        """
        if name not in self.state_variables:
            raise KeyError(f"State variable '{name}' not found")
        return self.state_variables[name]

    def register_derived_property(
        self, name: str, function: Callable, depends_on: List[str] = None
    ) -> None:
        """Register a function to calculate a derived property.

        Args:
            name: Name of the derived property
            function: Function to calculate the property
            depends_on: List of variable names this property depends on
        """
        self._derived_functions[name] = {
            "function": function,
            "depends_on": depends_on or [],
        }

    def get_derived(self, name: str) -> np.ndarray:
        """Get a derived property of the state.

        Args:
            name: Name of the derived property to calculate

        Returns:
            Numpy array data for the derived property

        Raises:
            KeyError: If the derived property is not registered
            ValueError: If dependencies for the derived property are missing
        """
        # Check if the value is cached
        if name in self._derived_cache:
            return self._derived_cache[name]

        # Check if the property is registered
        if name not in self._derived_functions:
            raise KeyError(f"Derived property '{name}' not registered")

        derived_info = self._derived_functions[name]
        function = derived_info["function"]
        depends_on = derived_info["depends_on"]

        # Check dependencies
        for dep in depends_on:
            if dep not in self.state_variables:
                raise ValueError(
                    f"Derived property '{name}' depends on '{dep}', which is not available"
                )

        # Prepare arguments for function
        kwargs = {dep: self.state_variables[dep] for dep in depends_on}

        # Calculate the derived property
        result = function(**kwargs)
        if not isinstance(result, np.ndarray):
            result = np.array(result)

        # Cache the result
        self._derived_cache[name] = result

        return result

    def _clear_derived_cache(self) -> None:
        """Clear the derived property cache after state changes."""
        self._derived_cache.clear()

    def clone(self) -> "StateRepresentation":
        """Create a shallow copy of the state, reusing existing numpy arrays.

        Returns:
            A new StateRepresentation with shared numpy array data
        """
        new_state = StateRepresentation(
            grid_shape=self.grid_shape,
            cell_size=self.cell_size,
            state_variables=self.state_variables,
            _tile_size=self._tile_size,
        )

        # Copy derived functions
        for name, info in self._derived_functions.items():
            new_state.register_derived_property(name, info["function"], info["depends_on"])

        return new_state

    def enable_tiling(self, tile_size: int) -> None:
        """Enable tiling for large landscapes.

        Args:
            tile_size: Size of tiles in grid cells

        Raises:
            ValueError: If tile_size is invalid
        """
        if tile_size <= 0:
            raise ValueError("Tile size must be positive")

        self._tile_size = tile_size

    def disable_tiling(self) -> None:
        """Disable tiling."""
        self._tile_size = None

    def get_tiles(
        self,
    ) -> Iterator[Tuple[Tuple[int, int, int, int], Dict[str, np.ndarray]]]:
        """Get iterator over tiles of the landscape.

        Returns:
            Iterator yielding (tile_bounds, tile_data) for each tile
            where tile_bounds is (row_start, row_end, col_start, col_end)
            and tile_data is a dictionary of variable numpy arrays for the tile
        """
        if self._tile_size is None:
            # If tiling is disabled, yield the entire grid as one "tile"
            tile_bounds = (0, self.grid_shape[0], 0, self.grid_shape[1])
            yield tile_bounds, self.state_variables
            return

        # Calculate number of tiles
        rows, cols = self.grid_shape
        n_row_tiles = (rows + self._tile_size - 1) // self._tile_size
        n_col_tiles = (cols + self._tile_size - 1) // self._tile_size

        # Iterate over tiles
        for i in range(n_row_tiles):
            for j in range(n_col_tiles):
                # Calculate tile bounds
                row_start = i * self._tile_size
                row_end = min(row_start + self._tile_size, rows)
                col_start = j * self._tile_size
                col_end = min(col_start + self._tile_size, cols)

                # Extract tile data
                tile_data = {}
                for name, data in self.state_variables.items():
                    if isinstance(data, np.ndarray):
                        tile_data[name] = data[row_start:row_end, col_start:col_end]
                    else:
                        tile_data[name] = data

                yield (row_start, row_end, col_start, col_end), tile_data

    def apply_function(
        self,
        function: Callable,
        variables: List[str],
        output_variable: str,
        use_tiling: bool = True,
    ) -> None:
        """Apply a function to state variables.

        Args:
            function: Function to apply
            variables: List of variable names to pass to the function
            output_variable: Name to assign to the output
            use_tiling: Whether to use tiling if enabled
        """
        # Check if all required variables exist
        for var in variables:
            if var not in self.state_variables:
                raise KeyError(f"Variable '{var}' not found")

        if use_tiling and self._tile_size is not None:
            # Initialize output array
            sample_var = self.state_variables[variables[0]]
            output_shape = list(sample_var.shape)
            output_dtype = function(
                **{var: self.state_variables[var][0:1, 0:1] for var in variables}
            ).dtype
            output = np.zeros(output_shape, dtype=output_dtype)

            # Process each tile
            for (
                row_start,
                row_end,
                col_start,
                col_end,
            ), tile_data in self.get_tiles():
                # Extract tile variables
                tile_vars = {var: tile_data[var] for var in variables}

                # Apply function to tile
                tile_result = function(**tile_vars)
                if not isinstance(tile_result, np.ndarray):
                    tile_result = np.array(tile_result)

                # Store tile result
                output[row_start:row_end, col_start:col_end] = tile_result
        else:
            # Process the entire grid at once
            var_dict = {var: self.state_variables[var] for var in variables}
            output = function(**var_dict)
            if not isinstance(output, np.ndarray):
                output = np.array(output)

        # Set output variable
        self.set_variable(output_variable, output)

    # Default derived property calculations

    def _calculate_slope(self, elevation: np.ndarray) -> np.ndarray:
        """Calculate slope from elevation.

        Args:
            elevation: Elevation numpy array

        Returns:
            Slope numpy array in degrees
        """
        # Use Sobel operator for gradient
        from scipy.ndimage import sobel

        dx = sobel(elevation, axis=1)
        dy = sobel(elevation, axis=0)
        slope = np.degrees(np.arctan(np.sqrt(dx**2 + dy**2)))
        return slope

    def _calculate_aspect(self, elevation: np.ndarray) -> np.ndarray:
        """Calculate aspect from elevation.

        Args:
            elevation: Elevation numpy array

        Returns:
            Aspect numpy array in degrees (0-360, clockwise from north)
        """
        # Use Sobel operator for gradient
        from scipy.ndimage import sobel

        dx = sobel(elevation, axis=1)
        dy = sobel(elevation, axis=0)
        aspect = np.degrees(np.arctan2(-dx, dy))
        # Convert to 0-360, clockwise from north
        aspect = np.where(aspect < 0, aspect + 360, aspect)
        return aspect

    def copy(self) -> "StateRepresentation":
        """Create a deep copy of the state (alias for clone).

        Returns:
            A new StateRepresentation with copied data
        """
        return self.clone()

    def has_variable(self, name: str) -> bool:
        """Check if a variable exists in the state.

        Args:
            name: Name of the variable to check

        Returns:
            True if the variable exists, False otherwise
        """
        return name in self.state_variables

    def remove_variable(self, name: str) -> None:
        """Remove a variable from the state.

        Args:
            name: Name of the variable to remove

        Raises:
            KeyError: If the variable doesn't exist
        """
        if name not in self.state_variables:
            raise KeyError(f"State variable '{name}' not found")

        del self.state_variables[name]
        if name in self._modified_variables:
            self._modified_variables.remove(name)

    def get_all_variables(self) -> Dict[str, np.ndarray]:
        """Get all state variables.

        Returns:
            Dictionary of all state variables
        """
        return {
            name: np.copy(data) if isinstance(data, np.ndarray) else data
            for name, data in self.state_variables.items()
        }

    def initialize_burn_state_tracking(self) -> None:
        """Initialize burn state tracking variable.

        Creates a boolean array to track whether each cell has burned
        during its current state. This should be called when initializing
        a new state representation.
        """
        if "burned_in_current_state" not in self.state_variables:
            self.set_variable(
                "burned_in_current_state",
                np.zeros(self.grid_shape, dtype=bool),
            )

    def reset_burn_state_tracking(self, mask: np.ndarray) -> None:
        """Reset burn state tracking for specified cells.

        Args:
            mask: Boolean array indicating which cells to reset
        """
        if "burned_in_current_state" in self.state_variables:
            burned_state = self.get_variable("burned_in_current_state")
            burned_state[mask] = False
            self.set_variable("burned_in_current_state", burned_state)

    def mark_burned_cells(self, mask: np.ndarray) -> None:
        """Mark cells as burned in their current state.

        Args:
            mask: Boolean array indicating which cells have burned
        """
        if "burned_in_current_state" not in self.state_variables:
            self.initialize_burn_state_tracking()

        burned_state = self.get_variable("burned_in_current_state")
        burned_state[mask] = True
        self.set_variable("burned_in_current_state", burned_state)
