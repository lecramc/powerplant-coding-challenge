from typing import Dict

import pytest

from src.powerplant.entities.factories.powerplant_factories import PowerPlantFactory
from src.powerplant.usecases.get_production_plan_usecase import ProductionPlan


@pytest.mark.unit
def test_production_plan_usecase() -> None:
    # GIVEN
    load = 480
    fuel_prices: Dict[str, float] = {"gas": 20, "kerosine": 50, "co2": 10}
    wind_percentage = 60

    # Create a list of power plants
    plants = [
        PowerPlantFactory.create_gas_fired(
            name="gasplant1", efficiency=0.5, pmin=100, pmax=300
        ),
        PowerPlantFactory.create_turbojet(
            name="turbojet1", efficiency=0.3, pmin=0, pmax=200
        ),
        PowerPlantFactory.create_wind_turbine(name="windturbine1", pmax=150),
        PowerPlantFactory.create_wind_turbine(name="windturbine2", pmax=36),
    ]

    # WHEN
    use_case = ProductionPlan(plants)
    result = use_case.execute(load, fuel_prices, wind_percentage)

    # THEN
    expected_result = [
        {"name": "windturbine1", "p": 90.0},
        {"name": "windturbine2", "p": 21.6},
        {"name": "gasplant1", "p": 300.0},
        {"name": "turbojet1", "p": 68.4},
    ]
    assert result == expected_result, f"Expected {expected_result} but got {result}"
