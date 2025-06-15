```markdown
# UK Job Alert Bot (Line Notify + Python + MongoDB + GitLab CI)

Automatically scrapes UK job listings from [Reed.co.uk](https://www.reed.co.uk) every day, filters them, and sends push notifications to Line.

## 🛠 Tech Stack
- **Python**: Web scraping + sending notifications
- **Go**: Provides a REST API to browse MongoDB job data
- **MongoDB Atlas**: Stores job listing data
- **GitLab CI**: Scheduled daily job execution
- **Line Notify**: Push notification delivery

---

## 🚀 Getting Started

### 1. Python Setup
```bash
# Set up a virtual environment
python -m venv venv
source venv/bin/activate      # Linux/macOS
# or
venv\Scripts\activate         # Windows

# Install dependencies
pip install requests beautifulsoup4 pymongo python-dotenv
# For replit users
pip install --no-user requests beautifulsoup4 "pymongo[srv]" python-dotenv

# Freeze requirements (optional)
pip freeze > requirements.txt
```

### 2. Run the Crawler
```bash
python -m crawler.fetch_jobs
```

---

### 3. Go API Setup
```bash
# Install Go if not already installed: https://go.dev/dl/
go version     # verify installation

# Inside the /api directory
cd api
go mod init uk-job-alerts
go get github.com/gofiber/fiber/v2
```

---

## 🐞 Debug Mode
To debug in VS Code, press `Ctrl + Shift + D`, open `launch.json`, and use the following configuration:
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

---

## 📦 Project Structure
```
uk-job-alerts/
├── crawler/
│   └── fetch_jobs.py        # Scrapes job listings
├── notifier/
│   └── line_notify.py       # Sends Line Notify message
├── api/                     # Go-based REST API
├── .env                     # LINE_NOTIFY_TOKEN goes here
├── .gitlab-ci.yml           # GitLab CI schedule definition
```

---

## ✅ How to Use
1. Create a `.env` file and insert your `LINE_NOTIFY_TOKEN`.
2. Configure a GitLab CI schedule (e.g. daily at 9AM UK time).
3. Receive daily updates of UK tech jobs via Line!

---
```

---
