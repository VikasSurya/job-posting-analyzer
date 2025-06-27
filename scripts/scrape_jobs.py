import requests
from bs4 import BeautifulSoup
import pandas as pd

all_jobs = []

for page in range(1, 11):
    print(f"🔄 Scraping page {page}...")
    url = f"https://remoteok.com/remote-dev-jobs?page={page}"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    jobs = soup.find_all("tr", class_="job")

    for job in jobs:
        try:
            title = job.find("h2", {"itemprop": "title"}).text.strip()
            company = job.find("h3", {"itemprop": "name"}).text.strip()
            date_posted = job.find("time")["datetime"].strip()
            tags = job.find_all("div", class_="tag")
            skills = ", ".join(tag.text.strip() for tag in tags) if tags else ""

            all_jobs.append({
                "title": title,
                "company": company,
                "skills": skills,
                "date_posted": date_posted
            })
        except Exception as e:
            print("⚠️ Skipping job due to error:", e)

df = pd.DataFrame(all_jobs)
df.to_csv("../data/raw_jobs_data.csv", index=False)
print("✅ Scraped", len(df), "jobs across 10 pages!")
print("📁 Saved to: data/raw_jobs_data.csv")
