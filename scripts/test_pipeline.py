from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_ROOT))

from etl.pipeline import ETLPipeline

RAW_DATA_PATH = PROJECT_ROOT / "data" / "raw"

pipeline = ETLPipeline(RAW_DATA_PATH)

pipeline.run(
    file_name="product_category_name_translation.csv",
    table_name="retail.category_translation",
    required_columns=[
        "product_category_name",
        "product_category_name_english",
    ],
    conflict_columns=[
        "product_category_name",
    ],
)