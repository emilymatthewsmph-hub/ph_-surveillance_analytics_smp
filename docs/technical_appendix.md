# Technical Appendix

## Pipeline Design

The analytic pipeline follows a modular design pattern common in public health analytics:

1. Data generation
2. Syndrome classification
3. Weekly aggregation
4. Incidence rate calculation
5. Anomaly detection
6. Visualization

Each analytic step reads inputs from disk and writes outputs to disk to ensure traceability and reproducibility.

## Orchestration

Execution order is enforced through a lightweight orchestration script (`run_pipeline.py`). The orchestration layer coordinates execution but contains no analytic logic.

## SQL Parity

Key aggregation and anomaly detection logic is reproduced using SQL window functions to demonstrate analytic portability across Python and database environments.

## Visualization

Time-series plots are generated using a non-interactive backend suitable for server or batch execution environments.
