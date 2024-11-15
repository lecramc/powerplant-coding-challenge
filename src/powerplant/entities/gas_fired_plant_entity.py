from src.powerplant.entities.power_plant_entity import PowerPlant


class GasFiredPlant(PowerPlant):
    def calculate_cost_per_mwh(
        self, fuel_price: float = 0, co2_price: float = 0
    ) -> float:
        """Calculate the cost per MWh for the gas fired plant"""
        return (fuel_price / self.efficiency) + (0.3 * co2_price)

    def calculate_production(self, load: float, wind_percentage: float = 0) -> float:
        """Calculate the production of the gas fired plant"""
        return min(self.pmax, max(self.pmin, load))
