from pathlib import Path
import sys

import psycopg2
from psycopg2 import OperationalError

# ==========================================================
# Make Project Root Importable
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_ROOT))

# ==========================================================
# Import Settings
# ==========================================================

from config.settings import (
    DB_HOST,
    DB_PORT,
    DB_NAME,
    DB_USER,
    DB_PASSWORD,
)


# ==========================================================
# Database Connection
# ==========================================================

def get_connection():
    """
    Create and return a PostgreSQL database connection.
    """

    try:

        connection = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
        )

        return connection

    except OperationalError as e:

        print("\nFailed to connect to PostgreSQL.\n")
        raise e


# ==========================================================
# Connection Test
# ==========================================================

if __name__ == "__main__":

    conn = get_connection()

    print("=" * 60)
    print("Successfully Connected to PostgreSQL")
    print("=" * 60)

    conn.close()

    print("Connection Closed Successfully")