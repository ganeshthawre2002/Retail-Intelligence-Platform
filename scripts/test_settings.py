from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_ROOT))

from config.settings import *

print("=" * 50)
print("DATABASE CONFIGURATION")
print("=" * 50)

print(f"Host        : {DB_HOST}")
print(f"Port        : {DB_PORT}")
print(f"Database    : {DB_NAME}")
print(f"Username    : {DB_USER}")
print(f"Password    : {'*' * len(DB_PASSWORD)}")
print(f"Environment : {APP_ENV}")