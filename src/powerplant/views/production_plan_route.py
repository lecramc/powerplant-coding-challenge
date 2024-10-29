from typing import List

from fastapi import APIRouter, HTTPException

from src.powerplant.usecases.get_production_plan_usecase import ProductionPlan, Plan
from src.powerplant.views.schemas.production_plan_model import (
    ProductionPlanRequest,
    ProductionPlanResponse,
)
from src.powerplant.views.utils.convert_request_to_entities import (
    convert_request_to_entities,
)

router = APIRouter(prefix="/productionplan", tags=["productionplan"])


@router.post("/", response_model=List[ProductionPlanResponse])
async def production_plan(
    request: ProductionPlanRequest,
) -> List[ProductionPlanResponse]:
    try:
        load, fuel_prices, wind_percentage, plants = convert_request_to_entities(
            request
        )

        use_case = ProductionPlan(plants)
        production_plan: List[Plan] = use_case.execute(
            load, fuel_prices, wind_percentage
        )
        return [ProductionPlanResponse(**p) for p in production_plan]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {e}")
