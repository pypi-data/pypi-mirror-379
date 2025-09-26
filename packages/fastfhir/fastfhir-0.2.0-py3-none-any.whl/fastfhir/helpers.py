from fastfhir.models import Patient, Observation

def create_patient(id: str, family: str, birthDate: str) -> Patient:
    """Create a Patient resource (bypassing validation)."""
    return Patient.model_construct(
        id=id,
        name=[{"family": family}],
        birthDate=birthDate
    )

def create_observation(
    id: str,
    subject_id: str,
    code: str,
    display: str,
    value: float,
    unit: str
) -> Observation:
    """Create a full Observation resource."""
    return Observation.model_construct(
        id=id,
        subject={"reference": f"Patient/{subject_id}"},
        code={"coding": [{"code": code, "display": display}]},
        valueQuantity={"value": value, "unit": unit}
    )
