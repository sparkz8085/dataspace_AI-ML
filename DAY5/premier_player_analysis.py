"""Analyze the Premier League 2023-24 player stats CSV.

Usage:
    python3 DAY5/premier_player_analysis.py
    python3 DAY5/premier_player_analysis.py --input DAY5/premier-player-23-24.csv
    python3 DAY5/premier_player_analysis.py --output DAY5/premier-player-summary.csv
"""

from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd


def find_input_file(explicit_path: str | None) -> Path:
    """Resolve the CSV path from an explicit argument or common local locations."""

    candidates = []
    if explicit_path:
        candidates.append(Path(explicit_path))

    candidates.extend(
        [
            Path("DAY5/premier-player-23-24.csv"),
            Path("premier-player-23-24.csv"),
        ]
    )

    for candidate in candidates:
        if candidate.exists():
            return candidate

    searched = "\n".join(f"- {candidate}" for candidate in candidates)
    raise FileNotFoundError(f"Could not find the CSV file. Searched:\n{searched}")


def load_data(csv_path: Path) -> pd.DataFrame:
    """Load and normalize the Premier League player CSV."""

    df = pd.read_csv(csv_path, encoding="utf-8-sig")

    numeric_columns = [
        "Age",
        "MP",
        "Starts",
        "Min",
        "90s",
        "Gls",
        "Ast",
        "G+A",
        "G-PK",
        "PK",
        "PKatt",
        "CrdY",
        "CrdR",
        "xG",
        "npxG",
        "xAG",
        "npxG+xAG",
        "PrgC",
        "PrgP",
        "PrgR",
        "Gls_90",
        "Ast_90",
        "G+A_90",
        "G-PK_90",
        "G+A-PK_90",
        "xG_90",
        "xAG_90",
        "xG+xAG_90",
        "npxG_90",
        "npxG+xAG_90",
    ]

    for column in numeric_columns:
        if column in df.columns:
            df[column] = pd.to_numeric(df[column], errors="coerce")

    return df


def print_summary(df: pd.DataFrame) -> None:
    """Print a compact summary of the dataset."""

    print(f"Rows: {len(df)}")
    print(f"Columns: {len(df.columns)}")
    print("\nColumns:")
    print(", ".join(df.columns))

    print("\nTop 5 players by goals:")
    if "Gls" in df.columns:
        top_goals = df.sort_values(by="Gls", ascending=False).head(5)
        print(top_goals[[col for col in ["Player", "Team", "Pos", "Age", "Gls"] if col in top_goals.columns]].to_string(index=False))

    print("\nTop 5 players by assists:")
    if "Ast" in df.columns:
        top_assists = df.sort_values(by="Ast", ascending=False).head(5)
        print(top_assists[[col for col in ["Player", "Team", "Pos", "Age", "Ast"] if col in top_assists.columns]].to_string(index=False))

    print("\nTop 5 players by expected goal contribution (xG+xAG):")
    if "xG+xAG" in df.columns:
        top_xg_xag = df.sort_values(by="xG+xAG", ascending=False).head(5)
        print(top_xg_xag[[col for col in ["Player", "Team", "Pos", "Age", "xG+xAG"] if col in top_xg_xag.columns]].to_string(index=False))

    print("\nPlayers by position:")
    if "Pos" in df.columns:
        print(df["Pos"].value_counts().to_string())

    print("\nAverage age by position:")
    if "Pos" in df.columns and "Age" in df.columns:
        print(df.groupby("Pos", dropna=False)["Age"].mean().round(2).sort_values(ascending=False).to_string())


def build_summary_table(df: pd.DataFrame) -> pd.DataFrame:
    """Create a small summary table that can be exported to CSV."""

    summary_columns = [col for col in ["Player", "Nation", "Pos", "Age", "Team", "MP", "Starts", "Min", "Gls", "Ast", "xG", "xAG", "xG+xAG"] if col in df.columns]
    summary = df.loc[:, summary_columns].copy()

    sort_col = "Gls" if "Gls" in summary.columns else summary_columns[-1]
    return summary.sort_values(by=sort_col, ascending=False)


def main() -> None:
    parser = argparse.ArgumentParser(description="Analyze the Premier League 2023-24 player stats CSV.")
    parser.add_argument("--input", help="Path to premier-player-23-24.csv")
    parser.add_argument("--output", help="Optional path to save a summary CSV")
    args = parser.parse_args()

    csv_path = find_input_file(args.input)
    print(f"Using input file: {csv_path}")

    df = load_data(csv_path)
    print_summary(df)

    if args.output:
        output_path = Path(args.output)
        summary = build_summary_table(df)
        summary.to_csv(output_path, index=False)
        print(f"\nSaved summary to: {output_path}")


if __name__ == "__main__":
    main()