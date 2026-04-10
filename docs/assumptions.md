## Assumptions
This project is built on a set of analytic, operational, and methodological assumptions that support a simplified but realistic demonstration of respiratory syndromic surveillance workflows. These assumptions ensure reproducibility and interpretability while keeping the project focused on core surveillance concepts.

# Data Assumptions
All ED visit records in ed_visits.csv represent unique encounters.

Synthetic data generation produces plausible but non‑realistic distributions of age, sex, county, diagnosis codes, and chief complaints.

ICD‑10 codes used for syndrome classification (J10, J11, U07.1, J21) are sufficient for simplified ILI/CLI/RSV‑like definitions.

Population denominators in population.csv are static for the surveillance period.

Counties and age groups in the ED data align exactly with those in the population file.

# Temporal Assumptions
The surveillance period spans January–December 2024.

Weekly aggregation uses ISO week start dates.

No adjustments are made for partial weeks or holiday‑related fluctuations.

Rolling baselines use the previous four complete weeks only.

Syndrome Classification Assumptions
ICD‑10 codes alone are used for syndrome assignment.

Chief complaints are not incorporated into syndrome logic in this simplified model.

Each visit may be flagged for multiple syndromes if codes overlap (though synthetic data minimizes this).

# Surveillance Signal Assumptions
A 50% increase from baseline is considered meaningful for signal detection.

Baseline must be > 0 to avoid division errors and spurious signals.

No smoothing, seasonality adjustment, or spatial modeling is applied.

Signals represent analytic flags, not epidemiologic conclusions.

# SQL Parity Assumptions
SQL scripts assume a warehouse environment supporting analytic window functions.

Table names and schemas match the CSV outputs produced by the Python pipeline.

No indexing, partitioning, or optimization strategies are included, as the focus is analytic parity.

# Visualization Assumptions
Visualizations focus on a single county and age group to maintain clarity.

ILI is used as the example syndrome due to its interpretability and seasonal relevance.

Matplotlib’s non‑interactive backend (“Agg”) is used for reproducibility across environments.

# Scope Assumptions
This project is a demonstration of analytic capability, not a production surveillance system.

No PHI or real patient data is used.

The pipeline is intentionally simplified to highlight core concepts rather than operational complexity.
