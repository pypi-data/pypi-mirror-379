from pydantic import ValidationError

def validate_resource(resource):
    """
    Validate a FHIR resource using Pydantic v2.
    Returns (True, None) if valid, or (False, error_str) if invalid.
    """
    try:
        resource.__class__.model_validate(resource.model_dump())
        return True, None
    except ValidationError as e:
        return False, str(e)
