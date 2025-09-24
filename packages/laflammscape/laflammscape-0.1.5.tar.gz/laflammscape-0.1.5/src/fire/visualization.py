"""Visualization utilities for fire spread simulations.

Provides functions to visualize burn time maps, fire spread patterns,
and other fire behavior metrics.
"""

from typing import Any, List, Optional, Tuple

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap


def plot_burn_times(
    burn_times,
    title: str = "Fire Spread - Burn Times",
    save_path: Optional[str] = None,
    show: bool = True,
    figsize: Tuple[int, int] = (10, 8),
) -> None:
    """Visualize burn times from fire spread simulation.

    Args:
        burn_times: 2D array of burn times in minutes (NumPy or TensorFlow)
        title: Plot title
        save_path: Path to save the figure (if None, figure is not saved)
        show: Whether to display the figure
        figsize: Figure size (width, height) in inches
    """
    # Ensure input is a NumPy array
    burn_times = np.asarray(burn_times)
    # Create a custom colormap (unburned areas in gray, burn times in hot colors)
    # Define colors for the colormap
    colors = [(0.8, 0.8, 0.8)]  # Light gray for unburned
    # Add a gradient from yellow to red for burn times
    colors.extend([(1, 1, 0), (1, 0.5, 0), (1, 0, 0), (0.5, 0, 0)])
    burn_cmap = LinearSegmentedColormap.from_list("burn_times", colors)

    # Create a copy of burn times for visualization
    vis_times = burn_times.copy()

    # Set unburned areas (infinity) to a value beyond the maximum burn time
    if np.any(np.isinf(vis_times)):
        max_time = np.max(vis_times[~np.isinf(vis_times)]) if np.any(~np.isinf(vis_times)) else 0
        vis_times[np.isinf(vis_times)] = max_time * 1.5

    # Set negative values (e.g., -1 for unburned) to a value beyond the maximum
    if np.any(vis_times < 0):
        max_time = np.max(vis_times[vis_times >= 0]) if np.any(vis_times >= 0) else 0
        vis_times[vis_times < 0] = max_time * 1.5

    # Create the plot
    plt.figure(figsize=figsize)
    img = plt.imshow(vis_times, cmap=burn_cmap)
    plt.colorbar(img, label="Burn Time (minutes)")
    plt.title(title)

    # Add a legend or text annotation for unburned areas
    if np.any(np.isinf(burn_times)) or np.any(burn_times < 0):
        plt.text(
            0.01,
            0.01,
            "Gray areas: Unburned",
            transform=plt.gca().transAxes,
            color="black",
            bbox=dict(facecolor="white", alpha=0.7),
        )

    # Save the figure if a path is provided
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches="tight")

    # Show the figure if requested
    if show:
        plt.show()
    else:
        plt.close()


def plot_fire_comparison(
    burn_times_list: List[Any],
    titles: List[str],
    main_title: str = "Fire Spread Comparison",
    save_path: Optional[str] = None,
    show: bool = True,
    figsize: Tuple[int, int] = (15, 10),
) -> None:
    """Create a side-by-side comparison of multiple fire spread simulations.

    Args:
        burn_times_list: List of 2D arrays of burn times (NumPy or TensorFlow)
        titles: List of titles for each subplot
        main_title: Main title for the entire figure
        save_path: Path to save the figure (if None, figure is not saved)
        show: Whether to display the figure
        figsize: Figure size (width, height) in inches
    """
    # Ensure all inputs are NumPy arrays
    burn_times_list = [np.asarray(bt) for bt in burn_times_list]
    colors = [(0.8, 0.8, 0.8)]  # Light gray for unburned
    # Add a gradient from yellow to red for burn times
    colors.extend([(1, 1, 0), (1, 0.5, 0), (1, 0, 0), (0.5, 0, 0)])
    burn_cmap = LinearSegmentedColormap.from_list("burn_times", colors)

    # Create the figure with subplots
    n_plots = len(burn_times_list)
    fig, axes = plt.subplots(1, n_plots, figsize=figsize)

    # If only one plot, convert axes to an array for consistent indexing
    if n_plots == 1:
        axes = np.array([axes])

    # Find the global maximum burn time for consistent color scaling
    max_time = 0
    for burn_times in burn_times_list:
        if np.any(~np.isinf(burn_times) & (burn_times >= 0)):
            max_burn = np.max(burn_times[(~np.isinf(burn_times)) & (burn_times >= 0)])
            max_time = max(max_time, max_burn)

    # Plot each burn time array
    for i, (burn_times, title) in enumerate(zip(burn_times_list, titles)):
        # Create a copy for visualization
        vis_times = burn_times.copy()

        # Set unburned areas to a value beyond the maximum
        if np.any(np.isinf(vis_times)) or np.any(vis_times < 0):
            vis_times[np.isinf(vis_times) | (vis_times < 0)] = max_time * 1.5

        # Plot the burn times
        im = axes[i].imshow(vis_times, cmap=burn_cmap)
        axes[i].set_title(title)
        axes[i].axis("o")  # Hide axes for cleaner appearance

    # Add a colorbar to the right of the subplots
    cbar_ax = fig.add_axes([0.92, 0.15, 0.02, 0.7])
    cbar = fig.colorbar(im, cax=cbar_ax)
    cbar.set_label("Burn Time (minutes)")

    # Add overall title
    fig.suptitle(main_title, fontsize=16)

    # Adjust layout
    plt.tight_layout(rect=[0, 0, 0.9, 0.95])

    # Save the figure if a path is provided
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches="tight")

    # Show the figure if requested
    if show:
        plt.show()
    else:
        plt.close()


