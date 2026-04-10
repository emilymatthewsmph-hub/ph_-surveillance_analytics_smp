# Portfolio Summary: Respiratory Syndromic Surveillance Analytics

This project demonstrates a complete respiratory syndromic surveillance pipeline modeled after analytic workflows used by CDC, state health departments, and federal public health contractors. It integrates epidemiologic indicator development with reproducible data engineering practices, producing a transparent and audit‑ready analytic system.

# Purpose
The project showcases the ability to design, implement, and document a modular surveillance workflow that:

Processes ED visit data

Classifies respiratory syndromes

Aggregates weekly indicators

Computes incidence rates

Detects surveillance signals

Reproduces logic in SQL

Generates epidemiologic visualizations

# Technical Scope
The pipeline includes:

Synthetic data generation

ICD‑10–based syndrome classification

Weekly aggregation and incidence rate calculation

Rolling baseline and percent‑change signal detection

Equivalent SQL scripts for warehouse environments

Visualization of weekly ILI trends

All components are implemented using modular Python scripts and analytic SQL.

# Public Health Relevance
The project reflects core elements of operational respiratory surveillance:

Weekly reporting cycles

Syndrome‑based monitoring

Baseline comparison

Percent‑change review

County‑ and age‑group stratification

Epidemiologic signal interpretation

These elements align with practices used in NSSP, RESP‑NET, ILINet, and state‑level situational awareness systems.

# Skills Demonstrated
Public health analytics

Epidemiologic indicator development

Python data engineering

SQL analytic modeling

Modular pipeline design

Reproducible research practices

Data visualization

Technical documentation


# Summary Statement
This project provides a transparent, modular, and reproducible respiratory surveillance pipeline that integrates epidemiologic reasoning with modern data engineering practices. It demonstrates the ability to design and document surveillance indicators in both Python and SQL, producing outputs suitable for analytic review, operational monitoring, and professional portfolio presentation.
The project models how emergency department (ED) visit data can be transformed into actionable surveillance indicators through syndrome classification, weekly aggregation, incidence rate calculation, anomaly detection, and visualization. All data used in this project is fully synthetic and contains no protected health information (PHI).

This sample is intended to demonstrate:
- Public health surveillance domain knowledge
- Modular analytic pipeline design
- Python and SQL parity for production environments
- Rule-based anomaly detection for situational awareness
- Reproducible, auditable analytics suitable for federal use

The analytic emphasis is on **transparency, interpretability, and operational realism**, not prediction or machine learning. This reflects best practices in federal and state public health surveillance settings, where indicators must be explainable, reviewable, and defensible.

The project is designed as a standalone example but is intentionally extensible to additional data sources, multi-year baselines, and production scheduling frameworks.
