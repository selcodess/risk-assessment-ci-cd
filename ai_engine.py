"""Small educational text similarity classifier; not a production risk model."""
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

EXAMPLES = [
    ("customer data leak caused by weak password access", "Data security", "Review access controls and enable multifactor authentication."),
    ("unauthorized access to sensitive user information", "Data security", "Restrict permissions and audit access logs."),
    ("supplier cannot deliver materials on time", "Supply chain", "Create backup supplier options and review delivery timelines."),
    ("warehouse stock shortage delays production", "Supply chain", "Monitor inventory levels and establish safety stock."),
    ("unexpected server outage makes website unavailable", "IT availability", "Create backups, monitor uptime and document recovery procedures."),
    ("application downtime because cloud infrastructure fails", "IT availability", "Review redundancy and disaster recovery plans."),
    ("project expenses exceed the approved budget", "Financial", "Track forecasts and review spending approvals."),
    ("company faces unexpected cash flow problems", "Financial", "Review cash flow forecasts and short-term funding needs."),
    ("employee shares confidential information by mistake", "Human error", "Improve training and establish an incident reporting process."),
    ("staff enters incorrect figures into spreadsheets", "Human error", "Add validation checks and review critical entries."),
]


def analyze_description(description: str) -> dict:
    """Find the closest reference example using TF-IDF + cosine similarity."""
    if not isinstance(description, str) or not description.strip():
        raise ValueError("Please enter a risk description.")
    corpus = [example[0] for example in EXAMPLES] + [description.strip()]
    vectors = TfidfVectorizer(ngram_range=(1, 2), stop_words="english").fit_transform(corpus)
    scores = cosine_similarity(vectors[-1], vectors[:-1]).ravel()
    idx = int(scores.argmax())
    score = float(scores[idx])
    if score < 0.08:
        return {"category": "Uncertain", "similarity": round(score, 3),
                "reference": None, "recommendation": "Insufficient similarity to known examples. Request human review."}
    reference, category, recommendation = EXAMPLES[idx]
    return {"category": category, "similarity": round(score, 3),
            "reference": reference, "recommendation": recommendation}
