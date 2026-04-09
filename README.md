Respiratory Syndromic Surveillance Analytics (Synthetic Data)

## Project Overview
This project demonstrates a federal‑style respiratory syndromic surveillance pipeline using fully synthetic emergency department (ED) visit data. The workflow mirrors analytic patterns used by CDC, state health departments, and HHS‑supported surveillance systems to monitor respiratory illness trends, calculate standardized indicators, and flag anomalous increases for situational awareness.
The project emphasizes:

Clear analytic lineage
Reproducible execution
Modular, auditable design
Portability across Python and SQL environments

All data are synthetic and contain no PHI.

# Surveillance Capabilities
The pipeline implements the following core public‑health surveillance functions:


# Syndrome Classification
Rule‑based mapping of ED visits into:

Influenza‑Like Illness (ILI)
COVID‑Like Illness (CLI)
RSV‑Like Illness



# Weekly Aggregation & Incidence Rates
Aggregation of visit‑level data into weekly counts and incidence rates per 100,000 population by county and age group.


# Anomaly Detection (Signal Flagging)
Rule‑based comparison of weekly rates against rolling historical baselines to flag unusual increases warranting epidemiologic review.


# Epidemiologic Visualization
Generation of time‑series plots to support interpretation of surveillance trends and situational awareness.



Pipeline Orchestration
The analytic workflow is implemented using modular Python components coordinated by a lightweight orchestration layer (run_pipeline.py). The orchestration layer defines the official execution order of the pipeline but does not contain analytic logic itself.
This design reflects how surveillance workflows are operationalized in federal and state environments, where:

Analytic logic is modular and reusable
Execution order is explicit and reviewable
Outputs are written to disk at each stage to support auditability and re‑runs
Pipelines are suitable for scheduled or batch execution


# SQL Parity
Key analytic transformations — including weekly aggregation, baseline calculation, and anomaly detection — are reproduced using analytic SQL window functions. The SQL examples demonstrate how the same surveillance logic can be implemented in enterprise data warehouse environments commonly used in federal settings.

Project Structure
Plain Textph_surveillance_analytics_smp/├── data/│   ├── ed_visits.csv│   ├── lab_results.csv│   └── population.csv│├── outputs/│   ├── weekly_syndrome_counts.csv│   ├── weekly_incidence_rates.csv│   ├── anomaly_flags.csv│   └── ili_weekly_trend.png│├── src/│   ├── generate_synthetic_data.py│   ├── classify_syndromes.py│   ├── weekly_aggregation.py│   ├── anomaly_detection.py│   ├── plot_surveillance_trends.py│   └── run_pipeline.py│├── sql/│   ├── syndrome_classification.sql│   ├── weekly_aggregation.sql│   └── incidence_and_anomaly.sql│└── README.mdShow more lines

## Assumptions & Limitations

All data are fully synthetic and simplified
Syndrome definitions are illustrative, not exhaustive
No risk adjustment or seasonality modeling is applied
Anomaly thresholds are conservative and rule‑based for transparency

The project structure is intentionally extensible to support future enhancements such as laboratory data integration or multi‑year baselines.


Author:
Emily Matthews, MPH
Public Health Surveillance & Health Analytics
(Portfolio sample — synthetic data only)


## How to Run This Project
This guide describes how to execute the pipeline end‑to‑end in a clean, reproducible manner.

Prerequisites

Python 3.8+
Required Python packages:

pandas
numpy
matplotlib



Install dependencies:
Shellpython -m pip install pandas numpy matplotlibShow more lines

Recommended Execution Order
The pipeline is designed to be run either step‑by‑step or via a single orchestration script.

Option 1: Run the Full Pipeline (Recommended)
From the project root directory:
Shellpython src/run_pipeline.pyShow more lines
This will:

Generate synthetic ED visit data
Classify syndromes
Aggregate weekly counts and incidence rates
Detect anomalous increases
Produce a surveillance time‑series visualization

All outputs will be written to the outputs/ directory.

Option 2: Run Components Individually
Each analytic step can also be run independently:
Shellpython src/generate_synthetic_data.pypython src/classify_syndromes.pypython src/weekly_aggregation.pypython src/anomaly_detection.pypython src/plot_surveillance_trends.py``Show more lines
This approach is useful for:

Re‑running specific stages
Inspecting intermediate outputs
Extending or modifying individual components


Outputs
After successful execution, the following files will be available:

weekly_syndrome_counts.csv
weekly_incidence_rates.csv
anomaly_flags.csv
ili_weekly_trend.png

These files represent standard public‑health surveillance deliverables suitable for downstream review, reporting, or visualization.

SQL Examples
The sql/ directory contains example queries that reproduce core surveillance logic using SQL. These are illustrative and intended for execution in a database environment after loading the relevant CSV inputs.
