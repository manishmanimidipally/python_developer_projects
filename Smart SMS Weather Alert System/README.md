# 📲 Smart SMS Weather Alert System

## 🚀 Overview

Smart SMS Weather Alert System is a Python-based automation project that monitors real-time weather conditions and sends SMS alerts using Twilio when predefined thresholds are exceeded.

This project demonstrates real-world integration of external APIs, automation logic, and notification systems.

---

## ✨ Features

* 🌦️ Fetch real-time weather data using API
* 🔔 Send SMS alerts using Twilio
* ⚙️ Configurable temperature threshold
* 🔐 Secure API key management using `.env`
* ⏱️ Can be automated using scheduler (cron / task scheduler)

---

## 🛠️ Tech Stack

* **Language:** Python
* **SMS Service:** Twilio
* **Weather API:** OpenWeather
* **Libraries:** requests, python-dotenv, twilio

---

## 📁 Project Structure

```id="d0t3lm"
Smart SMS Weather Alert System/
│
├── main.py
├── config.py
├── .env
└── requirements.txt
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```id="yq8c2m"
git clone https://github.com/manishmanimidipally/python_developer_projects.git
cd python_developer_projects/Smart\ SMS\ Weather\ Alert\ System
```

---

### 2️⃣ Install Dependencies

```id="g4h3n1"
pip install -r requirements.txt
```

---

### 3️⃣ Setup Environment Variables

Create `.env` file:

```env id="c0g2o9"
ACCOUNT_SID=your_twilio_sid
AUTH_TOKEN=your_auth_token
TWILIO_NUMBER=+1xxxxxxxxxx
MY_PHONE=+91xxxxxxxxxx
WEATHER_API_KEY=your_api_key
```

---

### 4️⃣ Run Application

```id="r8t1v2"
python main.py
```

---

## 🧪 Example Output

```id="c2f8w1"
🌡️ Current temperature in Hyderabad: 36°C
✅ SMS sent successfully!
```

📱 SMS:

```id="k1v9u0"
🔥 ALERT! Temperature is 36°C in Hyderabad
```

---

## 🧠 How It Works

1. Fetch weather data from API
2. Convert temperature from Kelvin to Celsius
3. Compare with threshold value
4. Trigger SMS using Twilio

---

## 🔐 Important Notes

* Twilio trial accounts require verified phone numbers
* API keys should not be shared publicly
* Internet connection is required

---

## 🎯 Use Cases

* 🌦️ Weather alerts
* 📈 Stock alerts (can be extended)
* 🚨 System monitoring
* 🔔 Notification automation

---

## 🧠 Key Learnings

* API integration using Python
* Automation with conditional logic
* SMS notification systems
* Secure environment variable handling

---

## 📌 Resume Highlight

Developed an automated SMS alert system using Python by integrating weather APIs and Twilio services to send real-time notifications based on predefined conditions.

---

## 🚀 Future Enhancements

* 🌐 Build Flask web dashboard
* 📊 Add analytics (charts)
* 📧 Add email notifications
* 🤖 AI-based alert system

---

## 🙌 Acknowledgement

Inspired by real-world automation systems and API-based notification services.

---

## 📬 Contact

Feel free to connect for feedback or collaboration!
