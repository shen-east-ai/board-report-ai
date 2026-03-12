import pandas as pd

df = pd.read_csv("sample_kpis.csv")

df["variance"] = df["actual"] - df["budget"]

print("\nKPI Variance Summary\n")

for index, row in df.iterrows():
    print(f"{row['metric']}:")
    print(f"  Actual: {row['actual']}")
    print(f"  Budget: {row['budget']}")
    print(f"  Variance: {row['variance']}\n")
