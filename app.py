
import streamlit as st
from ai_engine import analyze_description
from ml_model import predict_category
from risk import assess_risk

st.set_page_config(
    page_title="AI Risk Assessment Assistant",
    page_icon="🛡️"
)

st.title("🛡️ AI Risk Assessment Assistant")
st.caption("NLP + Machine Learning | Educational Project")

st.info(
    "Educational prototype. Results require human review."
)

description = st.text_area(
    "Describe the risk (English)",
    placeholder="Example: Supplier delivery is delayed"
)

col1, col2 = st.columns(2)

with col1:
    probability = st.slider("Probability", 1, 5, 3)

with col2:
    impact = st.slider("Impact", 1, 5, 3)

if st.button("Analyze risk", type="primary"):
    if not description.strip():
        st.warning("Please enter a risk description.")
    else:
        risk = assess_risk(probability, impact)
        nlp = analyze_description(description)
        ml = predict_category(description)

        st.subheader("Results")

        a, b = st.columns(2)
        a.metric("Risk Score", f"{risk['score']}/25")
        b.metric("Risk Level", risk["level"])

        st.subheader("Machine Learning Prediction")
        st.success(f"Predicted category: {ml}")

        st.subheader("NLP Similarity Analysis")
        st.write("Closest category:", nlp["category"])
        st.write("Similarity:", f"{nlp['similarity']:.1%}")
        st.write("Recommendation:", nlp["recommendation"])

        st.caption(
            "Similarity is not prediction confidence. "
            "The ML model uses a small training dataset "
            "and is not validated for real decisions."
        )

        st.warning("Human review required.")
