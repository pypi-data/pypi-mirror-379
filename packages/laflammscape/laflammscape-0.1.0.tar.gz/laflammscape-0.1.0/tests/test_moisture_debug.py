#!/usr/bin/env python3

import os
import sys

import numpy as np

# Add the src directory to the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

from src.fire.behavior import FuelModel
from src.fire.simulation import FireSimulationInterface
from src.state.representation import StateRepresentation


def test_moisture_extinction():
    """Test moisture extinction values and fire spread behavior."""

    # Create a small test state
    size = 10
    state = StateRepresentation(grid_shape=(size, size), cell_size=90.0)

    # Create fuel models
    fuel_models = [
        FuelModel(
            id="GR1",
            loading={
                "1hr": 0.10,
                "10hr": 0.00,
                "100hr": 0.00,
                "herb": 0.30,
                "woody": 0.00,
            },
            sav={"1hr": 2200, "herb": 2000, "woody": None},
            depth=0.4,
            moisture_extinction=15,  # 15% moisture extinction
            heat_content=8000,
        ),
        FuelModel(
            id="GR3",
            loading={
                "1hr": 0.10,
                "10hr": 0.40,
                "100hr": 0.00,
                "herb": 1.50,
                "woody": 0.00,
            },
            sav={"1hr": 1500, "herb": 1800, "woody": None},
            depth=2.0,
            moisture_extinction=30,  # 30% moisture extinction
            heat_content=8000,
        ),
    ]

    # Set up landscape with different moisture scenarios
    fuel_model_grid = np.ones((size, size), dtype=np.int32) * 0  # Use fuel model 0 (GR1)

    # Test different moisture scenarios
    scenarios = [
        {"name": "Dry", "m1hr": 4.0, "m10hr": 6.0, "m100hr": 8.0},
        {"name": "Moderate", "m1hr": 8.0, "m10hr": 10.0, "m100hr": 12.0},
        {"name": "Wet", "m1hr": 12.0, "m10hr": 14.0, "m100hr": 16.0},
        {"name": "Very Wet", "m1hr": 18.0, "m10hr": 20.0, "m100hr": 22.0},
    ]

    for scenario in scenarios:
        print(f"\n=== {scenario['name']} Scenario ===")
        print(
            f"Moisture: 1hr={scenario['m1hr']}%, 10hr={scenario['m10hr']}%, 100hr={scenario['m100hr']}%"
        )
        print("Fuel model moisture extinction: 15%")

        # Set up state variables
        state.set_variable("fuel_model", fuel_model_grid)
        state.set_variable("fuel_moisture_1hr", np.full((size, size), scenario["m1hr"]))
        state.set_variable("fuel_moisture_10hr", np.full((size, size), scenario["m10hr"]))
        state.set_variable("fuel_moisture_100hr", np.full((size, size), scenario["m100hr"]))
        state.set_variable("fuel_moisture_herb", np.full((size, size), 60.0))
        state.set_variable("fuel_moisture_woody", np.full((size, size), 90.0))
        state.set_variable("slope", np.zeros((size, size)))
        state.set_variable("aspect", np.zeros((size, size)))
        state.set_variable("weather_wind_speed", np.full((size, size), 10.0))
        state.set_variable("weather_wind_direction", np.zeros((size, size)))

        # Create fire simulation
        fire_sim = FireSimulationInterface(fuel_models=fuel_models)

        # Set ignition point at center
        burn_times = np.full((size, size), np.inf)
        burn_times[size // 2, size // 2] = 0.0

        # Run simulation for 8 hours (480 minutes) to allow fire spread
        result = fire_sim.simulate_spread(
            burn_times=burn_times,
            fuel_models=fuel_model_grid,
            moisture_1hr=state.get_variable("fuel_moisture_1hr"),
            moisture_10hr=state.get_variable("fuel_moisture_10hr"),
            moisture_100hr=state.get_variable("fuel_moisture_100hr"),
            moisture_herb=state.get_variable("fuel_moisture_herb"),
            moisture_woody=state.get_variable("fuel_moisture_woody"),
            wind_speed=state.get_variable("weather_wind_speed"),
            wind_direction=state.get_variable("weather_wind_direction"),
            slope=state.get_variable("slope"),
            aspect=state.get_variable("aspect"),
            spatial_resolution=90.0,
            burn_time_minutes=480.0,
        )

        # Count burned cells
        burned_cells = np.sum(result < np.inf)
        print(f"Burned cells: {burned_cells} out of {size*size}")

        # Check if fire spread beyond ignition point
        if burned_cells > 1:
            print("✓ Fire spread occurred")
            min_time = np.min(result[result < np.inf])
            max_time = np.max(result[result < np.inf])
            print(f"  Burn time range: {min_time:.1f} to {max_time:.1f} minutes")
        else:
            print("✗ Fire did not spread (moisture extinction likely triggered)")

        # Check moisture extinction logic
        m1hr = scenario["m1hr"]
        m10hr = scenario["m10hr"]
        m100hr = scenario["m100hr"]
        mext = 15.0  # GR1 moisture extinction

        print("Moisture extinction check:")
        print(f"  1hr moisture ({m1hr}%) > extinction ({mext}%)? {m1hr > mext}")
        print(f"  10hr moisture ({m10hr}%) > extinction ({mext}%)? {m10hr > mext}")
        print(f"  100hr moisture ({m100hr}%) > extinction ({mext}%)? {m100hr > mext}")

        should_burn = not (m1hr > mext or m10hr > mext or m100hr > mext)
        print(f"  Should burn: {should_burn}")


if __name__ == "__main__":
    test_moisture_extinction()
