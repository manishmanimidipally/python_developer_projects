import os
from dotenv import load_dotenv

load_dotenv()

ACCOUNT_SID = os.getenv("ACCOUNT_SID")
AUTH_TOKEN = os.getenv("AUTH_TOKEN")
TWILIO_NUMBER = os.getenv("TWILIO_NUMBER")
MY_PHONE = os.getenv("MY_PHONE")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

CITY = "Hyderabad"
TEMP_THRESHOLD = 35