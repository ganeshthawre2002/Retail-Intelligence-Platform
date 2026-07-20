from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_ROOT))

from etl.extract import Extractor
from etl.transform import DataTransformer

RAW_DATA_PATH = PROJECT_ROOT / "data" / "raw"

extractor = Extractor(RAW_DATA_PATH)
transformer = DataTransformer()

df = extractor.load_csv(
    "product_category_name_translation.csv"
)

print("Rows Before:", len(df))

df = transformer.clean_strings(df)
df = transformer.replace_empty_strings(df)
df = transformer.remove_duplicates(df)

print("Rows After:", len(df))

