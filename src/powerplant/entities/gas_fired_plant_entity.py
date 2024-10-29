from src.powerplant.entities.power_plant_entity import PowerPlant


class GasFiredPlant(PowerPlant):
    def calculate_cost_per_mwh(
        self, fuel_price: float = 0, co2_price: float = 0
    ) -> float:
        return (fuel_price / self.efficiency) + (0.3 * co2_price)

    def calculate_production(self, load: float, wind_percentage: float = 0) -> float:
        return min(self.pmax, max(self.pmin, load))
