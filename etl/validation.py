import pandas as pd


class DataValidator:
    """
    Performs basic validation on datasets before loading.
    """

    def validate_not_empty(self, df: pd.DataFrame) -> None:
        """
        Ensure the dataset contains rows.
        """

        if df.empty:
            raise ValueError("Dataset is empty.")

    def validate_required_columns(
        self,
        df: pd.DataFrame,
        required_columns: list[str],
    ) -> None:
        """
        Ensure all required columns exist.
        """

        missing = set(required_columns) - set(df.columns)

        if missing:
            raise ValueError(
                f"Missing required columns: {sorted(missing)}"
            )

    def count_duplicate_rows(self, df: pd.DataFrame) -> int:
        """
        Return the number of duplicate rows.
        """

        return int(df.duplicated().sum())

    def count_missing_values(self, df: pd.DataFrame) -> int:
        """
        Return the total number of missing values.
        """

        return int(df.isna().sum().sum())