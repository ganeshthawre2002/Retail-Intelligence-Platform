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
# Database Manager
# ==========================================================

class DatabaseManager:
    """
    Handles all database operations.
    """

    def execute(self, query: str, params=None) -> None:
        """
        Execute INSERT, UPDATE, DELETE, CREATE queries.
        """

        conn = get_connection()
        cursor = conn.cursor()

        try:

            cursor.execute(query, params)

            conn.commit()

        except Exception as e:

            conn.rollback()

            raise e

        finally:

            cursor.close()
            conn.close()

    def fetch_one(self, query: str, params=None):
        """
        Return a single row.
        """

        conn = get_connection()
        cursor = conn.cursor()

        try:

            cursor.execute(query, params)

            return cursor.fetchone()

        finally:

            cursor.close()
            conn.close()

    def fetch_all(self, query: str, params=None):
        """
        Return all rows.
        """

        conn = get_connection()
        cursor = conn.cursor()

        try:

            cursor.execute(query, params)

            return cursor.fetchall()

        finally:

            cursor.close()
            conn.close()