# Job Market Analyzer

A Python automation tool that collects job market data, analyzes hiring trends, and generates structured Excel reports.

The tool fetches remote job listings from an online API, processes the dataset using **pandas**, and generates a formatted Excel report with summaries and charts.

This project demonstrates **API data collection, data analysis, and automated reporting using Python**.

---

## Features

* Fetch job listings from an online API
* Extract structured job data
* Save results to CSV
* Analyze top companies hiring
* Analyze top job locations
* Analyze top skills/tags
* Generate salary summary statistics
* Export a formatted Excel report
* Create automatic charts in Excel
* Support command-line arguments for job limits

---

## Extracted Data

The scraper collects the following fields:

```
job_title
company
location
salary_min
salary_max
tags
job_url
date_posted
```

---

## Example Output Files

The project generates the following files:

```
output/jobs.csv
output/jobs_report.xlsx
```

The Excel report contains multiple sheets:

```
All Jobs
Overview
Top Companies
Top Locations
Top Skills
Salary Summary
```

The report also includes charts such as:

* Top Companies by Job Count
* Top Skills by Job Demand

---

## Project Structure

```
job-market-analyzer
│
├── output/
│   ├── jobs.csv
│   └── jobs_report.xlsx
│
├── scraper.py
├── analyzer.py
├── excel_report.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Installation

Clone the repository:

```
git clone https://github.com/kanatKZ001/job-market-analyzer.git
cd job-market-analyzer
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## Usage

### Fetch job listings

```
python scraper.py
```

Limit the number of jobs collected:

```
python scraper.py --limit 30
```

---

### Analyze the dataset in the terminal

```
python analyzer.py
```

This prints summaries such as:

* top companies
* top locations
* most common job skills
* salary statistics

---

### Generate the Excel report

```
python excel_report.py
```

The report will be saved as:

```
output/jobs_report.xlsx
```

---

## Technologies Used

* Python
* requests
* pandas
* openpyxl
* argparse

---

## Learning Goals

This project demonstrates practical skills in:

* API data collection
* JSON data processing
* data cleaning and transformation
* job market analysis
* automation pipelines
* Excel report generation
* CLI tool development

---

## Possible Improvements

Future enhancements could include:

* salary cleaning and currency normalization
* filtering by job category
* trend analysis over time
* interactive dashboards
* scheduled report generation
* database storage
* automatic email reports

---

## Author

Kanat Zhumatov

Computer Science student interested in **Python automation, data analysis, and building practical developer tools**.
