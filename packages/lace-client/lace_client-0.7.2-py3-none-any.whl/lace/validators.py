"""
Schema validators for Lace.
"""

import json
from typing import Dict, List, Tuple, Any, Optional
import jsonschema
from jsonschema import Draft7Validator

try:
    import importlib.resources as ir
except ImportError:
    # Python 3.8 compatibility
    import importlib_resources as ir


# Load schema once at module level
ANALYSIS_SCHEMA = json.loads(
    ir.files('lace.schemas').joinpath('analysis.v1.1.json').read_text(encoding='utf-8')
)


def validate_analysis(data: dict) -> Tuple[bool, List[str]]:
    """
    Validate analysis data against the schema.
    
    Returns:
        (valid, errors) - valid is True if validation passed, errors is list of error messages
    """
    try:
        # Guardrail: Require schema_version field
        if 'schema_version' not in data:
            return False, ["Missing required field: schema_version"]
        if data['schema_version'] != 'analysis.v1.1':
            return False, [f"Schema version mismatch: expected 'analysis.v1.1', got '{data['schema_version']}'"]
        
        validator = Draft7Validator(ANALYSIS_SCHEMA)
        
        errors = []
        for error in validator.iter_errors(data):
            # Create human-friendly error message
            path = ".".join(str(p) for p in error.path) if error.path else "root"
            if error.validator == "required":
                # Extract missing field from error message
                missing = error.message.split("'")[1] if "'" in error.message else error.message
                errors.append(f"Missing required field: {path}.{missing}")
            elif error.validator == "enum":
                errors.append(f"Invalid value at {path}: expected one of {error.validator_value}, got {error.instance}")
            elif error.validator == "type":
                errors.append(f"Wrong type at {path}: expected {error.validator_value}, got {type(error.instance).__name__}")
            elif error.validator == "minimum":
                errors.append(f"Value at {path} too small: minimum {error.validator_value}, got {error.instance}")
            elif error.validator == "maximum":
                errors.append(f"Value at {path} too large: maximum {error.validator_value}, got {error.instance}")
            else:
                errors.append(f"Validation error at {path}: {error.message}")
        
        return len(errors) == 0, errors
        
    except Exception as e:
        return False, [f"Schema validation error: {str(e)}"]


def validate_answer_type(answer: Any, question_type: str) -> bool:
    """
    Validate that an answer matches the expected question type.
    
    Args:
        answer: The answer value
        question_type: Expected type (bool, enum, string, number)
    
    Returns:
        True if valid, False otherwise
    """
    if question_type == "bool":
        return isinstance(answer, bool)
    elif question_type == "enum":
        return isinstance(answer, str)  # Enum values are strings
    elif question_type == "string":
        return isinstance(answer, str)
    elif question_type == "number":
        return isinstance(answer, (int, float))
    else:
        # Unknown type, be permissive
        return True


def coerce_answer(value: str, question_type: str, enum_choices: List[str] = None) -> Tuple[Any, bool]:
    """
    Coerce a string value to the expected question type with deterministic rules.
    
    Args:
        value: String value to coerce
        question_type: Expected type (bool, enum, string, number)
        enum_choices: Valid choices for enum type
    
    Returns:
        (coerced_value, success) - success is False if coercion failed
    """
    if question_type == "bool":
        # Deterministic bool coercion: true/false/1/0/yes/no/on/off (case-insensitive)
        lower_val = value.lower().strip()
        if lower_val in ('true', '1', 'yes', 'on'):
            return True, True
        elif lower_val in ('false', '0', 'no', 'off'):
            return False, True
        else:
            return None, False
    
    elif question_type == "number":
        # Parse as int if exact, else float
        try:
            # First try int
            if '.' not in value and 'e' not in value.lower():
                return int(value), True
            else:
                return float(value), True
        except ValueError:
            return None, False
    
    elif question_type == "enum":
        # Case-sensitive exact match
        if enum_choices and value not in enum_choices:
            return None, False
        return value, True
    
    elif question_type == "string":
        # Use verbatim
        return value, True
    
    else:
        # Unknown type, pass through
        return value, True


def parse_answer_arg(answer_str: str) -> Tuple[str, str]:
    """
    Parse --answer argument in format id=value.
    
    Returns:
        (id, value) tuple
    
    Raises:
        ValueError if format is invalid
    """
    if '=' not in answer_str:
        raise ValueError(f"Invalid answer format: '{answer_str}'. Expected: id=value")
    
    parts = answer_str.split('=', 1)  # Split only on first =
    answer_id = parts[0].strip()
    answer_value = parts[1]  # Don't strip value, preserve whitespace
    
    if not answer_id:
        raise ValueError(f"Invalid answer format: '{answer_str}'. ID cannot be empty")
    
    return answer_id, answer_value


def generate_answer_stub(questions: List[Dict], provided_answers: Dict) -> Dict:
    """
    Generate a JSON stub for unanswered required questions.
    
    Args:
        questions: List of question dictionaries
        provided_answers: Already provided answers
    
    Returns:
        JSON-serializable dict with FILL_ME placeholders
    """
    stub = {}
    
    for q in questions:
        qid = q.get('id')
        qtype = q.get('type')
        required = q.get('required', False)
        enum_choices = q.get('enum', [])
        
        # Skip if already answered or not required
        if qid in provided_answers or not required:
            continue
        
        # Generate appropriate placeholder
        if qtype == 'bool':
            stub[qid] = True  # Default to true as example
        elif qtype == 'enum' and enum_choices:
            # Show the allowed choices
            stub[qid] = f"one-of: {'|'.join(enum_choices)}"
        elif qtype == 'number':
            stub[qid] = "FILL_ME"
        else:
            stub[qid] = "FILL_ME"
    
    return stub