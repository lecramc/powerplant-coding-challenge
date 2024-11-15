from src.powerplant.entities.gas_fired_plant_entity import GasFiredPlant
from src.powerplant.entities.turbo_jet_entity import TurboJet
from src.powerplant.entities.wind_turbine_entity import WindTurbine


class PowerPlantFactory:
    """Factory to create power plants"""

    @staticmethod
    def create_gas_fired(
        name: str = "gasplant",
        efficiency: float = 0.5,
        pmin: float = 100,
        pmax: float = 300,
    ) -> GasFiredPlant:
        """Create a gas fired plant"""
        return GasFiredPlant(
            name=name, type="gasfired", efficiency=efficiency, pmin=pmin, pmax=pmax
        )

    @staticmethod
    def create_turbojet(
        name: str = "turbojet",
        efficiency: float = 0.3,
        pmin: float = 0,
        pmax: float = 200,
    ) -> TurboJet:
        """Create a turbojet"""
        return TurboJet(
            name=name, type="turbojet", efficiency=efficiency, pmin=pmin, pmax=pmax
        )

    @staticmethod
    def create_wind_turbine(
        name: str = "windturbine", pmax: float = 150
    ) -> WindTurbine:
        """Create a wind turbine"""
        return WindTurbine(
            name=name, type="windturbine", efficiency=1.0, pmin=0, pmax=pmax
        )
