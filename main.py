import os
from typing import Dict

from fastapi import FastAPI

from src.powerplant.views import production_plan_route

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
app = FastAPI()

app.include_router(production_plan_route.router)


@app.get("/")
async def root() -> Dict[str, str]:
    return {"message": "Hello World"}
