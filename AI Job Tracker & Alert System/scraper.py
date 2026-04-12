from database import insert_job, create_table

def scrape_jobs():
    print("🔍 Adding sample jobs...")

    create_table()

    jobs = [
        ("Python Developer", "Google"),
        ("Backend Engineer (Python)", "Amazon"),
        ("Django Developer", "Infosys"),
        ("Flask Developer", "TCS"),
        ("Software Engineer - Python", "Microsoft"),
        ("Junior Python Developer", "Wipro"),
        ("Data Analyst (Python)", "Accenture"),
        ("AI/ML Engineer", "OpenAI"),
        ("Automation Engineer (Python)", "Capgemini"),
        ("Full Stack Developer", "Zoho"),
    ]

    count = 0

    for title, company in jobs:
        insert_job(title, company)
        print(f"✔ {title} - {company}")
        count += 1

    print(f"✅ Total jobs added: {count}")


if __name__ == "__main__":
    scrape_jobs()