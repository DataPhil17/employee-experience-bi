import pandas as pd  
from pathlib import Path

RAW_PATH = Path("data/raw/hr_attrition.csv")
OUT_PATH = Path("data/processed/employee_clean.csv")

def main():
    df = pd.read_csv(RAW_PATH)

    # Standardize column names
    df.columns = (
        df.columns.str.strip()
        .str.replace(" ", "_")
        .str.replace("-", "_")
        .str.lower()
    )

    # Attrition flag
    df["attrition_flag"] = df["attrition"].map({"Yes": 1, "No": 0})

    # Tenure
    df["tenure_years"] = df["yearsatcompany"]
    df["tenure_band"] = pd.cut(
        df["tenure_years"],
        bins=[-0.1, 1, 2, 5, 10, 50],
        labels=["0-1", "1-2", "2-5", "5-10", "10+"]
    )

    # Age band
    df["age_band"] = pd.cut(
        df["age"],
        bins=[0, 24, 34, 44, 54, 100],
        labels=["<25", "25-34", "35-44", "45-54", "55+"]
    )

    # Overtime normalization
    df["overtime_flag"] = df["overtime"].map({"Yes": 1, "No": 0})

    # Select columns for BI (clean semantic layer)
    cols = [
        "employeenumber",
        "department",
        "jobrole",
        "joblevel",
        "educationfield",
        "gender",
        "age",
        "age_band",
        "monthlyincome",
        "overtime",
        "overtime_flag",
        "distancefromhome",
        "jobsatisfaction",
        "worklifebalance",
        "tenure_years",
        "tenure_band",
        "attrition",
        "attrition_flag"
    ]

    df_out = df[cols].copy()
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    df_out.to_csv(OUT_PATH, index=False)

    print(f"Clean dataset written: {OUT_PATH}")

if __name__ == "__main__":
    main()
