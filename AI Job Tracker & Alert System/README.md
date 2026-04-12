# 💼 AI Job Tracker & Alert System

A modern web application for tracking and managing AI/Python job opportunities with automated scraping and email alerts.

## Features

✨ **Modern Dashboard** - Beautiful, responsive UI for job management  
🔍 **Job Scraping** - Automatically fetch job listings from various sources  
📧 **Email Alerts** - Receive notifications for new job postings  
📊 **Job Database** - SQLite-based permanent job storage  
🎨 **Professional Design** - Modern gradient UI with smooth animations  

## Project Structure

```
├── app.py              # Flask application entry point
├── config.py           # Configuration and environment variables
├── database.py         # SQLite database operations
├── scraper.py          # Job scraping logic
├── requirements.txt    # Python dependencies
├── .env               # Environment variables (keep secret!)
├── static/
│   └── style.css      # Modern CSS styling
└── templates/
    └── dashboard.html  # Dashboard UI template
```

## Installation

### 1. Clone the repository
```bash
git clone <repository-url>
cd "AI Job Tracker & Alert System"
```

### 2. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure environment variables
Create a `.env` file in the project root:
```
FLASK_ENV=development
EMAIL=your_email@gmail.com
PASSWORD=your_app_password
RECEIVER_EMAIL=recipient@gmail.com
DATABASE_URL=jobs.db
```

**⚠️ Security Note:** Never commit `.env` to version control. It's already in `.gitignore`.

## Usage

### Run the web dashboard
```bash
python app.py
```
Visit `http://localhost:5000` in your browser.

### Scrape job listings
```bash
python scraper.py
```

### Database operations
```python
from database import get_jobs, insert_job, create_table

# Get all jobs
jobs = get_jobs()

# Insert a new job
insert_job("Python Developer", "Tech Corp")
```

## Configuration

Edit `config.py` to customize:
- **KEYWORDS** - Job search keywords
- **EMAIL_CONFIG** - Email settings (from `.env`)
- **DATABASE_URL** - Database file location
- **FLASK_ENV** - Development or production mode

## Security Best Practices

✅ Never commit `.env` file  
✅ Use environment variables for secrets  
✅ Rotate email app passwords regularly  
✅ Keep dependencies updated  
✅ Validate all user inputs  

## Technologies Used

- **Backend:** Flask (Python web framework)
- **Database:** SQLite
- **Frontend:** HTML5, CSS3, Font Awesome icons
- **Task:** Job scraping and notifications

## Requirements

- Python 3.8+
- Flask
- Beautiful Soup 4
- python-dotenv
- Requests

## Future Enhancements

🔄 Real-time job alerts  
🔎 Advanced filtering and search  
📱 Mobile responsive improvements  
🔐 User authentication  
💾 PostgreSQL database support  

## License

Developed by Mamid for portfolio purposes.

## Support

For issues or questions, please check the configuration and ensure all environment variables are set correctly.
