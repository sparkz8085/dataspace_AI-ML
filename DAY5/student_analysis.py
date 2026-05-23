import argparse
from pathlib import Path

import pandas as pd


def find_input_file(explicit_path: str | None) -> Path:
    if explicit_path:
        path = Path(explicit_path)
        if not path.exists():
            raise FileNotFoundError(f"Input CSV not found: {path}")
        return path

    candidates = [
        Path("DAY5/Students (1).csv"),
        Path("DAY5/students.csv"),
        Path("DAY5/students_data.csv"),
    ]

    for candidate in candidates:
        if candidate.exists():
            return candidate

    raise FileNotFoundError(
        "No input CSV found. Expected one of: "
        "DAY5/Students (1).csv, DAY5/students.csv, DAY5/students_data.csv"
    )


def ensure_required_columns(df: pd.DataFrame, required: set[str]) -> None:
    missing = required - set(df.columns)
    if missing:
        cols = ", ".join(sorted(missing))
        raise ValueError(f"Missing required columns: {cols}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Run DAY5 pandas tasks from note.txt on a student CSV file."
    )
    parser.add_argument(
        "--input",
        help="Path to input CSV file. If omitted, script auto-detects DAY5 CSV files.",
    )
    parser.add_argument(
        "--output",
        default="DAY5/students_with_status.csv",
        help="Path to save DataFrame with computed Status column.",
    )
    args = parser.parse_args()

    input_path = find_input_file(args.input)
    df = pd.read_csv(input_path)

    print(f"Using input file: {input_path}")
    print("\n1) Full DataFrame")
    print(df)

    ensure_required_columns(df, {"Name", "Marks"})

    print("\n2) Name and Marks columns")
    print(df[["Name", "Marks"]])

    print("\n3) Students with Marks > 85")
    print(df[df["Marks"] > 85])

    if "City" in df.columns:
        print("\n4) Students from Kolkata")
        print(df[df["City"].str.lower() == "kolkata"])
    else:
        print("\n4) Skipped: City column not present in this file")

    print("\n5) Average marks of all students")
    print(df["Marks"].mean())

    print("\n6) Student(s) with highest marks")
    max_marks = df["Marks"].max()
    print(df[df["Marks"] == max_marks])

    if "City" in df.columns:
        print("\n7) Count of students in each city")
        print(df["City"].value_counts())
    else:
        print("\n7) Skipped: City column not present in this file")

    print("\n8) Add Status column (Pass if Marks >= 80 else Fail)")
    df["Status"] = df["Marks"].apply(lambda m: "Pass" if m >= 80 else "Fail")
    print(df[["Name", "Marks", "Status"]])

    print("\n9) Top 3 students by Marks (descending)")
    sorted_df = df.sort_values(by="Marks", ascending=False)
    print(sorted_df.head(3))

    if "Gender" in df.columns:
        print("\n10) Average marks grouped by Gender")
        print(df.groupby("Gender")["Marks"].mean())
    else:
        print("\n10) Skipped: Gender column not present in this file")

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    sorted_df.to_csv(output_path, index=False)
    print(f"\nSaved sorted DataFrame with Status to: {output_path}")


if __name__ == "__main__":
    main()
