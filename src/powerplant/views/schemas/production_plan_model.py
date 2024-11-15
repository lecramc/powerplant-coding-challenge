from pydantic import BaseModel, Field
from typing import List, Literal


class FuelPrices(BaseModel):
    """Fuel prices"""

    gas: float = Field(..., alias="gas(euro/MWh)")
    kerosine: float = Field(..., alias="kerosine(euro/MWh)")
    co2: float = Field(..., alias="co2(euro/ton)")
    wind: float = Field(..., alias="wind(%)")


class PowerPlantPayload(BaseModel):
    """Payload for the powerplants"""

    name: str
    type: Literal["gasfired", "turbojet", "windturbine"]
    efficiency: float
    pmin: float
    pmax: float


class ProductionPlanRequest(BaseModel):
    """Request for the production plan"""

    load: float
    fuels: FuelPrices
    powerplants: List[PowerPlantPayload]


class ProductionPlanResponse(BaseModel):
    """Response for the production plan"""

    name: str
    p: float
