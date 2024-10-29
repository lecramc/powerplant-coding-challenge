from abc import ABC, abstractmethod


class PowerPlant(ABC):
    def __init__(
        self,
        name: str,
        type: str,
        efficiency: float,
        pmin: float,
        pmax: float,
        cost: float = 0,
    ):
        self.name: str = name
        self.type: str = type
        self.efficiency: float = efficiency
        self.pmin: float = pmin
        self.pmax: float = pmax
        self.cost: float = cost

    @abstractmethod
    def calculate_cost_per_mwh(
        self, fuel_price: float = 0, co2_price: float = 0
    ) -> float:
        pass

    @abstractmethod
    def calculate_production(self, load: float, wind_percentage: float = 0) -> float:
        pass

    def validate_production_limits(self, production: float) -> bool:
        return self.pmin <= production <= self.pmax
