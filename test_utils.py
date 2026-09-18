import pytest
from src.utils import validate_confidence


def test_valid_confidence():
    assert validate_confidence(0.5) == 0.5


def test_invalid_confidence():
    with pytest.raises(ValueError):
        validate_confidence(1.5)
