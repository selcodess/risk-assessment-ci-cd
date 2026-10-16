"""Simple rule-based risk assessment demonstration (not an AI model)."""


def assess_risk(probability: int, impact: int) -> dict:
    if not all(isinstance(v, int) and not isinstance(v, bool) for v in (probability, impact)):
        raise TypeError("Probability and impact must be integers")
    if not (1 <= probability <= 5 and 1 <= impact <= 5):
        raise ValueError("Probability and impact must be between 1 and 5")

    score = probability * impact
    level = "HIGH" if score >= 15 else "MEDIUM" if score >= 8 else "LOW"
    return {"score": score, "level": level, "human_review_required": level == "HIGH"}


if __name__ == "__main__":
    print(assess_risk(4, 5))
