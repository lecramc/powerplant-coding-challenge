import pytest

from src.powerplant.entities.gas_fired_plant_entity import GasFiredPlant
from src.powerplant.entities.turbo_jet_entity import TurboJet
from src.powerplant.entities.wind_turbine_entity import WindTurbine


@pytest.mark.unit
def test_gas_fired_plant_cost() -> None:
    """Test the gas fired plant cost calculation"""
    plant = GasFiredPlant("gasplant1", "gasfired", 0.5, 100, 300)
    assert plant.calculate_cost_per_mwh(20, 10) == 43


@pytest.mark.unit
def test_wind_turbine_production() -> None:
    """Test the wind turbine production calculation"""
    plant = WindTurbine("windplant1", "windturbine", 1.0, 0, 150)
    assert plant.calculate_production(100, wind_percentage=50) == 75


@pytest.mark.unit
def test_turbojet_cost() -> None:
    """Test the turbojet cost calculation"""
    plant = TurboJet("turbojet1", "turbojet", 0.3, 0, 200)
    assert plant.calculate_cost_per_mwh(50) == pytest.approx(166.67, 0.01)
