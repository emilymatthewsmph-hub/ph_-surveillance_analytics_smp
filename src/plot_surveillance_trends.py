

import matplotlib
matplotlib.use("Agg")

import pandas as pd
import matplotlib.pyplot as plt
import os

INPUT_PATH = "data/weekly_incidence_rates.csv"
OUTPUT_DIR = "outputs"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "ili_weekly_trend.png")
df = pd.read_csv(INPUT_PATH, parse_dates=["week"])
county_filter = "CountyA"
age_group_filter = "18-64"

df_plot = df[
    (df["county"] == county_filter) &
    (df["age_group"] == age_group_filter)
].sort_values("week")

plt.figure()
plt.plot(
    df_plot["week"],
    df_plot["ili_rate"],
    marker="o"
)

plt.title("Weekly Influenza-Like Illness (ILI) Rate\nCountyA, Ages 18–64")
plt.xlabel("Week")
plt.ylabel("ILI cases per 100,000")

plt.xticks(rotation=45)
plt.tight_layout()
os.makedirs(OUTPUT_DIR, exist_ok=True)
plt.savefig(OUTPUT_PATH)
plt.close()

print(f"Visualization saved to: {OUTPUT_PATH}")


