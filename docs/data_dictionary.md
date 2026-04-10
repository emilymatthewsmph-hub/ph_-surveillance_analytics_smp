##  Data Dictionary

This document describes the structure and meaning of all datasets used or produced by the respiratory surveillance analytics pipeline. It is intended to support transparency, reproducibility, and auditability.

# 1. Input Datasets

1.1 ed_visits.csv — Synthetic Emergency Department Visits

 |Column |Type |Description |
 |------------|-------------|
|visit_id|	Integer|	Unique identifier for each ED encounter|
|patient_id| Integer|	Synthetic patient identifier; may appear in multiple visits|
|age|	Integer|	Patient age in years|
|sex|	String|	Patient sex (“M” or “F”)|
|county|	String|	County where the visit occurred (CountyA, CountyB, CountyC)|
|chief_complaint|	String|Free‑text presenting symptoms|
|diagnosis_code |	String |	ICD‑10 code assigned at discharge|
|visit_date|	Date|	Date of ED encounter|

1.2 population.csv — Population Denominators

 |Column |Type |Description |
|------------|-------------|
county	String	County name.
age_group	String	Age category (0‑17, 18‑64, 65+).
population	Integer	Population count for the county/age group.

1.3 lab_results.csv — Optional Synthetic Lab Data
(Not used in the core pipeline but included for future enhancements.)

|Column |Type |Description |
|------------|-------------|
patient_id	Integer	Synthetic patient identifier.
test_type	String	Test modality (PCR, antigen).
pathogen	String	Pathogen tested (Flu A, RSV, SARS‑CoV‑2).
result	String	Test result (“positive” or “negative”).
collection_date	Date	Date specimen was collected.

# 2. Intermediate Outputs
2.1 ed_visits_classified.csv — Syndrome‑Flagged ED Visits

|Column |Type |Description |
|------------|-------------|
ili_flag	Boolean	True if ICD‑10 code indicates ILI.
cli_flag	Boolean	True if ICD‑10 code indicates CLI.
rsv_flag	Boolean	True if ICD‑10 code indicates RSV‑like illness.
age_group	String	Derived age category.
week	Date	ISO week start date.
(Includes all original ED visit fields.)

# 3. Final Outputs
3.1 weekly_syndrome_counts.csv

|Column |Type |Description |
|------------|-------------|
week	Date	Week start date.
county	String	County name.
age_group	String	Age category.
ili_visits	Integer	Weekly ILI visit count.
cli_visits	Integer	Weekly CLI visit count.
rsv_visits	Integer	Weekly RSV‑like visit count.
total_visits	Integer	Total ED visits for the week.
3.2 weekly_incidence_rates.csv
Column	Type	Description
ili_rate	Float	ILI incidence per 100,000 population.
cli_rate	Float	CLI incidence per 100,000 population.
rsv_rate	Float	RSV‑like incidence per 100,000 population.
(Includes all columns from weekly_syndrome_counts.csv.)

3.3 weekly_surveillance_signals.csv
|Column |Type |Description |
|------------|-------------|
ili_baseline_rate	Float	Rolling 4‑week baseline for ILI.
ili_pct_change	Float	Percent change from baseline.
ili_signal_flag	Integer	1 if signal criteria met.
cli_baseline_rate	Float	Rolling 4‑week baseline for CLI.
cli_pct_change	Float	Percent change from baseline.
cli_signal_flag	Integer	1 if signal criteria met.
rsv_baseline_rate	Float	Rolling 4‑week baseline for RSV.
rsv_pct_change	Float	Percent change from baseline.
rsv_signal_flag	Integer	1 if signal criteria met.
3.4 ili_weekly_trend.png
A CDC‑style epidemiologic line plot showing weekly ILI incidence for a selected county and age group.

## ED Visit Data (`ed_visits.csv`)

| Column Name | Description |
|------------|-------------|
| visit_id | Unique synthetic identifier for each ED visit |
| patient_id | Synthetic patient identifier |
| age | Age at visit |
| sex | Patient sex |
| county | County of residence |
| chief_complaint | Free-text chief complaint |
| diagnosis_code | ICD-10-like diagnosis code |
| visit_date | Date of ED visit |

## Population Data (`population.csv`)

| Column Name | Description |
|------------|-------------|
| county | County name |
| age_group | Age group category |
| population | Population count used as denominator |

## Weekly Surveillance Outputs

### Weekly Syndrome Counts
- Total ED visits by syndrome, county, age group, and week

### Weekly Incidence Rates
- Syndrome-specific rates per 100,000 population

### Anomaly Flags
- Binary flags indicating elevated activity relative to historical baselines
``
