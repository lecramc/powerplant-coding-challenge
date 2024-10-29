from typing import List, Dict, Tuple

from src.powerplant.entities.gas_fired_plant_entity import GasFiredPlant
from src.powerplant.entities.power_plant_entity import PowerPlant
from src.powerplant.entities.turbo_jet_entity import TurboJet
from src.powerplant.entities.wind_turbine_entity import WindTurbine


def convert_request_to_entities(request:ProductionPlanRequest) -> Tuple[float, Dict[str, float], float, List[PowerPlant]]:
    load = request.load
    fuel_prices = {
        "gas": request.fuels.gas,
        "kerosine": request.fuels.kerosine,
        "co2": request.fuels.co2
    }
    wind_percentage = request.fuels.wind

    plants: List[PowerPlant] = []
    for plant_data in request.powerplants:
        if plant_data.type == "gasfired":
            plants.append(GasFiredPlant(
                plant_data.name, plant_data.type, plant_data.efficiency, plant_data.pmin, plant_data.pmax
            ))
        elif plant_data.type == "turbojet":
            plants.append(TurboJet(
                plant_data.name, plant_data.type, plant_data.efficiency, plant_data.pmin, plant_data.pmax
            ))
        elif plant_data.type == "windturbine":
            plants.append(WindTurbine(
                plant_data.name, plant_data.type, plant_data.efficiency, plant_data.pmin, plant_data.pmax
            ))

    return load, fuel_prices, wind_percentage, plants
