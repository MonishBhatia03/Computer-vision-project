import csv
import os
from datetime import datetime


def log_detection(path, source, detections):
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    exists = os.path.exists(path)

    with open(path, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        if not exists:
            writer.writerow(["timestamp", "source", "label", "confidence"])

        for d in detections:
            writer.writerow([
                datetime.now().isoformat(timespec="seconds"),
                source,
                d.label,
                round(d.confidence, 4)
            ])
