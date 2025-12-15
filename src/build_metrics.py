import pandas as pd
from pathlib import Path

IN_PATH = Path("data/processed/employee_clean.csv")
OUT_PATH = Path("data/processed/attrition_metrics.csv")

def main():
    df = pd.read_csv(IN_PATH)

    # Common HR groupings for self-service
    group_cols = ["department", "jobrole", "joblevel", "tenure_band", "overtime"]
    group_cols = [c for c in group_cols if c in df.columns]

    if "attrition_flag" not in df.columns:
        raise ValueError("attrition_flag missing. Re-run src/clean_hr.py")

    metrics = (
        df.groupby(group_cols, dropna=False)
          .agg(
              employees=("attrition_flag", "size"),
              attritions=("attrition_flag", "sum"),
              avg_monthly_income=("monthlyincome", "mean") if "monthlyincome" in df.columns else ("attrition_flag","mean"),
          )
          .reset_index()
    )
    metrics["attrition_rate"] = metrics["attritions"] / metrics["employees"]

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    metrics.to_csv(OUT_PATH, index=False)
    print(f"Wrote: {OUT_PATH} ({len(metrics):,} rows)")

if __name__ == "__main__":
    main()