def animate_fire_spread(
    burn_times,
    time_steps: int = 20,
    interval: int = 200,
    title: str = "Fire Spread Animation",
    save_path: Optional[str] = None,
    figsize: Tuple[int, int] = (10, 8),
) -> None:
    """Create an animation of fire spread over time.

    Args:
        burn_times: 2D array of burn times in minutes (NumPy or TensorFlow)
        time_steps: Number of frames in the animation
        interval: Time between frames in milliseconds
        title: Animation title
        save_path: Path to save the animation (if None, animation is not saved)
        figsize: Figure size (width, height) in inches
    """
    import matplotlib.animation as animation

    # Ensure input is a NumPy array
    burn_times = np.asarray(burn_times)
    # Create a copy for visualization
    vis_times = burn_times.copy()

    # Replace infinite values with a large number
    vis_times[np.isinf(vis_times) | (vis_times < 0)] = np.nan

    # Get the maximum finite burn time
    if np.any(~np.isnan(vis_times)):
        max_time = np.nanmax(vis_times)
    else:
        max_time = 1.0  # Default if all values are NaN

    # Create time points for the animation
    time_points = np.linspace(0, max_time, time_steps)

    # Create the figure and axis
    fig, ax = plt.subplots(figsize=figsize)
    plt.title(title)

    # Define colors for the colormap
    colors = [(0.8, 0.8, 0.8, 0.3)]  # Transparent gray for unburned
    # Add a gradient from yellow to red for burn times
    colors.extend([(1, 1, 0, 1), (1, 0.5, 0, 1), (1, 0, 0, 1), (0.5, 0, 0, 1)])
    burn_cmap = LinearSegmentedColormap.from_list("burn_times", colors)

    # Initialize the plot with empty data
    fire_mask = np.zeros_like(burn_times, dtype=bool)
    img = ax.imshow(fire_mask, cmap=burn_cmap, interpolation="nearest")

    # Add timestamp text
    timestamp = ax.text(
        0.02,
        0.95,
        "",
        transform=ax.transAxes,
        color="black",
        fontsize=12,
        bbox=dict(facecolor="white", alpha=0.7),
    )

    # Animation update function
    def update(frame):
        # Current time
        current_time = time_points[frame]

        # Update fire mask - cells that have burned by this time
        fire_mask = (vis_times <= current_time) & (~np.isnan(vis_times))

        # Update the image data
        img.set_array(fire_mask)

        # Update timestamp
        timestamp.set_text(f"Time: {current_time:.1f} minutes")

        return img, timestamp

    # Create the animation
    anim = animation.FuncAnimation(fig, update, frames=time_steps, interval=interval, blit=True)

    # Save the animation if a path is provided
    if save_path:
        anim.save(save_path, writer="pillow", fps=30)

    # Display the animation
    plt.tight_layout()
    plt.show()


def create_fuel_model_legend(fuel_model_ids, fuel_mapping_module, save_path=None):
    """Create a legend mapping fuel model IDs to names/descriptions.
    Args:
        fuel_model_ids: Iterable of integer fuel model IDs (e.g., from np.unique() or tf.unique())
        fuel_mapping_module: FuelMappingModule instance
        save_path: Optional path to save the legend as a text file
    Returns:
        legend: dict mapping model_id -> {"name": str, "description": str}
    """
    # Ensure input is a NumPy array
    fuel_model_ids = np.asarray(fuel_model_ids)
    legend = {}
    for model_id in fuel_model_ids:
        model = fuel_mapping_module.get_fuel_model(int(model_id))
        if model is not None:
            legend[model_id] = {
                "name": getattr(model, "name", f"Model {model_id}"),
                "description": getattr(model, "description", ""),
            }
        else:
            legend[model_id] = {
                "name": f"Unknown ({model_id})",
                "description": "",
            }
    if save_path:
        with open(save_path, "w") as f:
            for model_id, info in legend.items():
                f.write(f"Fuel Model {model_id}: {info['name']} - {info['description']}\n")
    return legend


