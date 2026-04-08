# ph_-surveillance_analytics_smp
Build a synthetic public health surveillance pipeline that ingests ED visit data, classifies syndromes (ILI/CLI/RSV‑like), aggregates weekly counts and rates, and flags anomalies—using Python and SQL.
resp_surveillance_project/
│
├── data/
│   ├── ed_visits.csv
│   ├── lab_results.csv        
│   └── population.csv
│
├── outputs/
│   ├── weekly_syndrome_counts.csv
│   ├── weekly_incidence_rates.csv
│   └── anomaly_flags.csv
│
├── src/
│   ├── generate_synthetic_data.py
│   ├── classify_syndromes.py
│   ├── weekly_aggregation.py
│   ├── anomaly_detection.py
│   └── run_pipeline.py
│
├── sql/
│   ├── syndrome_classification.sql
│   ├── weekly_aggregation.sql
│   └── incidence_and_anomaly.sql
│
└── README.md
