import requests
from bs4 import BeautifulSoup
from crawler.save_to_mongo import save_jobs
from notifier.telegram_bot import send_telegram_message
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env'))
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def fetch_jobs(keyword=".net engineer", location="london"):
    url = f"https://www.reed.co.uk/jobs/{keyword.replace(' ', '-')}-jobs-in-{location.replace(' ', '-')}"
    headers = {"User-Agent": "Mozilla/5.0"}

    res = requests.get(url, headers=headers)
    if res.status_code != 200:
        print(f"Failed to fetch page. Status: {res.status_code}")
        return []

    soup = BeautifulSoup(res.text, "html.parser")
    jobs = []

    for job_card in soup.find_all("article", class_="card"):
        title_el = job_card.select_one("h2 a")
        company_el = job_card.select_one("a.gtmJobListingPostedBy")
        location_el = None
        for li in job_card.select("li"):
            if "location" in li.get("aria-labelledby", "") or "location" in li.text.lower():
                location_el = li
                break

        if title_el:
            jobs.append({
                "title": title_el.text.strip(),
                "company": company_el.text.strip() if company_el else "",
                "location": location_el.text.strip() if location_el else "",
                "url": "https://www.reed.co.uk" + title_el["href"]
            })


    return jobs


if __name__ == "__main__":
    result = fetch_jobs()
    if result:
        save_jobs(result)
        send_telegram_message(BOT_TOKEN, CHAT_ID, result)
    else:
        print("jobs is empty, plz try again!")
