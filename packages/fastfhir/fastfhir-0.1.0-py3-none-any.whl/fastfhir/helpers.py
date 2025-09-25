from fastfhir.models import Patient, Observation

def create_patient(id: str, family: str, birthDate: str) -> Patient:
    """Create a Patient resource (bypassing validation)."""
    return Patient.model_construct(
        id=id,
        name=[{"family": family}],
        birthDate=birthDate
    )

def create_observation(id: str, code: str, value: float) -> Observation:
    """Create an Observation resource (bypassing validation)."""
    return Observation.model_construct(
        id=id,
        code={"coding": [{"code": code}]},
        valueQuantity={"value": value}
    )
