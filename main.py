import os
from typing import Dict

from fastapi import FastAPI

from src.powerplant.views import production_plan_route

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

tags_metadata = [
    {
        "name": "productionplan",
        "description": "Get the production plan for a given load",
    }
]
app = FastAPI(title="Production Plan API", openapi_tags=tags_metadata)

app.include_router(production_plan_route.router)


@app.get("/")
async def root() -> Dict[str, str]:
    return {"message": "Hello World"}
