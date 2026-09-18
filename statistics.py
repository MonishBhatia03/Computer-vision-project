from collections import Counter


def calculate_statistics(detections):
    labels = [d.label.lower() for d in detections]
    counts = Counter(labels)
    total = len(labels)

    helmet = sum(v for k, v in counts.items() if "helmet" in k and "no" not in k)
    no_helmet = sum(
        v for k, v in counts.items()
        if "no_helmet" in k or "without" in k or "no-helmet" in k
    )

    violation_percentage = (no_helmet / total * 100) if total else 0.0

    return {
        "total": total,
        "helmet": helmet,
        "no_helmet": no_helmet,
        "violation_percentage": round(violation_percentage, 2),
        "class_counts": dict(counts),
    }
