import os


def ensure_file_exists(path):
    if not os.path.isfile(path):
        raise FileNotFoundError(f"File does not exist: {path}")


def validate_confidence(value):
    value = float(value)
    if not 0 < value <= 1:
        raise ValueError("Confidence must be in the range (0, 1].")
    return value
