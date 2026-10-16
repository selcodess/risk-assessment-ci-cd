"""Run with: streamlit run app.py"""
import streamlit as st
from ai_engine import analyze_description
from risk import assess_risk

st.set_page_config(page_title="AI Risk Assessment Assistant", page_icon="🛡️")
st.title("🛡️ AI Risk Assessment Assistant")
st.caption("Educational demo | TF-IDF text similarity | Human-led decisions")
st.info("This is a learning project, not a validated decision-making or security system.")
description = st.text_area("Describe the risk (English)",
    placeholder="Example: Unauthorized access to customer information")
col1, col2 = st.columns(2)
with col1:
    probability = st.slider("Probability", 1, 5, 3)
with col2:
    impact = st.slider("Impact", 1, 5, 3)

if st.button("Analyze risk", type="primary"):
    if not description.strip():
        st.warning("Enter a description to continue.")
    else:
        scoring = assess_risk(probability, impact)
        analysis = analyze_description(description)
        st.subheader("Results")
        a, b = st.columns(2)
        a.metric("Risk score", f"{scoring['score']}/25")
        b.metric("Rule-based level", scoring["level"])
        st.write("**Suggested category:**", analysis["category"])
        st.write("**Text similarity to closest example:**", f"{analysis['similarity']:.1%}")
        st.caption("Similarity is not a confidence probability or risk likelihood.")
        if analysis["reference"]:
            st.write("**Closest example:**", analysis["reference"])
        st.write("**General suggestion:**", analysis["recommendation"])
        st.warning("Human review required before any real-world decision.")
