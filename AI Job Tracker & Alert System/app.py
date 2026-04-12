from flask import Flask, render_template
from database import get_jobs
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['ENV'] = os.getenv('FLASK_ENV', 'development')
app.config['DEBUG'] = app.config['ENV'] == 'development'

@app.route("/")
def dashboard():
    try:
        jobs = get_jobs()
        return render_template("dashboard.html", jobs=jobs)
    except Exception as e:
        print(f"Error fetching jobs: {e}")
        return render_template("dashboard.html", jobs=[], error="Failed to load jobs")

if __name__ == "__main__":
    app.run(debug=app.config['DEBUG'])