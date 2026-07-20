from pathlib import Path

from etl.extract import Extractor
from etl.validation import DataValidator
from etl.transform import DataTransformer
from etl.load import DataLoader


class ETLPipeline:

    def __init__(self, raw_data_path: Path):

        self.extractor = Extractor(raw_data_path)
        self.validator = DataValidator()
        self.transformer = DataTransformer()
        self.loader = DataLoader()

    def run(
        self,
        file_name: str,
        table_name: str,
        required_columns: list[str],
        conflict_columns: list[str] | None = None,
    ):

        print("=" * 60)
        print(f"Processing: {file_name}")
        print("=" * 60)

        # Extract
        df = self.extractor.load_csv(file_name)

        # Validate
        self.validator.validate_not_empty(df)

        self.validator.validate_required_columns(
            df,
            required_columns,
        )

        # Transform
        df = self.transformer.clean_strings(df)
        df = self.transformer.replace_empty_strings(df)
        df = self.transformer.remove_duplicates(df)

        # Load
        inserted = self.loader.load_dataframe(
            table_name=table_name,
            df=df,
            conflict_columns=conflict_columns,
        )

        print(f"Inserted Rows : {inserted}")
        print("Pipeline Completed Successfully.\n")

        return inserted