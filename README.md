# Job Posting Analyzer

A complete Data Engineering project built using Python and MySQL that automates the extraction, transformation, and loading (ETL) of job listings from RemoteOK. The pipeline scrapes real-time job postings, processes them into a structured format, and loads them into a MySQL database for further analysis and visualization.

## Tech Stack

- Python – Scripting & automation
- Requests + BeautifulSoup – Web scraping
- Pandas – Data cleaning & transformation
- MySQL – Data storage and querying
- CSV – Intermediate file storage

## Project Structure

job-posting-analyzer/
├── data/
│   ├── raw_jobs_data.csv         
│   └── cleaned_jobs_data.csv     
├── scripts/
│   ├── scrape_jobs.py            
│   ├── clean_data.py             
│   └── load_to_mysql.py          
└── README.md                     

## Features

- Scrapes job titles, companies, skill tags, and posting dates
- Cleans and standardizes job data using pandas
- Loads structured data into a MySQL database table
- Modular design for scalable ETL pipelines
- Easily extendable for dashboards and analytics tools

## Workflow Overview

1. scrape_jobs.py
   - Scrapes job listings from the first 10 pages of RemoteOK.
   - Extracts: Job Title, Company, Skills, Date Posted.
   - Stores data in data/raw_jobs_data.csv.

2. clean_data.py
   - Filters out incomplete or irrelevant records.
   - Normalizes text fields.
   - Saves the cleaned output to data/cleaned_jobs_data.csv.

3. load_to_mysql.py
   - Connects to a MySQL database (job_analyzer).
   - Creates table jobs (if not exists).
   - Inserts cleaned job listings into the table.

## Sample Output (in MySQL)

| Title                   | Company         | Skills                          | Date Posted              |
|------------------------|-----------------|----------------------------------|---------------------------|
| Lead Data Engineer      | Open Architects | Python, DevOps, DataOps          | 2025-06-02T22:32:54+00:00 |
| Data Warehouse Engineer | Plutus          | Backend, Front End               | 2024-10-11T00:00:04+00:00 |
| Data Engineer           | Paperpile       | Node.js, JavaScript, TypeScript  | 2023-05-09T05:46:36+00:00 |

## Setup Instructions

1. Clone the Repository

git clone https://github.com/VikasSurya/job-posting-analyzer.git
cd job-posting-analyzer

2. Install Required Packages

pip install requests beautifulsoup4 pandas mysql-connector-python

3. Create MySQL Database and Table

Login to MySQL and run:

CREATE DATABASE job_analyzer;

USE job_analyzer;

CREATE TABLE jobs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    company VARCHAR(255),
    skills TEXT,
    date_posted VARCHAR(50)
);

4. Run the Scripts

python scripts/scrape_jobs.py
python scripts/clean_data.py
python scripts/load_to_mysql.py

## Use Cases

- Skill demand trend analysis
- Keyword-based job search
- Data pipeline building for dashboards
- Testing automation in ETL development

## Future Improvements

- Search & filter features for job keywords
- Interactive dashboard using Power BI or Tableau
- Scheduled jobs using cron or Airflow
- Cloud integration with AWS RDS or GCP SQL

## Author

Vikas Surya  
GitHub: https://github.com/VikasSurya  
LinkedIn: https://www.linkedin.com/in/vikassurya

