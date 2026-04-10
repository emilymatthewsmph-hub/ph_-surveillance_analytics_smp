### Technical Appendix
This appendix provides detailed information on the analytic logic, data transformations, and computational methods used throughout the respiratory surveillance analytics pipeline. It is intended to support transparency, reproducibility, and auditability in public health surveillance workflows.


## Pipeline Design

The analytic pipeline follows a modular design pattern common in public health analytics:

# 1. Data generation
   Synthetic ED visit data is generated using controlled randomization to simulate realistic distributions of:

Age (0–89 years)

Sex (M/F)

County (CountyA, CountyB, CountyC)

Chief complaints (respiratory and non‑respiratory)

ICD‑10 diagnosis codes relevant to respiratory surveillance

Visit dates across the 2024 calendar year

Random seeds ensure reproducibility.

# 2. Syndrome classification
Syndrome flags are assigned using simplified ICD‑10 definitions:

 | Column | Type | Description |
 |---------|-----|------------|
| Syndrome	| ICD‑10 Codes | Description|
| ILI | J10, J11 | Influenza-like illness|
| CLI | U07.1 | COVID-like illness |
| RSV-like | J21 | RSV-associated bronchiolitis |
Flags are Boolean and non-exclusive. 

# 3. Weekly aggregation
Weekly indicators are computed using:

ISO week start dates (Period('W'))

Grouping by week, county, and age group

Summation of syndrome flags

Total ED visit counts

Age groups are derived using:

0–17

18–64

65+

# 4. Incidence rate calculation
Incidence rates per 100,000 population are computed as:

rate
=
syndrome_visits
population
×
100000

Population denominators are static and sourced from population.csv.

# 5. Surveillance Signal Detection Logic
Signal detection uses:

Rolling 4‑week baselines

Percent change from baseline

Minimum baseline > 0

Threshold: ≥ 50% increase

Percent change formula:

pct_change
=
current_rate
−
baseline
baseline
Signal flag:

signal
=
{
1
if baseline > 0 and pct_change ≥ 0.50
0
otherwise

# 6. Visualization

Each analytic step reads inputs from disk and writes outputs to disk to ensure traceability and reproducibility.
Visualizations use:

Matplotlib with the “Agg” backend for non‑interactive rendering

Weekly ILI incidence rates

A single county and age group for clarity

Line plots with markers to emphasize weekly points

Outputs are saved to outputs/ili_weekly_trend.png.

Time-series plots are generated using a non-interactive backend suitable for server or batch execution environments.

## Orchestration

Execution order is enforced through a lightweight orchestration script (`run_pipeline.py`). The orchestration layer coordinates execution but contains no analytic logic.

# Reproducibility Considerations
All scripts use explicit file paths.

Random seeds ensure deterministic synthetic data.

Outputs are written to version‑controlled directories.

SQL scripts assume warehouse environments supporting analytic functions.

## SQL Parity

Key aggregation and anomaly detection logic is reproduced using SQL window functions to demonstrate analytic portability across Python and database environments.
SQL scripts reproduce all Python‑based indicators using:

Window functions (AVG() OVER)

Ordered partitions by county and age group

Lagged rolling windows (ROWS BETWEEN 4 PRECEDING AND 1 PRECEDING)

Explicit CASE statements for signal flags

This ensures analytic equivalence across platforms.


