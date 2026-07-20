from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_ROOT))

from etl.extract import Extractor
from etl.transform import DataTransformer
from etl.validation import DataValidator
from etl.load import DataLoader

RAW_DATA_PATH = PROJECT_ROOT / "data" / "raw"

extractor = Extractor(RAW_DATA_PATH)
validator = DataValidator()
transformer = DataTransformer()
loader = DataLoader()

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

df = transformer.clean_strings(df)
df = transformer.replace_empty_strings(df)
df = transformer.remove_duplicates(df)

rows = loader.load_dataframe(
    "retail.category_translation",
    df,
)

print(f"\nLoaded {rows:,} rows successfully.")