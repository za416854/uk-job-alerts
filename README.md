
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

- **Language**: Python 3.10
- **Queue**: None (single batch job)
- **Database**: MongoDB Atlas
- **Deployment**: Railway (Free tier)
- **CI/CD**: GitLab CI with daily cron schedule
- **Notification**: Telegram Bot API
- **Monitoring**: Prometheus metrics exposed

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

1. **Environment Variables (.env)**

```
MONGO_URI=your_mongo_uri
BOT_TOKEN=your_telegram_bot_token
CHAT_ID=your_telegram_chat_id
```

2. **Run manually**

```bash
python -m crawler.fetch_jobs
```

3. **Run via GitLab CI** (auto-daily)

- Go to **CI/CD > Schedules**
- Add a rule like `0 18 * * *` (every 6PM London)
- Pass variables if not masked in project

---

## 📬 Telegram Output Example

> `📌 Senior Python Developer`
> `🏢 Company: XYZ Recruitment`
> `📍 Location: Remote`
> [Apply Link](https://www.reed.co.uk/jobs/senior-python-developer/xxxxxxx)

---

## ✅ Motivation

I built this project to automate job hunting in the UK tech market and explore integration between Python automation, CI/CD, and Telegram notifications. Ideal for personal use and learning DevOps workflow.

---

## 📄 License

MIT License
