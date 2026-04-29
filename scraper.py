import os
import time
import argparse
import requests
import pandas as pd

API_URL = "https://remoteok.com/api"
OUTPUT_DIR = "output"
OUTPUT_CSV = os.path.join(OUTPUT_DIR, "jobs.csv")

HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json"
}


def parse_arguments():
    parser = argparse.ArgumentParser(description="Job Market Analyzer Scraper")
    parser.add_argument(
        "--limit",
        type=int,
        default=50,
        help="Maximum number of jobs to save"
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=1.0,
        help="Delay before request"
    )
    return parser.parse_args()


def fetch_jobs(api_url: str) -> list[dict]:
    response = requests.get(api_url, headers=HEADERS, timeout=20)
    response.raise_for_status()
    data = response.json()

    # RemoteOK API usually returns metadata first, then jobs
    if isinstance(data, list):
        return data[1:]
    return []


def normalize_job(job: dict) -> dict:
    tags = job.get("tags", [])
    if isinstance(tags, list):
        tags_str = ", ".join(tags)
    else:
        tags_str = ""

    salary_min = job.get("salary_min")
    salary_max = job.get("salary_max")

    return {
        "job_title": job.get("position") or job.get("title"),
        "company": job.get("company"),
        "location": job.get("location"),
        "salary_min": salary_min,
        "salary_max": salary_max,
        "tags": tags_str,
        "job_url": job.get("url"),
        "date_posted": job.get("date")
    }


def save_to_csv(records: list[dict], output_path: str) -> None:
    df = pd.DataFrame(records)
    df.to_csv(output_path, index=False, encoding="utf-8-sig")
    print(f"Saved {len(df)} records to {output_path}")


def main():
    args = parse_arguments()
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    time.sleep(args.delay)

    try:
        raw_jobs = fetch_jobs(API_URL)
        jobs = [normalize_job(job) for job in raw_jobs[:args.limit]]

        if not jobs:
            print("No jobs were fetched.")
            return

        save_to_csv(jobs, OUTPUT_CSV)

    except requests.RequestException as error:
        print(f"Request error: {error}")


if __name__ == "__main__":
    main()