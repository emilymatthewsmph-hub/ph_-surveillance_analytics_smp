### Public Health Respiratory Surveillance Analytics (Syndromic Surveillance Sample Project)
This repository demonstrates an end‑to‑end respiratory syndromic surveillance pipeline modeled after analytic workflows used by CDC, state health departments, and federal public health contractors. The project ingests synthetic emergency department (ED) visit data, classifies respiratory syndromes, aggregates weekly indicators, calculates incidence rates, and detects surveillance signals using rule‑based anomaly logic. Equivalent SQL scripts reproduce the same indicators for warehouse‑based environments.

The project is designed to showcase both epidemiologic reasoning and data engineering rigor, using modular Python scripts, reproducible data transformations, and transparent analytic logic.

## Project Objectives
This project implements a complete surveillance workflow that:

Generates synthetic ED visit data for respiratory illness monitoring

Classifies visits into ILI, CLI, and RSV‑like syndromes

Aggregates weekly counts and incidence rates

Computes rolling baselines and percent change

Flags surveillance signals requiring epidemiologic review

Reproduces the same logic in SQL for warehouse environments

Produces a CDC‑style epidemiologic trend visualization

##Key Features
Synthetic ED data generation (Python)

Syndrome classification using ICD‑10 codes

Weekly aggregation by county and age group

Incidence rate calculation using population denominators

Surveillance signal detection using rolling 4‑week baselines

SQL parity for warehouse‑based analytics

Visualization of weekly ILI trends

Modular, reproducible pipeline with clear folder structure

## Project Architecture
The surveillance pipeline follows a layered architecture similar to CDC NSSP and state surveillance systems.

Code
                +---------------------------+
                |   Synthetic ED Data       |
                |   (ed_visits.csv)         |
                +-------------+-------------+
                              |
                              v
                +---------------------------+
                |   Syndrome Classification |
                |   (ILI / CLI / RSV)       |
                +-------------+-------------+
                              |
                              v
                +---------------------------+
                |   Weekly Aggregation      |
                |   Counts + Rates          |
                +-------------+-------------+
                              |
                              v
                +---------------------------+
                |   Surveillance Signals    |
                |   Baseline + % Change     |
                +-------------+-------------+
                              |
                              v
                +---------------------------+
                |   Visualization Output    |
                |   (ILI Trend Plot)        |
                +---------------------------+

# mermaid
flowchart TD
    A[Generate Synthetic ED Data<br>generate_synthetic_data.py] --> B[Classify Syndromes<br>classify_syndromes.py]
    B --> C[Weekly Aggregation<br>weekly_aggregation.py]
    C --> D[Incidence Rates<br>weekly_incidence_rates.csv]
    D --> E[Surveillance Signals<br>surveillance_signals.py]
    E --> F[Visualization<br>plot_surveillance_trends.py]
## Repository Structure
Code
ph_surveillance_analytics_smp/
│
├── data/
│   ├── ed_visits.csv
│   ├── population.csv
│   └── lab_results.csv
│
├── outputs/
│   ├── weekly_syndrome_counts.csv
│   ├── weekly_incidence_rates.csv
│   ├── weekly_surveillance_signals.csv
│   └── ili_weekly_trend.png
│
├── src/
│   ├── generate_synthetic_data.py
│   ├── classify_syndromes.py
│   ├── weekly_aggregation.py
│   ├── surveillance_signals.py
│   ├── plot_surveillance_trends.py
│   └── run_pipeline.py
│
├── sql/
│   ├── syndrome_classification.sql
│   ├── weekly_aggregation.sql
│   └── incidence_and_surveillance_signals.sql
│
└── docs/
    ├── assumptions.md
    ├── data_dictionary.md
    ├── technical_appendix.md
    ├── limitations.md
    ├── future_enhancements.md
    └── portfolio_summary.md
## Methods Overview
1. Synthetic ED Data Generation
Creates 5,000 synthetic ED visits with:

Age, sex, county

Chief complaint

ICD‑10 diagnosis code

Visit date

2. Syndrome Classification
Flags visits as:

ILI (J10, J11)

CLI (U07.1)

RSV‑like (J21)

3. Weekly Aggregation
Groups by:

Week

County

Age group

Outputs:

Weekly syndrome counts

Weekly incidence rates per 100,000

4. Surveillance Signal Detection
For each syndrome:

Rolling 4‑week baseline

Percent change

Signal flag if ≥ 50% increase and baseline > 0

5. SQL Parity
All indicators are reproduced using analytic SQL with window functions.

6. Visualization
Generates a CDC‑style weekly ILI trend plot.

## How to Run the Pipeline
From the project root:

Code
python src/generate_synthetic_data.py
python src/classify_syndromes.py
python src/weekly_aggregation.py
python src/surveillance_signals.py
python src/plot_surveillance_trends.py
Or run the orchestrator:

Code
python src/run_pipeline.py
# Skills Demonstrated
Public health surveillance analytics

Epidemiologic indicator development

Python data engineering

SQL analytic window functions

Modular pipeline design

Reproducible research practices

Data visualization

Documentation and technical communication

## Future Enhancements
RSV seasonality modeling

CLI subtyping (COVID vs non‑COVID viral CLI)

Age‑standardized incidence rates

ED volume normalization

Multi‑pathogen co‑circulation indicators

Integration of lab‑confirmed results

Z‑score or Bayesian signal detection

## Limitations
Synthetic data only

Simplified ICD‑10 logic

No real‑world seasonality

No spatial smoothing

No hospital‑level variation
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

