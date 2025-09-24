"""Output Module implementation.

Provides classes and functions for exporting simulation results,
generating visualizations, and performing analysis.
"""

import json
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional

import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.colors import LinearSegmentedColormap

from ..state.representation import StateRepresentation
from ..state.tracker import AnnualStateTracker


@dataclass
class OutputManager:
    """Manages outputs from Laflammscape simulations.

    Features:
    - Multi-format export
    - Visualization generation
    - Fire regime analysis
    - Web output generation
    """

    output_dir: Path
    _exporters: Dict[str, Any] = field(default_factory=dict)
    _colormaps: Dict[str, Any] = field(default_factory=dict)
    _variable_metadata: Dict[str, Dict[str, Any]] = field(default_factory=dict)

    def __post_init__(self):
        """Initialize after dataclass creation."""
        # Ensure output directory exists
        self.output_dir.mkdir(parents=True, exist_ok=True)

        # Initialize subdirectories
        (self.output_dir / "data").mkdir(exist_ok=True)
        (self.output_dir / "figures").mkdir(exist_ok=True)
        (self.output_dir / "reports").mkdir(exist_ok=True)
        (self.output_dir / "web").mkdir(exist_ok=True)

        # Setup default colormaps
        self._setup_default_colormaps()

        # Setup default variable metadata
        self._setup_default_variable_metadata()

    def _setup_default_colormaps(self) -> None:
        """Setup default colormaps for common variables."""
        # Vegetation type colormap
        self._colormaps["vegetation_type"] = mcolors.ListedColormap(
            [
                "#276419",  # Forest - dark green
                "#78AB46",  # Shrubland - light green
                "#E6E28A",  # Grassland - light yellow
                "#C2B280",  # Barren - tan
                "#95D0FC",  # Water - light blue
                "#B50000",  # Developed - red
            ]
        )

        # Fire-related colormaps
        self._colormaps["burn_severity"] = LinearSegmentedColormap.from_list(
            "burn_severity",
            [
                (0, "white"),
                (0.2, "yellow"),
                (0.5, "orange"),
                (0.8, "red"),
                (1.0, "darkred"),
            ],
        )

        self._colormaps["fire_mortality"] = LinearSegmentedColormap.from_list(
            "fire_mortality",
            [(0, "white"), (0.3, "yellow"), (0.7, "orange"), (1.0, "red")],
        )

        # Elevation and derived
        self._colormaps["elevation"] = plt.cm.terrain
        self._colormaps["slope"] = plt.cm.YlOrBr
        self._colormaps["aspect"] = plt.cm.twilight_shifted

        # Fuel model
        self._colormaps["fuel_model"] = plt.cm.tab20

        # Default colormap for other variables
        self._colormaps["default"] = plt.cm.viridis

    def _setup_default_variable_metadata(self) -> None:
        """Setup default metadata for common variables."""
        self._variable_metadata.update(
            {
                "vegetation_type": {
                    "title": "Vegetation Type",
                    "units": "class",
                    "value_range": None,  # Categorical variable
                    "class_names": {
                        1: "Forest",
                        2: "Shrubland",
                        3: "Grassland",
                        4: "Barren",
                        5: "Water",
                        6: "Developed",
                    },
                },
                "elevation": {
                    "title": "Elevation",
                    "units": "m",
                    "value_range": None,  # Automatically determined
                },
                "slope": {
                    "title": "Slope",
                    "units": "degrees",
                    "value_range": [0, 90],
                },
                "aspect": {
                    "title": "Aspect",
                    "units": "degrees",
                    "value_range": [0, 360],
                },
                "burn_severity": {
                    "title": "Burn Severity",
                    "units": "index",
                    "value_range": [0, 1],
                },
                "fire_mortality": {
                    "title": "Fire Mortality",
                    "units": "proportion",
                    "value_range": [0, 1],
                },
                "fuel_model": {
                    "title": "Fuel Model",
                    "units": "class",
                    "value_range": None,
                },
                "fuel_moisture_1hr": {
                    "title": "1-hr Fuel Moisture",
                    "units": "%",
                    "value_range": [0, 30],
                },
                "fuel_moisture_10hr": {
                    "title": "10-hr Fuel Moisture",
                    "units": "%",
                    "value_range": [0, 35],
                },
                "fuel_moisture_100hr": {
                    "title": "100-hr Fuel Moisture",
                    "units": "%",
                    "value_range": [0, 40],
                },
            }
        )

    def register_exporter(self, name: str, exporter: Any) -> None:
        """Register an output exporter.

        Args:
            name: Name to register the exporter under
            exporter: Exporter object
        """
        self._exporters[name] = exporter

    def register_colormap(self, variable: str, colormap: Any) -> None:
        """Register a colormap for a variable.

        Args:
            variable: Name of the variable
            colormap: Matplotlib colormap
        """
        self._colormaps[variable] = colormap

    def register_variable_metadata(self, variable: str, metadata: Dict[str, Any]) -> None:
        """Register metadata for a variable.

        Args:
            variable: Name of the variable
            metadata: Dictionary of metadata
        """
        self._variable_metadata[variable] = metadata

    def export_state(self, state: StateRepresentation, name: str) -> None:
        """Export a single state.

        Args:
            state: State to export
            name: Base name for export files
        """
        # Create output directory
        export_dir = self.output_dir / "data" / name
        export_dir.mkdir(exist_ok=True)

        # Export each variable as a NumPy file
        for var_name, var_data in state.state_variables.items():
            var_file = export_dir / f"{var_name}.npy"
            # Ensure variable is a NumPy array
            var_data = np.asarray(var_data)
            np.save(var_file, var_data)

        # Export metadata
        meta = {
            "grid_shape": state.grid_shape,
            "cell_size": state.cell_size,
            "variables": list(state.state_variables.keys()),
            "export_time": datetime.now().isoformat(),
        }

        with open(export_dir / "metadata.json", "w") as f:
            json.dump(meta, f, indent=2)

        # Generate a summary report
        summary = {
            "name": name,
            "grid_shape": state.grid_shape,
            "cell_size": state.cell_size,
            "variables": {},
        }

        for var_name, var_data in state.state_variables.items():
            # Ensure variable is a NumPy array
            var_data = np.asarray(var_data)
            var_summary = {
                "shape": var_data.shape,
                "dtype": str(var_data.dtype),
                "min": float(var_data.min()) if var_data.size > 0 else None,
                "max": float(var_data.max()) if var_data.size > 0 else None,
                "mean": float(var_data.mean()) if var_data.size > 0 else None,
            }
            summary["variables"][var_name] = var_summary

        with open(export_dir / "summary.json", "w") as f:
            json.dump(summary, f, indent=2)

    def export_timeseries(self, tracker: AnnualStateTracker, variables: List[str]) -> None:
        """Export a timeseries of state variables.

        Args:
            tracker: State tracker containing multiple years of data
            variables: List of state variable names to export
        """
        # Get all years from tracker
        years = sorted(tracker.states.keys())

        # Create output directory
        export_dir = self.output_dir / "data" / "timeseries"
        export_dir.mkdir(exist_ok=True)

        # Process each variable
        for var_name in variables:
            # Check if all years have this variable
            missing_years = []
            for year in years:
                state = tracker.states[year]
                if var_name not in state.state_variables:
                    missing_years.append(year)

            if missing_years:
                print(f"Warning: Variable '{var_name}' missing for years: {missing_years}")
                continue

            # Create a multi-year array
            first_state = tracker.states[years[0]]
            var_data = first_state.state_variables[var_name]
            # Ensure variable is a NumPy array
            var_data = np.asarray(var_data)
            data_shape = [len(years)] + list(var_data.shape)
            timeseries = np.zeros(data_shape, dtype=var_data.dtype)

            # Fill the timeseries array
            for i, year in enumerate(years):
                state = tracker.states[year]
                data = state.state_variables[var_name]
                # Ensure variable is a NumPy array
                data = np.asarray(data)
                timeseries[i] = data

            # Save the timeseries
            var_file = export_dir / f"{var_name}_timeseries.npy"
            np.save(var_file, timeseries)

            # Save metadata
            meta = {
                "variable": var_name,
                "years": years,
                "shape": data_shape,
                "dtype": str(var_data.dtype),
                "export_time": datetime.now().isoformat(),
            }

            meta_file = export_dir / f"{var_name}_metadata.json"
            with open(meta_file, "w") as f:
                json.dump(meta, f, indent=2)

            # Save summary statistics as CSV
            stats = []
            for i, year in enumerate(years):
                year_data = timeseries[i]
                stats.append(
                    {
                        "year": year,
                        "min": (float(year_data.min()) if year_data.size > 0 else None),
                        "max": (float(year_data.max()) if year_data.size > 0 else None),
                        "mean": (float(year_data.mean()) if year_data.size > 0 else None),
                        "std": (float(year_data.std()) if year_data.size > 0 else None),
                    }
                )

            stats_df = pd.DataFrame(stats)
            stats_file = export_dir / f"{var_name}_statistics.csv"
            stats_df.to_csv(stats_file, index=False)

    def generate_visualization(
        self,
        state: StateRepresentation,
        variable: str,
        output_path: Optional[str] = None,
        title: Optional[str] = None,
        colormap: Optional[Any] = None,
        dpi: int = 300,
    ) -> str:
        """Generate a visualization of a state variable.

        Args:
            state: State to visualize
            variable: Name of the state variable to visualize
            output_path: Optional path to save visualization to
            title: Optional title for the visualization
            colormap: Optional colormap override
            dpi: Resolution for output image

        Returns:
            Path to the generated visualization file

        Raises:
            KeyError: If the variable doesn't exist in the state
        """
        if variable not in state.state_variables:
            raise KeyError(f"Variable '{variable}' not found in state")

        # Get the data to visualize
        data = state.get_variable(variable)
        # Ensure variable is a NumPy array
        data = np.asarray(data)

        # Get metadata for the variable
        metadata = self._variable_metadata.get(variable, {})
        variable_title = title or metadata.get("title", variable)
        units = metadata.get("units", "")
        value_range = metadata.get("value_range")
        class_names = metadata.get("class_names")

        # Get colormap
        cmap = colormap or self._colormaps.get(variable, self._colormaps.get("default"))

        # Create figure
        fig = plt.figure(figsize=(10, 8), dpi=dpi)
        ax = fig.add_subplot(111)

        # Plot the data
        if value_range:
            im = ax.imshow(data, cmap=cmap, vmin=value_range[0], vmax=value_range[1])
        else:
            im = ax.imshow(data, cmap=cmap)

        # Add colorbar
        cbar = fig.colorbar(im, ax=ax)
        if units:
            cbar.set_label(units)

        # Add class labels if categorical
        if class_names:
            # Create custom tick labels
            unique_values = sorted(np.unique(data))
            tick_locs = [val for val in unique_values if val in class_names]
            tick_labels = [class_names[val] for val in tick_locs]

            cbar.set_ticks(tick_locs)
            cbar.set_ticklabels(tick_labels)

        # Add title
        ax.set_title(variable_title)

        # Remove axis ticks
        ax.set_xticks([])
        ax.set_yticks([])

        # Add grid
        ax.grid(False)

        # Set up path for saving
        if output_path:
            fig_path = Path(output_path)
        else:
            fig_dir = self.output_dir / "figures"
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            fig_path = fig_dir / f"{variable}_{timestamp}.png"

        # Save figure
        fig.savefig(fig_path, dpi=dpi, bbox_inches="tight")
        plt.close(fig)

        return str(fig_path)

    def generate_timeseries_plot(
        self,
        tracker: AnnualStateTracker,
        variable: str,
        aggregation: str = "mean",
        output_path: Optional[str] = None,
        title: Optional[str] = None,
        dpi: int = 300,
    ) -> str:
        """Generate a plot of a variable over time.

        Args:
            tracker: State tracker containing multiple years of data
            variable: Name of the state variable to visualize
            aggregation: Aggregation method ('mean', 'max', 'min', 'sum')
            output_path: Optional path to save visualization to
            title: Optional title for the visualization
            dpi: Resolution for output image

        Returns:
            Path to the generated visualization file
        """
        # Get all years
        years = sorted(tracker.states.keys())

        # Check if all years have this variable
        values = []
        for year in years:
            state = tracker.states[year]
            if variable not in state.state_variables:
                continue

            data = state.get_variable(variable)

            # Apply aggregation
            if aggregation == "mean":
                values.append(float(data.mean()))
            elif aggregation == "max":
                values.append(float(data.max()))
            elif aggregation == "min":
                values.append(float(data.min()))
            elif aggregation == "sum":
                values.append(float(data.sum()))
            else:
                values.append(float(data.mean()))  # Default to mean

        # Get metadata for the variable
        metadata = self._variable_metadata.get(variable, {})
        variable_title = metadata.get("title", variable)
        units = metadata.get("units", "")

        # Create plot title
        if title:
            plot_title = title
        else:
            plot_title = f"{variable_title} ({aggregation.capitalize()})"
            if units:
                plot_title += f" [{units}]"

        # Create figure
        fig = plt.figure(figsize=(10, 6), dpi=dpi)
        ax = fig.add_subplot(111)

        # Plot the data
        ax.plot(years, values, marker="o", linestyle="-", linewidth=2)

        # Add labels and title
        ax.set_xlabel("Year")
        y_label = aggregation.capitalize()
        if units:
            y_label += f" [{units}]"
        ax.set_ylabel(y_label)
        ax.set_title(plot_title)

        # Add grid
        ax.grid(True, linestyle="--", alpha=0.7)

        # Set up path for saving
        if output_path:
            fig_path = Path(output_path)
        else:
            fig_dir = self.output_dir / "figures"
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            fig_path = fig_dir / f"{variable}_timeseries_{timestamp}.png"

        # Save figure
        fig.savefig(fig_path, dpi=dpi, bbox_inches="tight")
        plt.close(fig)

        return str(fig_path)

    def analyze_fire_regime(self, tracker: AnnualStateTracker) -> Dict[str, Any]:
        """Analyze fire regime characteristics from simulation results.

        Args:
            tracker: State tracker containing multiple years of fire data

        Returns:
            Dictionary of fire regime metrics
        """
        # Get all years
        years = sorted(tracker.states.keys())

        # Extract burn data from each year
        burn_maps = {}
        for year in years:
            state = tracker.states[year]
            if "burn_map" in state.state_variables:
                data = state.get_variable("burn_map")
                # Ensure variable is a NumPy array
                data = np.asarray(data)
                burn_maps[year] = data

        if not burn_maps:
            return {"error": "No burn maps found in simulation results"}

        # Calculate cumulative burn map
        first_burn_map = next(iter(burn_maps.values()))
        cumulative_burn = np.zeros_like(first_burn_map, dtype=bool)
        for year, burn_map in burn_maps.items():
            burned_mask = burn_map > 0
            cumulative_burn = cumulative_burn | burned_mask

        # Count cells in grid
        total_cells = np.prod(first_burn_map.shape)
        burnable_cells = total_cells  # Could be refined with nonburnable mask

        # Calculate basic metrics
        total_burned_cells = cumulative_burn.sum()
        burn_fraction = total_burned_cells / burnable_cells

        # Calculate burn fractions by year
        annual_burn_fractions = {}
        for year, burn_map in burn_maps.items():
            burned_mask = burn_map > 0
            annual_burn_fraction = burned_mask.sum() / burnable_cells
            annual_burn_fractions[year] = float(annual_burn_fraction)

        # Calculate mean annual burn fraction
        mean_annual_burn_fraction = np.mean(list(annual_burn_fractions.values()))

        # Calculate fire rotation period (years required to burn area equal to burnable area)
        fire_rotation_period = (
            1.0 / mean_annual_burn_fraction if mean_annual_burn_fraction > 0 else float("inf")
        )

        # Calculate fire size distribution
        fire_sizes = []
        for year, burn_map in burn_maps.items():
            # Get unique fire IDs (excluding 0, which is unburned)
            fire_ids = np.unique(burn_map)
            fire_ids = fire_ids[fire_ids > 0]

            # Count cells for each fire
            for fire_id in fire_ids:
                fire_mask = burn_map == fire_id
                fire_size = fire_mask.sum()
                fire_sizes.append(int(fire_size))

        # Calculate fire size statistics
        if fire_sizes:
            mean_fire_size = np.mean(fire_sizes)
            median_fire_size = np.median(fire_sizes)
            max_fire_size = np.max(fire_sizes)
            std_fire_size = np.std(fire_sizes)
        else:
            mean_fire_size = median_fire_size = max_fire_size = std_fire_size = 0.0

        # Return metrics
        return {
            "years_analyzed": len(burn_maps),
            "burnable_area": int(burnable_cells),
            "total_burned_area": int(total_burned_cells),
            "cumulative_burn_fraction": float(burn_fraction),
            "mean_annual_burn_fraction": float(mean_annual_burn_fraction),
            "fire_rotation_period": float(fire_rotation_period),
            "annual_burn_fractions": annual_burn_fractions,
            "total_fires": len(fire_sizes),
            "fire_size_distribution": {
                "mean": float(mean_fire_size),
                "median": float(median_fire_size),
                "max": float(max_fire_size),
                "std": float(std_fire_size),
            },
        }

    def generate_web_output(
        self,
        tracker: AnnualStateTracker,
        variables: List[str],
        output_dir: Optional[str] = None,
    ) -> str:
        """Generate web-based visualization output.

        Args:
            tracker: State tracker containing simulation results
            variables: List of variables to include in visualization
            output_dir: Optional directory to save web output to

        Returns:
            Path to the generated web output directory
        """
        # Set up output directory
        if output_dir:
            web_dir = Path(output_dir)
        else:
            web_dir = self.output_dir / "web"

        data_dir = web_dir / "data"
        img_dir = web_dir / "img"

        # Create directories
        web_dir.mkdir(exist_ok=True, parents=True)
        data_dir.mkdir(exist_ok=True)
        img_dir.mkdir(exist_ok=True)

        # Get all years
        years = sorted(tracker.states.keys())

        # Generate visualizations for each variable and year
        for variable in variables:
            for year in years:
                if year not in tracker.states:
                    continue

                state = tracker.states[year]
                if variable not in state.state_variables:
                    continue

                # Generate visualization
                img_path = img_dir / f"{variable}_{year}.png"
                self.generate_visualization(
                    state,
                    variable,
                    str(img_path),
                    title=f"{variable} - Year {year}",
                )

        # Generate metadata for web interface
        metadata = {
            "title": "Laflammscape Simulation Results",
            "description": "Web-based visualization of landscape simulation results",
            "years": years,
            "variables": variables,
            "generation_time": datetime.now().isoformat(),
        }

        with open(web_dir / "metadata.json", "w") as f:
            json.dump(metadata, f, indent=2)

        # Generate simple HTML index
        html = """<!DOCTYPE html>
<html>
<head>
    <title>Laflammscape Simulation Results</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 0; padding: 20px; }}
        h1 {{ color: #333; }}
        .controls {{ margin-bottom: 20px; }}
        .visualization {{ margin-top: 20px; }}
        select {{ padding: 5px; }}
        img {{ max-width: 100%; }}
    </style>
    <script>
        function updateVisualization() {{
            const variable = document.getElementById('variable-select').value;
            const year = document.getElementById('year-select').value;
            const imgPath = `img/${{variable}}_${{year}}.png`;
            document.getElementById('viz-image').src = imgPath;
            document.getElementById('viz-title').innerText = `${{variable}} - Year ${{year}}`;
        }}
    </script>
</head>
<body>
    <h1>Laflammscape Simulation Results</h1>
    <div class="controls">
        <label for="variable-select">Variable:</label>
        <select id="variable-select" onchange="updateVisualization()">
            {"".join(f'<option value="{var}">{var}</option>' for var in variables)}
        </select>

        <label for="year-select">Year:</label>
        <select id="year-select" onchange="updateVisualization()">
            {"".join(f'<option value="{year}">{year}</option>' for year in years)}
        </select>
    </div>

    <div class="visualization">
        <h2 id="viz-title">{variables[0] if variables else ""} - Year {years[0] if years else ""}</h2>
        <img id="viz-image" src="img/{variables[0]}_{years[0]}.png" alt="Visualization" />
    </div>

    <script>
        // Initialize visualization
        updateVisualization();
    </script>
</body>
</html>
"""

        with open(web_dir / "index.html", "w") as f:
            f.write(html)

        return str(web_dir)
