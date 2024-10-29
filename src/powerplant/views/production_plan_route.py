from http.client import HTTPException
from typing import Dict, Union, List

from fastapi import  APIRouter

from src.powerplant.usecases.get_production_plans_usecase import ProductionPlan

router = APIRouter(prefix="/productionplan", tags=["productionplan"])
@router.post("/")
async def production_plan(request: ProductionPlanRequest) -> List[Dict[str, Union[str, float]]]:
    try:
        load, fuel_prices, wind_percentage, plants = convert_request_to_entities(request)

        use_case = ProductionPlan(plants)
        result = use_case.execute(load, fuel_prices, wind_percentage)

        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {e}")