def animate_vegetation_change(
    veg_type_grids=None,
    category_map=None,
    save_path=None,
    interval=200,
    figsize=(10, 8),
    state_tracker=None,
    years=None,
    debug_save_frames=False,
):
    """Create a GIF animation of eco_state changes over time.
    Args:
        veg_type_grids: List of 2D numpy arrays (one per year). Ignored if state_tracker is provided.
        category_map: Dict mapping int eco_state to name (for legend/colors). If None, will use default or code values.
        save_path: Path to save the GIF (should end with .gif)
        interval: Delay between frames in ms
        figsize: Figure size
        state_tracker: Optional AnnualStateTracker. If provided, loads each year's eco_state grid.
        years: Optional list of years to visualize (default: all years in state_tracker)
        debug_save_frames: If True, saves the first few frames as PNGs for inspection.
    Example usage:
        category_map = {
            26: "California",
            27: "Nevada",
            28: "Oregon",
            32: "Arizona",
            33: "Utah",
        }
        animate_vegetation_change(veg_type_grids, category_map=category_map, save_path="veg_states.gi")
    """
    import matplotlib.animation as animation
    import matplotlib.colors as mcolors
    import matplotlib.pyplot as plt
    import numpy as np

    try:
        from tqdm import tqdm

        use_tqdm = True
    except ImportError:
        use_tqdm = False

        def tqdm(x, **kwargs):
            return x

    if state_tracker is not None:
        if years is None:
            try:
                years = sorted(state_tracker.states.keys())
            except AttributeError:
                raise ValueError(
                    "state_tracker must have a .states dict or specify years explicitly."
                )
        veg_type_grids = []
        print(f"Loading eco_state grids for {len(years)} years...")
        for year in (tqdm(years, desc="Loading frames for GIF") if use_tqdm else years):
            state = state_tracker.get_state(year)
            veg_grid = state.get_variable("eco_state")
            veg_grid = np.asarray(veg_grid)
            veg_grid = veg_grid.astype(int)
            veg_type_grids.append(veg_grid)
            print(year, np.unique(veg_grid))
    elif veg_type_grids is None:
        raise ValueError("Must provide either veg_type_grids or state_tracker.")

    veg_type_grids = [np.asarray(grid).astype(int) for grid in veg_type_grids]

    # Get all unique vegetation types across all frames
    all_types = sorted(set(np.concatenate([np.unique(grid) for grid in veg_type_grids])))
    type_to_index = {t: i for i, t in enumerate(all_types)}
    index_to_type = {i: t for i, t in enumerate(all_types)}
    # Remap all grids to 0-based indices
    remapped_grids = [np.vectorize(type_to_index.get)(grid) for grid in veg_type_grids]

    # If no category_map is provided, generate a default mapping (code to string)
    if category_map is None:
        category_map = {t: str(t) for t in all_types}

    # Assign a color to each type
    cmap = plt.get_cmap("tab20", len(all_types))
    norm = mcolors.BoundaryNorm(
        boundaries=np.arange(len(all_types) + 1) - 0.5, ncolors=len(all_types)
    )

    fig, ax = plt.subplots(figsize=figsize)
    im = ax.imshow(remapped_grids[0], cmap=cmap, norm=norm)
    cbar = plt.colorbar(im, ax=ax, ticks=range(len(all_types)))
    # Set colorbar tick labels to vegetation type names (state names) if category_map is provided
    cbar.ax.set_yticklabels(
        [category_map.get(index_to_type[i], str(index_to_type[i])) for i in range(len(all_types))]
    )
    ax.set_title("Vegetation Type (Year 0)")

    if debug_save_frames:
        for i, grid in enumerate(remapped_grids[:5]):
            plt.imsave(f"veg_frame_debug_{i}.png", grid, cmap=cmap, norm=norm)

    frame_range = (
        tqdm(range(len(remapped_grids)), desc="Rendering GIF frames")
        if use_tqdm
        else range(len(remapped_grids))
    )

    def update(frame):
        im.set_data(remapped_grids[frame])
        ax.set_title(
            f"Vegetation Type (Year {years[frame] if state_tracker is not None else frame})"
        )
        fig.canvas.draw_idle()
        return [im]

    if use_tqdm:
        frame_range.reset()

    anim = animation.FuncAnimation(fig, update, frames=frame_range, interval=interval, blit=True)
    anim.save(save_path, writer="pillow")
    plt.close(fig)
    if use_tqdm:
        frame_range.close()
