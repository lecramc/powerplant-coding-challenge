from typing import Optional

from src.powerplant.entities.power_plant_entity import PowerPlant


class TurboJet(PowerPlant):
    def calculate_cost_per_mwh(
        self, fuel_price: Optional[float] = 0, co2_price: Optional[float] = 0
    ) -> float:
        if not fuel_price:
            raise ValueError("No fuel price provided")
        return fuel_price / self.efficiency

    def calculate_production(
        self, load: float, wind_percentage: Optional[float] = 0
    ) -> float:
        return min(self.pmax, max(self.pmin, load))
