# Risk Assessment Demo: Python CI and Delivery

A beginner-friendly, **rule-based** risk scoring example created as a practical DevOps learning exercise. This is **not** a machine-learning or generative AI system.

## What it does

- Validates risk probability and impact on a 1-5 scale
- Calculates a risk score and LOW/MEDIUM/HIGH classification
- Flags HIGH risks for human review
- Runs automated tests with `pytest` on every push and pull request to `main`
- After a successful push to `main`, creates a downloadable **delivery artifact** (ZIP) using GitHub Actions

## Run locally

```bash
python -m pip install -r requirements-dev.txt
python risk.py
python -m pytest -q
```

## CI/CD explanation

- **Continuous Integration (CI):** GitHub Actions installs Python and runs automated tests on Python 3.11 and 3.12.
- **Continuous Delivery (CD):** After all tests pass on `main`, GitHub Actions packages the source and saves a versioned-by-run downloadable artifact. This is *artifact delivery*, not automatic deployment to a production service.

Workflow: `.github/workflows/ci-cd.yml`

## Future improvements

- Add CSV import and export
- Add a simple web interface
- Add optional explainable AI suggestions, with human approval
- Deploy to a hosting service after choosing a safe deployment target
