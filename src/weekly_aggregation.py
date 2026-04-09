import pandas as pd
import os

INPUT_PATH = "data/ed_visits_classified.csv"
POP_PATH = "data/population.csv"
OUT_COUNTS = "data/weekly_syndrome_counts.csv"
OUT_RATES = "data/weekly_incidence_rates.csv"

def assign_age_group(age):
    if age < 18:
        return "0-17"
    elif age < 65:
        return "18-64"
    else:
        return "65+"

def main():
    if not os.path.exists(INPUT_PATH):
        raise FileNotFoundError(f"Input file not found: {INPUT_PATH}")

    df = pd.read_csv(INPUT_PATH, parse_dates=["visit_date"])

    # Add age group
    df["age_group"] = df["age"].apply(assign_age_group)

    # Add week (ISO week)
    df["week"] = df["visit_date"].dt.to_period("W").apply(lambda r: r.start_time)

    # Weekly syndrome counts
    weekly = df.groupby(["week", "county", "age_group"]).agg(
        ili_visits=("ili_flag", "sum"),
        cli_visits=("cli_flag", "sum"),
        rsv_visits=("rsv_flag", "sum"),
        total_visits=("visit_id", "count")
    ).reset_index()

    weekly.to_csv(OUT_COUNTS, index=False)

    # Load population denominators
    pop = pd.read_csv(POP_PATH)

    # Join and compute incidence rates
    merged = weekly.merge(pop, on=["county", "age_group"], how="left")

    for syndrome in ["ili", "cli", "rsv"]:
        merged[f"{syndrome}_rate"] = (
            merged[f"{syndrome}_visits"] / merged["population"] * 100000
        )

    merged.to_csv(OUT_RATES, index=False)

    print(f"Weekly counts written to: {OUT_COUNTS}")
    print(f"Weekly incidence rates written to: {OUT_RATES}")

if __name__ == "__main__":
    main()
