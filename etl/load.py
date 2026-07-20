from pathlib import Path
import sys

# ==========================================================
# Make Project Root Importable
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_ROOT))

# ==========================================================
# Imports
# ==========================================================

from database.connection import get_connection


# ==========================================================
# Data Loader
# ==========================================================

class DataLoader:
    """
    Loads pandas DataFrames into PostgreSQL.
    """

    def load_dataframe(
        self,
        table_name: str,
        df,
        conflict_columns: list[str] | None = None,
    ) -> int:
        """
        Load a pandas DataFrame into PostgreSQL.

        Returns
        -------
        int
            Number of inserted rows.
        """

        conn = get_connection()
        cursor = conn.cursor()

        try:

            columns = list(df.columns)

            column_sql = ", ".join(columns)

            placeholders = ", ".join(["%s"] * len(columns))

            query = f"""
            INSERT INTO {table_name}
            ({column_sql})
            VALUES ({placeholders})
            """

            if conflict_columns:

                conflict_sql = ", ".join(conflict_columns)

                query += f"""
                ON CONFLICT ({conflict_sql})
                DO NOTHING
                """

            rows = [
                tuple(row)
                for row in df.itertuples(index=False, name=None)
            ]

            cursor.executemany(query, rows)

            inserted_rows = cursor.rowcount

            conn.commit()

            return inserted_rows

        except Exception:

            conn.rollback()
            raise

        finally:

            cursor.close()
            conn.close()