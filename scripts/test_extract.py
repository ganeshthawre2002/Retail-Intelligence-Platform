from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_ROOT))

from etl.extract import Extractor

RAW_DATA_PATH = PROJECT_ROOT / "data" / "raw"

extractor = Extractor(RAW_DATA_PATH)

df = extractor.load_csv(
    "product_category_name_translation.csv"
)

print(df.head())

print()

print(df.shape)
