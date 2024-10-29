from pydantic import BaseModel, Field
from typing import List, Literal


class FuelPrices(BaseModel):
    gas: float = Field(..., alias="gas(euro/MWh)")
    kerosine: float = Field(..., alias="kerosine(euro/MWh)")
    co2: float = Field(..., alias="co2(euro/ton)")
    wind: float = Field(..., alias="wind(%)")


class PowerPlantPayload(BaseModel):
    name: str
    type: Literal["gasfired", "turbojet", "windturbine"]
    efficiency: float
    pmin: float
    pmax: float


class ProductionPlanRequest(BaseModel):
    load: float
    fuels: FuelPrices
    powerplants: List[PowerPlantPayload]


class ProductionPlanResponse(BaseModel):
    name: str
    p: float
