from src.constanst import PLAIN_TASK_TYPES
from cerberus import Validator
steps_schema = {
    'start': {'type': 'dict', 'required': True, 'schema': {
        'days': {'type': 'integer', 'required': False},
        'seconds': {'type': 'integer', 'required': False},
        'microseconds': {'type': 'integer', 'required': False},
        'milliseconds': {'type': 'integer', 'required': False},
        'minutes': {'type': 'integer', 'required': False},
        'hours': {'type': 'integer', 'required': False},
        'weeks': {'type': 'integer', 'required': False}}},
    'type': {'type': 'string', 'required': True, 'allowed': PLAIN_TASK_TYPES},
    'payload': {'type': 'dict', 'required': False},
}
task_schema = {
    'document_format': {'type': 'integer', 'required': True},
    'steps': {'type': 'list', 'schema': {'type': 'dict', 'schema': steps_schema}}
}
task_validator = Validator(task_schema)
