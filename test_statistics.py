from src.detector import Detection
from src.statistics import calculate_statistics


def test_statistics():
    detections = [
        Detection("helmet", 0.91, 0, 0, 10, 10),
        Detection("no_helmet", 0.88, 0, 0, 10, 10),
        Detection("helmet", 0.95, 0, 0, 10, 10),
    ]
    result = calculate_statistics(detections)

    assert result["total"] == 3
    assert result["helmet"] == 2
    assert result["no_helmet"] == 1
    assert result["violation_percentage"] == 33.33
