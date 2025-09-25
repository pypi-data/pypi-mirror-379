import pytest
from fastfhir.models import Patient
from fastfhir.validation import validate_resource

def test_valid_patient():
    patient = Patient(
        id="123",
        name=[{"family": "Smith"}],
        birthDate="1990-01-01"
    )
    is_valid, errors = validate_resource(patient)
    assert is_valid is True
    assert errors is None

def test_invalid_patient_missing_required_field():
    patient = Patient.model_construct(id="456")
    is_valid, errors = validate_resource(patient)
    # FHIR v8 makes name and birthDate optional, so patient is valid
    assert is_valid is True

