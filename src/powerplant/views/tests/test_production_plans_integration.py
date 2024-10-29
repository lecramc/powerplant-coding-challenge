import json

from fastapi.testclient import TestClient

from main import app, ROOT_DIR

client = TestClient(app)

def test_production_plan_api() -> None:
    with open(f'{ROOT_DIR}/example_payloads/payload3.json') as f:
        payload = json.load(f)
    with open(f'{ROOT_DIR}/example_payloads/response3.json') as f:
        expected_response = json.load(f)

    response = client.post("/productionplan", json=payload)
    assert response.status_code == 200
    assert response.json() == expected_response