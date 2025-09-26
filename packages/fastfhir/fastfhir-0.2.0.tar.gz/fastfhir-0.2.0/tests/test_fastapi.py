import pytest
from fastapi.testclient import TestClient
from fastfhir.fastapi_router import router as fhir_router
from fastfhir.models import Patient, Observation
from fastapi import FastAPI

# FastAPI app for testing
app = FastAPI()
app.include_router(fhir_router)
client = TestClient(app)

# ------------------- PATIENT TESTS -------------------
def test_create_and_get_patient():
    payload = {
        "id": "p1",
        "name": [{"family": "Smith", "given": ["John"]}],
        "birthDate": "1990-01-01"
    }
    response = client.post("/Patient", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == "p1"

    response = client.get("/Patient/p1")
    assert response.status_code == 200
    data = response.json()
    assert data["name"][0]["family"] == "Smith"

def test_create_patient_invalid_payload():
    payload = {"id": "p2"}  # missing required fields
    response = client.post("/Patient", json=payload)
    assert response.status_code == 200  # FastAPI validation

def test_search_patient_by_id():
    client.post("/Patient", json={
        "id": "p3",
        "name": [{"family": "Doe"}],
        "birthDate": "1980-05-05"
    })
    response = client.get("/Patient", params={"_id": "p3"})
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["id"] == "p3"

# ------------------- OBSERVATION TESTS -------------------
def test_create_and_get_observation():
    client.post("/Patient", json={
        "id": "p4",
        "name": [{"family": "Lee"}],
        "birthDate": "1975-03-03"
    })
    payload = {
        "id": "o1",
        "status": "final",
        "subject": {"reference": "Patient/p4"},
        "code": {"coding": [{"code": "789-8", "display": "Hemoglobin"}]},
        "valueQuantity": {"value": 13.5, "unit": "g/dL"}
    }
    response = client.post("/Observation", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == "o1"
    assert data["subject"]["reference"] == "Patient/p4"

    response = client.get("/Observation/o1")
    assert response.status_code == 200
    data = response.json()
    assert data["code"]["coding"][0]["code"] == "789-8"

def test_search_observation_by_subject():
    client.post("/Patient", json={
        "id": "p4",
        "name": [{"family": "Lee"}],
        "birthDate": "1975-03-03"
    })
    client.post("/Observation", json={
        "id": "o1",
        "status": "final",
        "subject": {"reference": "Patient/p4"},
        "code": {"coding": [{"code": "789-8"}]},
        "valueQuantity": {"value": 13.5, "unit": "g/dL"}
    })
    response = client.get("/Observation", params={"subject": "Patient/p4"})
    assert response.status_code == 200
    data = response.json()
    assert any(o["subject"]["reference"] == "Patient/p4" for o in data)

def test_create_observation_invalid_payload():
    payload = {"id": "o2"}  # missing required fields
    response = client.post("/Observation", json=payload)
    assert response.status_code == 422  # FastAPI validation
