# Limitations

This project is designed as a demonstration of respiratory syndromic surveillance analytics and intentionally simplifies several aspects of real‑world surveillance systems. The following limitations should be considered when interpreting results.

Data Limitations
All ED visit data is synthetic and does not reflect real patient encounters.

Diagnosis codes are randomly assigned and do not follow clinical patterns.

Chief complaints are not used in syndrome classification, though they are important in operational systems.

No hospital‑level variation or facility reporting patterns are modeled.

Methodological Limitations
Syndrome definitions rely solely on ICD‑10 codes.

No natural seasonality (e.g., influenza peaks) is present in the synthetic data.

Rolling baselines do not incorporate smoothing, trend adjustment, or seasonality correction.

Percent change thresholds are simplified and not calibrated to real surveillance systems.

Statistical Limitations
No confidence intervals or uncertainty estimates are included.

No spatial smoothing or Bayesian modeling is applied.

No adjustment for multiple comparisons across counties or age groups.

Operational Limitations
The pipeline does not include automated data ingestion or ETL processes.

No alerting or notification system is implemented.

SQL scripts assume a warehouse environment but do not include optimization strategies.

Visualization is limited to a single syndrome, county, and age group.

Scope Limitations
The project is not intended for real‑world public health decision‑making.

Outputs should not be interpreted as epidemiologic findings.

The system is not validated against real surveillance data.
