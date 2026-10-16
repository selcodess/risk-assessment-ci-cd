"""Educational supervised risk text classifier (not for real decisions)."""
from functools import lru_cache
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline

TRAINING_EXAMPLES = [
    ("customer password was stolen", "Data security"),
    ("unauthorized access to customer records", "Data security"),
    ("private customer information was leaked", "Data security"),
    ("cyberattack exposed sensitive data", "Data security"),
    ("database credentials were compromised", "Data security"),
    ("supplier delivery is delayed", "Supply chain"),
    ("supplier cannot deliver the ordered materials", "Supply chain"),
    ("warehouse stock shortage delays production", "Supply chain"),
    ("shipment of components arrived late", "Supply chain"),
    ("inventory shortage interrupts manufacturing", "Supply chain"),
    ("company expenses exceed the budget", "Financial"),
    ("business faces unexpected cash flow problems", "Financial"),
    ("the firm is losing money", "Financial"),
    ("unexpected financial losses reduce profit", "Financial"),
    ("operating costs increased beyond forecasts", "Financial"),
]

@lru_cache(maxsize=1)
def train_model():
    texts, labels = zip(*TRAINING_EXAMPLES)
    model = make_pipeline(
        TfidfVectorizer(ngram_range=(1, 2), stop_words="english"),
        LogisticRegression(max_iter=1000),
    )
    model.fit(texts, labels)
    return model


def predict_category(description: str) -> str:
    """Predict one of 3 illustrative categories, not a calibrated probability."""
    if not isinstance(description, str) or not description.strip():
        raise ValueError("Please provide a non-empty risk description.")
    return str(train_model().predict([description.strip()])[0])
