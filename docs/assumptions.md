# Assumptions

This project is based on the following analytic and data assumptions:

## Data Assumptions
- All emergency department visit data is fully synthetic and generated for demonstration purposes only.
- Patient identifiers, visit identifiers, and dates are randomly generated and contain no real-world meaning.
- Diagnosis codes are simplified ICD-10-like codes used only for illustrative syndrome classification.
- Population denominators are fixed and assumed constant across the surveillance period.

## Surveillance Assumptions
- Weekly aggregation is an appropriate reporting interval for respiratory surveillance indicators.
- Syndrome definitions (ILI, COVID-like illness, RSV-like illness) are simplified and rule-based.
- A visit may be classified into only one primary syndrome category.

## Anomaly Detection Assumptions
- Short-term rolling baselines are sufficient for identifying meaningful increases in activity.
- Anomaly thresholds are conservative to prioritize interpretability over sensitivity.
- Flagged anomalies indicate signals for review, not confirmed outbreaks.

These assumptions are intentionally simplified to prioritize clarity and reproducibility in a portfolio context.
``
