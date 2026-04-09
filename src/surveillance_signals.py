
import pandas as pd
import os

INPUT_PATH = "data/weekly_incidence_rates.csv"
OUTPUT_PATH = "data/weekly_surveillance_signals.csv"

BASELINE_WEEKS = 4
PERCENT_INCREASE_THRESHOLD = 0.50  # 50% increase


def calculate_signals(
    df: pd.DataFrame,
    syndrome: str,
    baseline_weeks: int,
    pct_threshold: float,
) -> pd.DataFrame:
    """
    Calculate surveillance signals for a given syndrome.
    """

    rate_col = f"{syndrome}_rate"
    signal_col = f"{syndrome}_signal_flag"
    baseline_col = f"{syndrome}_baseline_rate"
    pct_change_col = f"{syndrome}_pct_change"

    df = df.sort_values("week")

    # Rolling baseline (previous N weeks)
    df[baseline_col] = (
        df.groupby(["county", "age_group"])[rate_col]
        .transform(lambda x: x.shift(1).rolling(baseline_weeks).mean())
    )

    # Percent change from baseline
    df[pct_change_col] = (
        (df[rate_col] - df[baseline_col]) / df[baseline_col]
    )

    # Signal criteria
    df[signal_col] = (
        (df[pct_change_col] >= pct_threshold)
        & (df[baseline_col] > 0)
    ).astype(int)

    return df


def main():
    if not os.path.exists(INPUT_PATH):
        raise FileNotFoundError(f"Input file not found: {INPUT_PATH}")

    df = pd.read_csv(INPUT_PATH, parse_dates=["week"])

    for syndrome in ["ili", "cli", "rsv"]:
        df = calculate_signals(
            df,
            syndrome=syndrome,
            baseline_weeks=BASELINE_WEEKS,
            pct_threshold=PERCENT_INCREASE_THRESHOLD,
        )

    df.to_csv(OUTPUT_PATH, index=False)

    print("Surveillance signal detection complete.")
    print(f"Signals written to: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
