import pytest
from src.detector import HelmetDetector


def test_invalid_confidence():
    with pytest.raises(ValueError):
        HelmetDetector(confidence=0)


def test_invalid_confidence_above_one():
    with pytest.raises(ValueError):
        HelmetDetector(confidence=1.2)
