from pathlib import Path

import pandas as pd


class Extractor:
    """
    Reads datasets from disk.
    """

    def __init__(self, raw_data_path: Path):

        self.raw_data_path = raw_data_path

    def load_csv(self, filename: str) -> pd.DataFrame:
        """
        Load a CSV file into a DataFrame.
        """

        file_path = self.raw_data_path / filename

        if not file_path.exists():
            raise FileNotFoundError(f"{filename} not found.")

        return pd.read_csv(file_path)