import jsonschema
from jsonschema import validate
import json

def get_schema():
    """This function loads the given schema available"""
    with open('FlaskApp/package/util_files/input_schema.json', 'r') as file:
        schema = json.load(file)
    return schema

def validate_json(json_data):
    # Describe what kind of json you expect.
    execute_api_schema = get_schema()
    try:
        validate(instance=json_data, schema=execute_api_schema)
    except jsonschema.exceptions.ValidationError:
        return False
    return True

'''
# Describe what kind of json you expect.
schema = {
    "type" : "object",
    "properties" : {
        "id" : {"type" : "number"},
        "company_name" : {"type" : "string"},
        "company_website" : {"type" : "string"},
    },
}

def validate_json(json_data):
    # Describe what kind of json you expect.
    
    try:
        validate(instance=json_data, schema=schema)
    except jsonschema.exceptions.ValidationError:
        return False
    return True
'''

