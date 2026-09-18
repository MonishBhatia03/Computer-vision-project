from dataclasses import dataclass
from typing import List
from ultralytics import YOLO


@dataclass
class Detection:
    label: str
    confidence: float
    x1: int
    y1: int
    x2: int
    y2: int


class HelmetDetector:
    def __init__(self, model_path="yolo11n.pt", confidence=0.40):
        if not 0 < confidence <= 1:
            raise ValueError("Confidence must be between 0 and 1.")
        self.model = YOLO(model_path)
        self.confidence = confidence

    def detect(self, frame) -> List[Detection]:
        results = self.model.predict(
            source=frame,
            conf=self.confidence,
            verbose=False
        )

        detections = []
        for result in results:
            names = result.names
            if result.boxes is None:
                continue

            for box in result.boxes:
                cls_id = int(box.cls[0])
                conf = float(box.conf[0])
                x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())
                detections.append(
                    Detection(
                        label=str(names[cls_id]),
                        confidence=conf,
                        x1=x1, y1=y1, x2=x2, y2=y2
                    )
                )
        return detections
