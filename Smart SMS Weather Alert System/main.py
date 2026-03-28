import requests
from twilio.rest import Client
from config import *

def get_weather():
    url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={WEATHER_API_KEY}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        temp_kelvin = data["main"]["temp"]
        temp_celsius = temp_kelvin - 273.15

        return round(temp_celsius, 2)

    except Exception as e:
        print("❌ Error fetching weather:", e)
        return None


def send_sms(message_text):
    try:
        client = Client(ACCOUNT_SID, AUTH_TOKEN)

        message = client.messages.create(
            body=message_text,
            from_=TWILIO_NUMBER,   
            to=MY_PHONE            
        )

        print("✅ SMS sent successfully!")
        print("SID:", message.sid)

    except Exception as e:
        print("❌ Error sending SMS:", e)


def main():
    temp = get_weather()

    if temp is None:
        return

    print(f"🌡️ Current temperature in {CITY}: {temp}°C")

    if temp > TEMP_THRESHOLD:
        message = f"🔥 ALERT! Temperature is {temp}°C in {CITY}"
        send_sms(message)
    else:
        print("✅ Temperature is normal. No alert sent.")


if __name__ == "__main__":
    main()