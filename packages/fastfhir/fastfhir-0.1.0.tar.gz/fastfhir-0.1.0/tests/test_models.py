import pytest
from fastfhir.models import Patient, Observation, Encounter

def test_patient_instantiation():
    patient = Patient.model_construct(
        id="123",
        name=[{"family": "Smith"}],
        birthDate="1990-01-01"
    )
    assert patient.id == "123"
    assert patient.name[0]["family"] == "Smith"

def test_observation_instantiation():
    obs = Observation.model_construct(
        id="obs1",
        code={"coding": [{"code": "heart-rate"}]},
        valueQuantity={"value": 72}
    )
    assert obs.id == "obs1"
    assert obs.valueQuantity["value"] == 72

def test_encounter_instantiation():
    encounter = Encounter.model_construct(
        id="enc1",
        status="in-progress"
    )
    assert encounter.id == "enc1"
    assert encounter.status == "in-progress"
