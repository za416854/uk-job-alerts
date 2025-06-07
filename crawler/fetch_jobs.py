import requests
from bs4 import BeautifulSoup
from save_to_mongo import save_jobs

def fetch_jobs(keyword="software engineer", location="london"):
    url = f"https://www.reed.co.uk/jobs/{keyword.replace(' ', '-')}-jobs-in-{location.replace(' ', '-')}"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    res = requests.get(url, headers=headers)
    if res.status_code != 200:
        print(f"Failed to fetch page. Status: {res.status_code}")
        return []

    soup = BeautifulSoup(res.text, "html.parser")
    jobs = []

    for job_card in soup.select(".job-result"):
        title = job_card.select_one(".job-result-heading__title")
        company = job_card.select_one(".gtmJobListingPostedBy")
        location = job_card.select_one(".job-metadata__item--location")
        link = job_card.select_one("a.job-result-card")

        if title and link:
            jobs.append({
                "title": title.text.strip(),
                "company": company.text.strip() if company else "",
                "location": location.text.strip() if location else "",
                "url": "https://www.reed.co.uk" + link["href"]
            })

    return jobs

if __name__ == "__main__":
    result = fetch_jobs()
    if result:
        save_jobs(result)