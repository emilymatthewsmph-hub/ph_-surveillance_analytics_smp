import pandas as pd
import os

INPUT_PATH = "data/ed_visits.csv"
OUTPUT_PATH = "data/ed_visits_classified.csv"

def classify_syndromes(df: pd.DataFrame) -> pd.DataFrame:
    # ILI: Influenza-like illness (J10, J11)
    df["ili_flag"] = df["diagnosis_code"].isin(["J10", "J11"])

    # CLI: COVID-like illness (U07.1)
    df["cli_flag"] = df["diagnosis_code"].isin(["U07.1"])

    # RSV-like illness (J21)
    df["rsv_flag"] = df["diagnosis_code"].isin(["J21"])

    return df

def main():
    if not os.path.exists(INPUT_PATH):
        raise FileNotFoundError(f"Input file not found: {INPUT_PATH}")

    df = pd.read_csv(INPUT_PATH, parse_dates=["visit_date"])
    df = classify_syndromes(df)

    df.to_csv(OUTPUT_PATH, index=False)
    print(f"Syndrome-classified file written to: {OUTPUT_PATH}")

if __name__ == "__main__":
    main()
