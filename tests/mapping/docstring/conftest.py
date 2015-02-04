import pytest


@pytest.fixture
def operation_dict():
    return {
        "tags": [
            "pet"
        ],
        "summary": "Finds Pets by status",
        "description": "Multiple status values can be provided with comma seperated strings",  # noqa
        "operationId": "findPetsByStatus",
        "produces": [
            "application/json",
            "application/xml"
        ],
        "parameters": [
            {
                "name": "status",
                "in": "query",
                "description": "the status, yo!",
                "required": False,
                "type": "array",
                "items": {
                    "type": "string"
                },
                "collectionFormat": "multi",
                "default": "available"
            }
        ],
        "responses": {
            "200": {
                "description": "successful operation",
                "schema": {
                    "type": "array",
                    "items": {
                        "$ref": "#/definitions/Pet"
                    }
                }
            },
            "400": {
                "description": "Invalid status value"
            }
        },
    }


@pytest.fixture
def parameter_dict(operation_dict):
    return operation_dict['parameters'][0]