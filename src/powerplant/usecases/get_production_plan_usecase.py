from typing import List, Dict

from src.powerplant.entities.gas_fired_plant_entity import GasFiredPlant
from src.powerplant.entities.power_plant_entity import PowerPlant
from src.powerplant.entities.turbo_jet_entity import TurboJet
from src.powerplant.entities.wind_turbine_entity import WindTurbine


class ProductionPlan:
    def __init__(self, plants: List[PowerPlant]):
        self.plants: List[PowerPlant] = plants

    def execute(self, load: float, fuel_prices: Dict[str, float], wind_percentage: float) -> List[Dict[str, float]]:
        self._calculate_production_costs(fuel_prices)

        self.plants.sort(key=lambda plant: plant.cost)

        production_plan = self._allocate_production(load, wind_percentage)

        self._include_non_active_plants(production_plan)

        return production_plan

    def _calculate_production_costs(self, fuel_prices: Dict[str, float]) -> None:
        """Calculates the cost per MWh for each power station according to its type and fuel prices."""
        for plant in self.plants:
            if isinstance(plant, GasFiredPlant):
                plant.cost = plant.calculate_cost_per_mwh(fuel_prices["gas"], fuel_prices["co2"])
                continue
            elif isinstance(plant, TurboJet):
                plant.cost = plant.calculate_cost_per_mwh(fuel_prices["kerosine"])
                continue
            plant.cost = plant.calculate_cost_per_mwh()

    def _allocate_production(self, load: float, wind_percentage: float) -> List[Dict[str, float]]:
        """Allocates production to meet the requested workload, respecting the order of merit"""
        production_plan: List[Dict[str, float]] = []
        total_production: float = 0.0

        for plant in self.plants:
            if total_production >= load:
                break

            # Calculate production for each plant
            production = self._calculate_plant_production(plant, load - total_production, wind_percentage)

            if production >= plant.pmin:
                production_plan.append({"name": plant.name, "p": production})
                total_production += production

        return production_plan

    @staticmethod
    def _calculate_plant_production( plant: PowerPlant, remaining_load: float, wind_percentage: float) -> float:
        """Calculates the production for a specific plant, taking into account its limits. """
        production = plant.calculate_production(remaining_load, wind_percentage)
        return round(min(production, plant.pmax), 1)


    def _include_non_active_plants(self, production_plan: List[Dict[str, float]]) -> None:
        """Adds unused power plants to the production plan with a production of 0.0"""
        for plant in self.plants:
            if all(entry["name"] != plant.name for entry in production_plan):
                production_plan.append({"name": plant.name, "p": 0.0})
