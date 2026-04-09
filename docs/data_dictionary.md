# Data Dictionary

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
