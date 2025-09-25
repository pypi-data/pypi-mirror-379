from fastfhir.helpers import create_patient, create_observation

def test_create_patient():
    patient = create_patient("123", "Smith", "1990-01-01")
    assert patient.id == "123"
    assert patient.name[0]["family"] == "Smith"

def test_create_observation():
    obs = create_observation("obs1", "heart-rate", 72)
    assert obs.id == "obs1"
    assert obs.valueQuantity["value"] == 72
