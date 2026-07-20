from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_ROOT))

from etl.extract import Extractor
from etl.validation import DataValidator

RAW_DATA_PATH = PROJECT_ROOT / "data" / "raw"

extractor = Extractor(RAW_DATA_PATH)
validator = DataValidator()

df = extractor.load_csv(
    "product_category_name_translation.csv"
)

validator.validate_not_empty(df)

validator.validate_required_columns(
    df,
    [
        "product_category_name",
        "product_category_name_english",
    ],
)

print("=" * 50)
print("VALIDATION PASSED")
print("=" * 50)

print(f"Rows              : {len(df):,}")
print(f"Columns           : {len(df.columns)}")
print(f"Duplicate Rows    : {validator.count_duplicate_rows(df):,}")
print(f"Missing Values    : {validator.count_missing_values(df):,}")