"""Simulation Orchestrator implementation.

Provides classes and functions for orchestrating landscape simulations with
performance monitoring and error recovery.
"""

import json
import logging
import time
import traceback
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional

import numpy as np
import psutil

from ..config.manager import ConfigurationManager
from ..data.manager import InputDataManager
from ..output.manager import OutputManager
from ..state.tracker import AnnualStateTracker

# Setup logging
logger = logging.getLogger("laflammscape.orchestrator")


@dataclass
class SimulationOrchestrator:
    """Orchestrates Laflammscape simulations.

    Features:
    - Performance monitoring
    - Error recovery
    - Simulation lifecycle management
    """

    config_manager: ConfigurationManager
    input_manager: InputDataManager
    state_tracker: AnnualStateTracker
    output_manager: OutputManager

    # Simulation modules
    modules: Dict[str, Any] = field(default_factory=dict)
    module_order: List[str] = field(default_factory=list)

    # Performance monitoring
    _performance_metrics: Dict[str, Any] = field(
        default_factory=lambda: {
            "year_execution_time": [],
            "module_execution_time": {},
            "memory_usage": [],
            "cpu_usage": [],
        }
    )

    # Error tracking and recovery
    _errors: List[Dict[str, Any]] = field(default_factory=list)
    _recovery_enabled: bool = True
    _recovery_dir: Optional[str] = None
    _checkpoint_frequency: int = 10  # Create checkpoints every N years

    def __post_init__(self):
        """Initialize after dataclass creation."""
        # Set default recovery directory
        if self._recovery_dir is None:
            self._recovery_dir = str(Path.cwd() / "recovery")

    def register_module(self, name: str, module: Any, order: Optional[int] = None) -> None:
        """Register a simulation module.

        Args:
            name: Name to register the module under
            module: Module object
            order: Optional execution order (lower numbers execute first)

        Raises:
            ValueError: If a module with the same name is already registered
        """
        if name in self.modules:
            raise ValueError(f"Module '{name}' is already registered")

        self.modules[name] = module

        # Initialize performance tracking for this module
        if name not in self._performance_metrics["module_execution_time"]:
            self._performance_metrics["module_execution_time"][name] = []

        # Update module order if specified
        if order is not None:
            # Insert at specified position, extending the list if needed
            while len(self.module_order) <= order:
                self.module_order.append(None)
            self.module_order[order] = name
        else:
            # Append to the end if no order specified
            self.module_order.append(name)

        # Clean up None entries in module_order
        self.module_order = [m for m in self.module_order if m is not None]

        logger.info(f"Registered module: {name}")

    def enable_recovery(self, enabled: bool = True, checkpoint_frequency: int = 10) -> None:
        """Enable or disable recovery mechanisms.

        Args:
            enabled: Whether to enable recovery
            checkpoint_frequency: How often to create checkpoints (in years)
        """
        self._recovery_enabled = enabled
        self._checkpoint_frequency = checkpoint_frequency

    def set_recovery_directory(self, directory: str) -> None:
        """Set directory for recovery checkpoints.

        Args:
            directory: Path to recovery directory
        """
        self._recovery_dir = directory

    def run_simulation(self, num_years: int, use_tqdm: bool = False) -> None:
        """Run the simulation for a specified number of years, with progress bar and metrics."""
        logger.info(f"Starting simulation for {num_years} years")
        if use_tqdm:
            try:
                from tqdm import tqdm

                use_tqdm = True
            except ImportError:
                use_tqdm = False
                print("[INFO] tqdm not installed, progress bar will be basic.")

        # Initialize performance metrics
        start_time = time.time()
        self._performance_metrics["simulation_start_time"] = time.strftime("%Y-%m-%dT%H:%M:%S")
        self._performance_metrics["year_execution_time"] = []
        self._performance_metrics["memory_usage"] = []
        self._performance_metrics["cpu_usage"] = []

        import psutil

        process = psutil.Process()

        if use_tqdm:
            with tqdm(total=num_years, desc="Simulation Years", unit="year") as pbar:
                try:
                    for year_index in range(num_years):
                        year_start = time.time()
                        # Create recovery point if enabled
                        if self._recovery_enabled and year_index % self._checkpoint_frequency == 0:
                            recovery_path = (
                                Path(self._recovery_dir)
                                / f"checkpoint_year_{self.state_tracker.current_year}"
                            )
                            self.state_tracker.create_recovery_point(str(recovery_path))
                        # Run the year
                        self._run_year()
                        # Record resource usage
                        memory_mb = process.memory_info().rss / (1024 * 1024)
                        cpu_percent = process.cpu_percent(interval=0.1)
                        self._performance_metrics["memory_usage"].append(memory_mb)
                        self._performance_metrics["cpu_usage"].append(cpu_percent)
                        year_elapsed = time.time() - year_start
                        self._performance_metrics["year_execution_time"].append(year_elapsed)
                        pbar.set_postfix(
                            {
                                "RAM (MB)": f"{memory_mb:.1f}",
                                "CPU (%)": f"{cpu_percent:.1f}",
                            }
                        )
                        pbar.update(1)
                        logger.info(f"Completed year {self.state_tracker.current_year}")
                except Exception as e:
                    self._handle_error(e)
                    if self._recovery_enabled:
                        logger.warning(
                            f"Attempting recovery after error in year {self.state_tracker.current_year}"
                        )
                        if not self._attempt_recovery():
                            logger.error("Recovery failed, stopping simulation")
                    else:
                        logger.error("Recovery disabled, stopping simulation")
                finally:
                    total_time = time.time() - start_time
                    self._performance_metrics["total_execution_time"] = total_time
                    self._performance_metrics["simulation_end_time"] = time.strftime(
                        "%Y-%m-%dT%H:%M:%S"
                    )
                    logger.info(f"Simulation completed in {total_time:.2f} seconds")
                    # Print summary
                    print("\n--- Simulation Performance Summary ---")
                    print(f"Total time: {total_time:.2f} seconds")
                    if self._performance_metrics["year_execution_time"]:
                        print(
                            f"Mean year time: {np.mean(self._performance_metrics['year_execution_time']):.2f} s"
                        )
                        print(
                            f"Max year time: {np.max(self._performance_metrics['year_execution_time']):.2f} s"
                        )
                    if self._performance_metrics["memory_usage"]:
                        print(
                            f"Mean memory: {np.mean(self._performance_metrics['memory_usage']):.1f} MB"
                        )
                        print(
                            f"Max memory: {np.max(self._performance_metrics['memory_usage']):.1f} MB"
                        )
                    if self._performance_metrics["cpu_usage"]:
                        print(f"Mean CPU: {np.mean(self._performance_metrics['cpu_usage']):.1f}%")
                        print(f"Max CPU: {np.max(self._performance_metrics['cpu_usage']):.1f}%")
                    print("--------------------------------------\n")
        else:
            print("Simulation Progress:")
            try:
                for year_index in range(num_years):
                    year_start = time.time()
                    # Create recovery point if enabled
                    if self._recovery_enabled and year_index % self._checkpoint_frequency == 0:
                        recovery_path = (
                            Path(self._recovery_dir)
                            / f"checkpoint_year_{self.state_tracker.current_year}"
                        )
                        self.state_tracker.create_recovery_point(str(recovery_path))
                    # Run the year
                    self._run_year()
                    # Record resource usage
                    memory_mb = process.memory_info().rss / (1024 * 1024)
                    cpu_percent = process.cpu_percent(interval=0.1)
                    self._performance_metrics["memory_usage"].append(memory_mb)
                    self._performance_metrics["cpu_usage"].append(cpu_percent)
                    year_elapsed = time.time() - year_start
                    self._performance_metrics["year_execution_time"].append(year_elapsed)
                    print(
                        f"  Year {year_index+1}/{num_years} complete in {year_elapsed:.2f}s, Mem: {memory_mb:.1f}MB, CPU: {cpu_percent:.1f}%"  # noqa: E501
                    )
                    logger.info(f"Completed year {self.state_tracker.current_year}")
            except Exception as e:
                self._handle_error(e)
                if self._recovery_enabled:
                    logger.warning(
                        f"Attempting recovery after error in year {self.state_tracker.current_year}"
                    )
                    if not self._attempt_recovery():
                        logger.error("Recovery failed, stopping simulation")
                else:
                    logger.error("Recovery disabled, stopping simulation")
            finally:
                total_time = time.time() - start_time
                self._performance_metrics["total_execution_time"] = total_time
                self._performance_metrics["simulation_end_time"] = time.strftime(
                    "%Y-%m-%dT%H:%M:%S"
                )
                logger.info(f"Simulation completed in {total_time:.2f} seconds")
                # Print summary
                print("\n--- Simulation Performance Summary ---")
                print(f"Total time: {total_time:.2f} seconds")
                if self._performance_metrics["year_execution_time"]:
                    print(
                        f"Mean year time: {np.mean(self._performance_metrics['year_execution_time']):.2f} s"
                    )
                    print(
                        f"Max year time: {np.max(self._performance_metrics['year_execution_time']):.2f} s"
                    )
                if self._performance_metrics["memory_usage"]:
                    print(
                        f"Mean memory: {np.mean(self._performance_metrics['memory_usage']):.1f} MB"
                    )
                    print(f"Max memory: {np.max(self._performance_metrics['memory_usage']):.1f} MB")
                if self._performance_metrics["cpu_usage"]:
                    print(f"Mean CPU: {np.mean(self._performance_metrics['cpu_usage']):.1f}%")
                    print(f"Max CPU: {np.max(self._performance_metrics['cpu_usage']):.1f}%")
                print("--------------------------------------\n")

    def _run_year(self) -> None:
        """Run a single year of simulation."""
        year_start_time = time.time()

        # Advance to next year
        self.state_tracker.advance_year()
        self.state_tracker.current_year

        # Determine modules to run based on order
        module_names = self.module_order or list(self.modules.keys())

        # Run modules sequentially
        for module_name in module_names:
            if module_name in self.modules:
                self._run_module(module_name, self.modules[module_name])

        # Record year execution time
        year_execution_time = time.time() - year_start_time
        self._performance_metrics["year_execution_time"].append(year_execution_time)

    def _run_module(self, module_name: str, module: Any) -> None:
        """Run a single simulation module.

        Args:
            module_name: Name of the module to run
            module: Module object to run
        """
        module_start_time = time.time()
        logger.debug(f"Running module: {module_name}")

        # Get current state
        current_state = self.state_tracker.get_state()

        # Execute module based on its interface
        if hasattr(module, "apply_to_state"):
            # Module directly modifies the state
            module.apply_to_state(current_state)
        elif hasattr(module, "process_state"):
            # Module returns a processed state
            updated_state = module.process_state(current_state)
            # Update variables that have changed
            for var_name in updated_state.state_variables:
                if var_name in current_state.state_variables:
                    # Check if variable has changed using NumPy operations
                    current_var = current_state.state_variables[var_name]
                    updated_var = updated_state.state_variables[var_name]
                    # Use numpy comparison for all arrays
                    if isinstance(current_var, np.ndarray) and isinstance(updated_var, np.ndarray):
                        if not np.array_equal(current_var, updated_var):
                            current_state.set_variable(var_name, updated_var)
                    else:
                        if current_var != updated_var:
                            current_state.set_variable(var_name, updated_var)
                else:
                    # New variable
                    current_state.set_variable(var_name, updated_state.state_variables[var_name])
        elif hasattr(module, "run"):
            # Module has a generic run method
            module.run()
        else:
            # Try to call the module directly
            module(current_state)

        # Ensure all state variables remain as NumPy arrays (no conversion needed)

        # Record module execution time
        module_execution_time = time.time() - module_start_time
        self._performance_metrics["module_execution_time"][module_name].append(
            module_execution_time
        )
        logger.warning(f"Module '{module_name}' processed in {module_execution_time:.3f} seconds.")

    def _record_resource_usage(self) -> None:
        """Record system resource usage."""
        process = psutil.Process()
        memory_info = process.memory_info()

        # Memory usage in MB
        memory_mb = memory_info.rss / (1024 * 1024)
        self._performance_metrics["memory_usage"].append(memory_mb)

        # CPU usage as percentage
        cpu_percent = process.cpu_percent(interval=0.1)
        self._performance_metrics["cpu_usage"].append(cpu_percent)

    def _handle_error(self, error: Exception, module_name: Optional[str] = None) -> None:
        """Handle a simulation error.

        Args:
            error: Exception that occurred
            module_name: Name of the module that caused the error, if applicable
        """
        error_info = {
            "year": self.state_tracker.current_year,
            "error_type": type(error).__name__,
            "error_message": str(error),
            "traceback": traceback.format_exc(),
            "timestamp": datetime.now().isoformat(),
        }

        if module_name:
            error_info["module"] = module_name

        self._errors.append(error_info)

        # Log error
        logger.error(f"Error in simulation: {error_info}")
        logger.debug(traceback.format_exc())

    def _attempt_recovery(self) -> bool:
        """Attempt to recover from an error using the most recent checkpoint.

        Returns:
            True if recovery was successful, False otherwise
        """
        # Get available checkpoint years
        checkpoint_years = self.state_tracker.get_checkpoint_years()

        if not checkpoint_years:
            logger.warning("No checkpoints available for recovery")
            return False

        # Find the most recent checkpoint before the current year
        current_year = self.state_tracker.current_year
        recovery_year = max([y for y in checkpoint_years if y < current_year], default=None)

        if recovery_year is None:
            logger.warning("No valid checkpoints for recovery")
            return False

        # Attempt recovery
        recovery_path = Path(self._recovery_dir) / f"checkpoint_year_{recovery_year}"
        if not recovery_path.exists():
            logger.warning(f"Recovery checkpoint not found: {recovery_path}")
            return False

        try:
            logger.info(f"Recovering from checkpoint for year {recovery_year}")

            # Load the checkpoint
            recovery_success = self.state_tracker.recover_from_point(str(recovery_path))

            if recovery_success:
                logger.info(f"Successfully recovered to year {recovery_year}")
                return True
            else:
                logger.warning("Recovery failed")
                return False
        except Exception as e:
            logger.error(f"Error during recovery: {e}")
            logger.debug(traceback.format_exc())
            return False

    def get_performance_summary(self) -> Dict[str, Any]:
        """Get a summary of simulation performance.

        Returns:
            Dictionary of performance metrics
        """
        year_times = self._performance_metrics["year_execution_time"]

        summary = {
            "total_execution_time": self._performance_metrics.get(
                "total_execution_time", sum(year_times) if year_times else 0
            ),
            "mean_year_execution_time": (sum(year_times) / len(year_times) if year_times else 0),
            "module_execution_time": {
                name: sum(times) / len(times) if times else 0
                for name, times in self._performance_metrics["module_execution_time"].items()
            },
            "memory_usage": {
                "mean": (
                    np.mean(self._performance_metrics["memory_usage"])
                    if self._performance_metrics["memory_usage"]
                    else 0
                ),
                "max": (
                    np.max(self._performance_metrics["memory_usage"])
                    if self._performance_metrics["memory_usage"]
                    else 0
                ),
            },
            "cpu_usage": {
                "mean": (
                    np.mean(self._performance_metrics["cpu_usage"])
                    if self._performance_metrics["cpu_usage"]
                    else 0
                ),
                "max": (
                    np.max(self._performance_metrics["cpu_usage"])
                    if self._performance_metrics["cpu_usage"]
                    else 0
                ),
            },
            "errors": len(self._errors),
        }

        return summary

    def export_performance_metrics(self, output_path: str) -> None:
        """Export performance metrics to a JSON file.

        Args:
            output_path: Path to write the metrics file

        Raises:
            IOError: If the file cannot be written
        """

        # Convert numpy values to Python primitives for JSON serialization
        def convert_to_serializable(obj):
            if isinstance(obj, np.ndarray):
                return obj.tolist()
            elif isinstance(obj, np.number):
                return obj.item()
            elif isinstance(obj, dict):
                return {k: convert_to_serializable(v) for k, v in obj.items()}
            elif isinstance(obj, list):
                return [convert_to_serializable(v) for v in obj]
            else:
                return obj

        # Prepare metrics for export
        metrics = convert_to_serializable(self._performance_metrics)

        # Add summary metrics
        metrics["summary"] = self.get_performance_summary()

        # Write to file
        with open(output_path, "w") as f:
            json.dump(metrics, f, indent=2)

        logger.info(f"Performance metrics exported to {output_path}")

    def export_error_log(self, output_path: str) -> None:
        """Export error log to a JSON file.

        Args:
            output_path: Path to write the error log file

        Raises:
            IOError: If the file cannot be written
        """
        with open(output_path, "w") as f:
            json.dump(self._errors, f, indent=2)

        logger.info(f"Error log exported to {output_path}")

    def clear_errors(self) -> None:
        """Clear the error log."""
        self._errors.clear()
        logger.info("Error log cleared")
