
# UK Job Alerts

This side project is a job monitoring system built to automatically fetch software engineering job listings from Reed.co.uk and send Telegram notifications for new job posts. It is designed to be lightweight, cloud-deployable, and suitable for daily job search automation.

---

## 🔍 Features

- Python crawler that scrapes job postings from reed.co.uk (e.g., software engineer in the UK)
- Filters out duplicates by checking MongoDB URL records
- Automatically stores job data in MongoDB Atlas
- Sends job updates via Telegram bot to a specified chat group
- Supports GitLab CI/CD for automated daily execution (cron schedule)
- Fully containerized with Docker and Railway deployment
- Simple Prometheus-compatible metrics available via `/metrics`

---

## 🏗️ Architecture Overview

```
[User Schedule] → GitLab CI → Python Crawler
                                ↓
                       Check existing MongoDB
                                ↓
                    ┌──── Duplicate ────┐
                    ↓                  ↓
             (Skip insert)       Insert New
                                        ↓
                                Send to Telegram
```

---

## ⚙️ Tech Stack

- **Python**: Web scraping + notification
- **Go**: REST API to query jobs stored in MongoDB
- **MongoDB Atlas**: Store job listings
- **GitLab CI**: Automate scheduled jobs
- **Line Notify**: Push daily alerts


---

## 📦 Folder Structure

```
uk-job-alerts/
├── crawler/
│   └── fetch_jobs.py       # Main crawler logic
├── notifier/
│   └── send_alert.py       # Telegram notifier logic
├── .gitlab-ci.yml          # CI pipeline
├── requirements.txt        # Dependencies
└── README.md
```

---

## 🛠️ Setup

```bash
# Create virtual environment
python -m venv venv

# Activate it
venv\Scripts\activate  (Windows)
source venv/bin/activate  (Linux/macOS)

# Install dependencies
pip install requests beautifulsoup4
# or for replit
pip install --no-user requests beautifulsoup4

pip install "pymongo[srv]"
# or
pip install --no-user "pymongo[srv]"  # for replit

pip install python-dotenv

# Export installed packages
pip freeze > requirements.txt

# Run the crawler
python -m crawler.fetch_jobs
```

2. **Run manually** 
```bash
# Install Go from https://go.dev/dl/
go version  # verify installation

# Init the project
go mod init uk-job-alerts

# Install required libraries
go get github.com/joho/godotenv
go get github.com/gofiber/fiber/v2
go get go.mongodb.org/mongo-driver/mongo

go mod tidy

# Run the API
go run api/main.go
```

** Open `launch.json` (Ctrl + Shift + D) and update:** 
```json
"configurations": [
    {
        "name": "Python: fetch_jobs (by module)",
        "type": "debugpy",
        "request": "launch",
        "module": "crawler.fetch_jobs",
        "console": "integratedTerminal",
        "cwd": "${workspaceFolder}"
    }
]
```

## Project Structure
- `crawler/fetch_jobs.py`: Job scraping logic
- `notifier/line_notify.py`: Push notification handler
- `.gitlab-ci.yml`: CI/CD pipeline config


## 📬 Telegram Output Example

> `📌 Senior Python Developer`
> `🏢 Company: XYZ Recruitment`
> `📍 Location: Remote`
> [Apply Link](https://www.reed.co.uk/jobs/senior-python-developer/xxxxxxx)

---

## ✅ Motivation

I built this project to automate job hunting in the UK tech market and explore integration between Python automation, CI/CD, and Telegram notifications. Ideal for personal use and learning DevOps workflow.

---
 
