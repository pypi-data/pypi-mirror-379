from fastapi import APIRouter, HTTPException
from fastfhir.models import Patient, Observation
from fastfhir.validation import validate_resource
from typing import List

router = APIRouter()

# In-memory stores
patients = {}
observations = {}

# ------------------ Patient Endpoints ------------------

@router.post("/Patient")
async def create_patient(patient: Patient):
    """
    Create a new Patient. Auto-fill defaults and validate.
    """
    # Auto-fill some defaults if missing
    if getattr(patient, "active", None) is None:
        patient.active = True

    is_valid, errors = validate_resource(patient)
    if not is_valid:
        raise HTTPException(status_code=400, detail=errors)

    patients[patient.id] = patient
    return patient.model_dump()  # Pydantic v2

@router.get("/Patient/{patient_id}")
async def get_patient(patient_id: str):
    patient = patients.get(patient_id)
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient.model_dump()

@router.get("/Patient")
async def search_patient(_id: str = None):
    """
    Search Patients by _id.
    """
    results = list(patients.values())
    if _id:
        results = [p for p in results if p.id == _id]
    return [p.model_dump() for p in results]    

# ------------------ Observation Endpoints ------------------

@router.post("/Observation")
async def create_observation(obs: Observation):
    """
    Create a new Observation. Auto-fill required fields and validate.
    """
    if not getattr(obs, "status", None):
        obs.status = "final"  # default

    is_valid, errors = validate_resource(obs)
    if not is_valid:
        raise HTTPException(status_code=400, detail=errors)

    observations[obs.id] = obs
    return obs.model_dump()

@router.get("/Observation/{obs_id}")
async def get_observation(obs_id: str):
    obs = observations.get(obs_id)
    if not obs:
        raise HTTPException(status_code=404, detail="Observation not found")
    return obs.model_dump()

@router.get("/Observation")
async def search_observation(subject: str = None):
    """
    Search Observations by subject reference.
    """
    results = list(observations.values())
    if subject:
        results = [o for o in results if o.subject.reference == subject]
    return [o.model_dump() for o in results]
