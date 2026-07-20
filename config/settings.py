from pathlib import Path
from dotenv import load_dotenv
import os


# ==========================================================
# Project Paths
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

ENV_FILE = PROJECT_ROOT / ".env"


# ==========================================================
# Load Environment Variables
# ==========================================================

load_dotenv(ENV_FILE)


# ==========================================================
# Database Configuration
# ==========================================================

DB_HOST = os.getenv("DB_HOST")
DB_PORT = int(os.getenv("DB_PORT", 5432))
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")


# ==========================================================
# Application Configuration
# ==========================================================

APP_ENV = os.getenv("APP_ENV", "development")