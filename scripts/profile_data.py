from pathlib import Path

import pandas as pd


# ==========================================================
# Project Paths
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW_DATA_PATH = PROJECT_ROOT / "data" / "raw"


# ==========================================================
# Load Datasets
# ==========================================================

def load_datasets(data_path: Path) -> dict[str, pd.DataFrame]:
    """
    Load all CSV datasets from the given directory.
    """

    datasets = {}

    csv_files = sorted(data_path.glob("*.csv"))

    print(f"\nFound {len(csv_files)} CSV file(s).\n")

    for file in csv_files:
        try:
            df = pd.read_csv(file)

            datasets[file.stem] = df

            print(
                f"✓ Loaded {file.name:<45}"
                f"({df.shape[0]:>8,} rows, {df.shape[1]:>2} columns)"
            )

        except Exception as e:
            print(f"✗ Failed to load {file.name}")
            print(e)

    return datasets


# ==========================================================
# Dataset Summary
# ==========================================================

def print_dataset_summary(datasets: dict[str, pd.DataFrame]) -> None:
    """
    Display a profiling summary for every dataset.
    """

    print("\n")
    print("=" * 125)

    print(
        f"{'Dataset':40}"
        f"{'Rows':>12}"
        f"{'Cols':>8}"
        f"{'Missing':>12}"
        f"{'Duplicates':>14}"
        f"{'Memory(MB)':>15}"
    )

    print("=" * 125)

    for name, df in datasets.items():

        rows = df.shape[0]
        cols = df.shape[1]
        missing = df.isna().sum().sum()
        duplicates = df.duplicated().sum()
        memory = df.memory_usage(deep=True).sum() / 1024 / 1024

        print(
            f"{name:40}"
            f"{rows:>12,}"
            f"{cols:>8}"
            f"{missing:>12,}"
            f"{duplicates:>14,}"
            f"{memory:>15.2f}"
        )

    print("=" * 125)


# ==========================================================
# Column Profile
# ==========================================================

def print_column_profile(datasets: dict[str, pd.DataFrame]) -> None:
    """
    Display column-level information for every dataset.
    """

    for dataset_name, df in datasets.items():

        print("\n")
        print("=" * 100)
        print(f"DATASET: {dataset_name}")
        print("=" * 100)

        print(
            f"{'Column':35}"
            f"{'Data Type':15}"
            f"{'Missing':>12}"
            f"{'Unique':>12}"
        )

        print("-" * 100)

        for column in df.columns:

            dtype = str(df[column].dtype)
            missing = df[column].isna().sum()
            unique = df[column].nunique()

            print(
                f"{column:35}"
                f"{dtype:15}"
                f"{missing:>12,}"
                f"{unique:>12,}"
            )


# ==========================================================
# Primary Key Candidates
# ==========================================================

def print_primary_key_candidates(datasets: dict[str, pd.DataFrame]) -> None:
    """
    Identify columns that could serve as primary keys.
    """

    print("\n")
    print("=" * 100)
    print("PRIMARY KEY CANDIDATES")
    print("=" * 100)

    for dataset_name, df in datasets.items():

        candidates = []

        for column in df.columns:

            if (
                df[column].isna().sum() == 0
                and df[column].nunique() == len(df)
            ):
                candidates.append(column)

        print(f"\n{dataset_name}")

        if candidates:
            for column in candidates:
                print(f"   ✓ {column}")
        else:
            print("   No obvious primary key candidate found.")




# ==========================================================
# inspections of unique columns in suspiciuos datasets 
# ==========================================================


def inspect_unique_columns(datasets: dict[str, pd.DataFrame], dataset_name: str) -> None:
    """
    Display the number of unique values for each column in a dataset.
    """

    df = datasets[dataset_name]

    print(f"\n{'=' * 80}")
    print(f"UNIQUE VALUE ANALYSIS: {dataset_name}")
    print("=" * 80)

    for column in df.columns:
        unique = df[column].nunique()
        total = len(df)

        print(f"{column:35} {unique:>10,} / {total:,}")


    

# =========================================================
# inspecting duplicate review ids 
# =========================================================

# ==========================================================
# Inspect Duplicate Review IDs
# ==========================================================

def inspect_duplicate_review_ids(datasets: dict[str, pd.DataFrame]) -> None:
    """
    Display duplicate review IDs.
    """

    df = datasets["olist_order_reviews_dataset"]

    duplicates = df[df.duplicated(subset=["review_id"], keep=False)]

    print("\n")
    print("=" * 100)
    print("DUPLICATE REVIEW IDs")
    print("=" * 100)

    if duplicates.empty:
        print("No duplicate review IDs found.")
    else:
        print(duplicates.sort_values("review_id"))
















# ==========================================================
# Main
# ==========================================================

def main():

    print("=" * 60)
    print("Retail Intelligence Platform")
    print("Data Profiling Tool")
    print("=" * 60)

    datasets = load_datasets(RAW_DATA_PATH)

    print_dataset_summary(datasets)

    print_column_profile(datasets)

    print_primary_key_candidates(datasets)


    inspect_unique_columns(datasets, "olist_order_items_dataset")
    inspect_unique_columns(datasets, "olist_order_payments_dataset")
    inspect_unique_columns(datasets, "olist_order_reviews_dataset")

    inspect_duplicate_review_ids(datasets)


# ==========================================================
# Entry Point
# ==========================================================

if __name__ == "__main__":
    main()