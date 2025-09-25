from enum import Enum


class OpenAPIType(Enum):
    OFFICIAL = 'official'
    ENDPOINT = 'endpoint'
    ENDPOINT_PARAMETERS = 'endpoint-parameters'
    ENDPOINT_PARAMETERS_CONSTRAINTS = 'endpoint-parameters-constraints'
    ENDPOINT_PARAMETERS_CONSTRAINTS_FEEDBACK = 'endpoint-parameters-constraints-feedback'
