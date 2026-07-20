from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_ROOT))

from database.database_manager import DatabaseManager


db = DatabaseManager()

result = db.fetch_one("SELECT version();")

print(result)