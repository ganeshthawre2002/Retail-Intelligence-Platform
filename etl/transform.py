import pandas as pd


class DataTransformer:
    """
    Performs reusable data transformations.
    """

    def clean_strings(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Strip whitespace from string columns.
        """

        df = df.copy()

        object_columns = df.select_dtypes(include="object").columns

        for column in object_columns:
            df[column] = df[column].str.strip()

        return df

    def replace_empty_strings(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Replace empty strings with missing values.
        """

        df = df.replace("", pd.NA)

        return df

    def remove_duplicates(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Remove duplicate rows.
        """

        return df.drop_duplicates()