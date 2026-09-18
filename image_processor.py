import os
import cv2
from .statistics import calculate_statistics


def process_image(detector, input_path, output_path):
    if not os.path.isfile(input_path):
        raise FileNotFoundError(f"Input image not found: {input_path}")

    frame = cv2.imread(input_path)
    if frame is None:
        raise ValueError("The input file could not be read as an image.")

    detections = detector.detect(frame)

    for d in detections:
        cv2.rectangle(frame, (d.x1, d.y1), (d.x2, d.y2), (0, 255, 0), 2)
        text = f"{d.label}: {d.confidence:.2f}"
        cv2.putText(frame, text, (d.x1, max(20, d.y1 - 8)),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 255, 0), 2)

    stats = calculate_statistics(detections)
    cv2.putText(
        frame,
        f"Detections: {stats['total']}",
        (15, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255, 255, 255),
        2
    )

    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    if not cv2.imwrite(output_path, frame):
        raise IOError("Could not save output image.")

    return stats
