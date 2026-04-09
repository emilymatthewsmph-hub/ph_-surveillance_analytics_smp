## Project Overview

This repository contains a self‑contained **public health syndromic surveillance analytics sample** designed to reflect workflows used by the CDC, state health departments, and HHS‑supported surveillance programs. The project demonstrates how emergency department (ED) visit data can be transformed into standardized surveillance indicators and anomaly signals to support situational awareness.

All data used in this project are fully synthetic and contain no protected health information (PHI).

---

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

flowchart TD
    A[generate_synthetic_data.py<br/>Synthetic ED Visits]
    B[data/ed_visits.csv]
    C[classify_syndromes.py<br/>ILI / CLI / RSV Flags]
    D[weekly_aggregation.py<br/>Weekly Counts & Rates]
    E[anomaly_detection.py<br/>Rolling Baselines & Flags]
    F[outputs/anomaly_flags.csv]
    G[plot_surveillance_trends.py<br/>Time Series Visualization]
    H[outputs/ili_weekly_trend.png]

    A --> B
    B --> C
    C --> D
    D --> E
    E --> F
    E --> G
    G --> H
``
