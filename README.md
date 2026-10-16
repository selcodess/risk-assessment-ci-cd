# 🛡️ AI Risk Assessment Assistant

An interactive educational risk assessment application built with Python, Streamlit, and scikit-learn.

**Live Demo:** https://selcodess-risk-assistant.streamlit.app/

**GitHub Repository:** https://github.com/selcodess/risk-assessment-ci-cd

## Project Overview

This project combines rule-based risk scoring with natural language processing techniques to help users explore and categorize potential business and IT risks.

## Key Features

- Risk scoring based on probability and impact.
- Text similarity classification using TF-IDF and cosine similarity.
- Risk categories and predefined recommendations.
- Interactive web interface developed with Streamlit.
- Automated testing using pytest.
- CI and automated artifact packaging using GitHub Actions.
- Human review safeguards for high-risk assessments.

## Technologies

Python, Streamlit, scikit-learn, pytest, Git, GitHub Actions, CI/CD.

## Run Locally

Install the application dependencies:

`pip install -r requirements.txt`

Launch the application:

`streamlit run app.py`

## Limitations

This is an educational prototype, not a validated production AI system. Similarity scores do not represent prediction confidence, and recommendations require human review.
