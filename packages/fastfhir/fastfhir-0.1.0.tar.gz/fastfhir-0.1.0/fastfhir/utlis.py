def resource_to_json(resource):
    return resource.json()

def json_to_resource(json_dict, resource_cls):
    return resource_cls.parse_obj(json_dict)
