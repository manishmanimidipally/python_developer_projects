import os
from dotenv import load_dotenv

load_dotenv()

# Job search keywords
KEYWORDS = ["python", "ai", "ml", "backend"]

# Email configuration
EMAIL_CONFIG = {
    "sender_email": os.getenv("EMAIL", ""),
    "sender_password": os.getenv("PASSWORD", ""),
    "receiver_email": os.getenv("RECEIVER_EMAIL", ""),
}

# Database configuration
DATABASE_URL = os.getenv("DATABASE_URL", "jobs.db")

# Flask configuration
FLASK_ENV = os.getenv("FLASK_ENV", "development")