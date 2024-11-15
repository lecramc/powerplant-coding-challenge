from typing import Optional

from src.powerplant.entities.power_plant_entity import PowerPlant


class WindTurbine(PowerPlant):
    def calculate_cost_per_mwh(
        self, fuel_price: Optional[float] = None, co2_price: Optional[float] = 0
    ) -> float:
        """Calculate the cost per MWh for the wind turbine"""
        return 0

    def calculate_production(
        self, load: float, wind_percentage: Optional[float] = 0
    ) -> float:
        """Calculate the production of the wind turbine"""
        if not wind_percentage:
            raise ValueError("No wind percentage provided")
        return min(self.pmax, self.pmax * (wind_percentage / 100))
