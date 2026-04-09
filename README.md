## Project Overview

This repository contains a self‑contained **public health syndromic surveillance analytics sample** designed to reflect workflows used by the CDC, state health departments, and HHS‑supported surveillance programs. The project demonstrates how emergency department (ED) visit data can be transformed into standardized surveillance indicators and anomaly signals to support situational awareness.

All data used in this project are fully synthetic and contain no protected health information (PHI).

---

## Final Product Workflow (508-Friendly)
Overview
This workflow describes the end‑to‑end transformation of synthetic emergency department (ED) visit data into standardized surveillance outputs designed to support public health situational awareness. Each step produces explicitly defined outputs that serve as inputs for the subsequent step.
All steps are executed sequentially and are independently reproducible.

Step 1: Synthetic Data Generation
Input:
No external input data required.
Process:
A synthetic dataset of emergency department (ED) visits is generated to mimic the structure and variability of real-world ED encounter data. The dataset includes visit date, patient demographics, geographic indicators, chief complaint text, and diagnosis codes.
Output:

data/ed_visits.csv


Step 2: Syndrome Classification
Input:

data/ed_visits.csv

Process:
Each ED visit is classified into one or more respiratory syndrome categories using deterministic, rule-based logic derived from diagnosis codes.
The following syndrome indicators are generated:

Influenza-Like Illness (ILI)
COVID-Like Illness (CLI)
RSV-Like Illness

Output:

data/ed_visits_classified.csv


Step 3: Weekly Aggregation and Incidence Rate Calculation
Input:

data/ed_visits_classified.csv
data/population.csv

Process:
Visit-level data are aggregated into weekly surveillance indicators stratified by county and age group. Syndrome-specific visit counts are calculated and converted into incidence rates per 100,000 population using external population denominators.
Outputs:

outputs/weekly_syndrome_counts.csv
outputs/weekly_incidence_rates.csv


Step 4: Anomaly Detection and Signal Flagging
Input:

outputs/weekly_incidence_rates.csv

Process:
Weekly incidence rates are evaluated against rolling historical baselines computed from prior reporting periods. Rule-based thresholds are applied to identify unusually elevated rates. These flags represent surveillance signals for epidemiologic review and do not imply confirmed outbreaks.
Output:

outputs/anomaly_flags.csv


Step 5: Epidemiologic Visualization
Input:

outputs/weekly_incidence_rates.csv
outputs/anomaly_flags.csv

Process:
Time-series visualizations are generated to display weekly trends in respiratory syndrome activity. Visual outputs are designed for non-interactive, server-safe execution and support high-level situational awareness.
Output:

outputs/ili_weekly_trend.png


Step 6: Orchestration and Reproducibility
Input:
All required inputs from previous steps.
Process:
A lightweight orchestration script (run_pipeline.py) executes each step in the defined order. The orchestration layer contains no analytic logic and exists solely to coordinate reproducible execution of the pipeline.
Final Outputs:
All outputs described above are reproducible from a single execution path or from individual step execution.

# Accessibility and Compliance Notes

All workflow descriptions are linear and text-based.
No information is conveyed solely through visual position, color, or shape.
Each processing step is labeled with explicit inputs, processes, and outputs.
File names and terminology are consistent across documentation.
Visual products are accompanied by text-based explanations elsewhere in documentation.


Intended Use
This workflow reflects analytic patterns commonly used in:

CDC syndromic surveillance systems
State and local health department surveillance units
HHS-supported situational awareness analytics

The design prioritizes interpretability, traceability, and reproducibility to support regulatory, operational, and analytic review.
## Analytic Capabilities

This project demonstrates:

- Rule‑based classification of ED visits into respiratory syndromes (ILI, COVID‑like illness, RSV‑like illness)
- Weekly aggregation and calculation of incidence rates per 100,000 population
- Rule‑based anomaly detection using rolling historical baselines
- Epidemiologic time‑series visualization for surveillance trend monitoring
- Parallel implementation of core logic in Python and SQL

The analytic emphasis is on **transparency, interpretability, and reproducibility**, consistent with federal public health surveillance practices.

---

## Folder Structure

```text
ph_surveillance_analytics_smp/
├── data/
│   ├── ed_visits.csv
│   ├── lab_results.csv
│   └── population.csv
│
├── outputs/
│   ├── weekly_syndrome_counts.csv
│   ├── weekly_incidence_rates.csv
│   ├── anomaly_flags.csv
│   └── ili_weekly_trend.png
│
├── src/
│   ├── generate_synthetic_data.py
│   ├── classify_syndromes.py
│   ├── weekly_aggregation.py
│   ├── anomaly_detection.py
│   ├── plot_surveillance_trends.py
│   └── run_pipeline.py
│
├── sql/
│   ├── syndrome_classification.sql
│   ├── weekly_aggregation.sql
│   └── incidence_and_anomaly.sql
│
├── docs/
│   ├── portfolio_summary.md
│   ├── assumptions.md
│   ├── data_dictionary.md
│   ├── limitations.md
│   ├── technical_appendix.md
│   └── future_enhancements.md
│
└── README.md
``

## Surveillance Pipeline Overview

This pipeline illustrates the transformation of synthetic ED visit data into weekly surveillance indicators, anomaly signals, and epidemiologic visualizations through a modular, orchestrated workflow.

┌──────────────────────────────┐
│ generate_synthetic_data.py   │
│ - create synthetic ED visits │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│ data/ed_visits.csv           │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│ classify_syndromes.py        │
│ - ILI / CLI / RSV flags      │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│ weekly_aggregation.py        │
│ - weekly counts              │
│ - incidence rates            │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│ anomaly_detection.py         │
│ - rolling baselines          │
│ - anomaly flags              │
└──────────────┬───────────────┘
               │
     ┌─────────┴─────────┐
     ▼                   ▼
┌───────────────┐  ┌────────────────────┐
│ anomaly_flags │  │ plot_surveillance  │
│ .csv          │  │ _trends.py          │
└───────────────┘  │ - time series plot  │
                   └──────────┬─────────┘
                              │
                              ▼
                   ┌────────────────────┐
                   │ outputs/ili_weekly │
                   │ _trend.png         │
                   └────────────────────┘
``
