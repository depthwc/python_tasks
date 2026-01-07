import requests
from bs4 import BeautifulSoup
import sqlite3
import csv

DB = 'jobs.db'

# Initialize DB and table
conn = sqlite3.connect(DB)
cur = conn.cursor()
cur.execute('''
    CREATE TABLE IF NOT EXISTS jobs (
        id INTEGER PRIMARY KEY,
        title TEXT,
        company TEXT,
        location TEXT,
        description TEXT,
        apply_link TEXT,
        UNIQUE(title, company, location)
    )
''')
conn.commit()

# Scrape jobs from website
url = 'https://realpython.github.io/fake-jobs/'
resp = requests.get(url)
resp.raise_for_status()
soup = BeautifulSoup(resp.text, 'html.parser')

jobs = []
for card in soup.select('.card-content'):
    title = card.find('h2', class_='title').get_text(strip=True)
    company = card.find('h3', class_='company').get_text(strip=True)
    location = card.find('p', class_='location').get_text(strip=True)
    
    desc_tag = card.find('p', class_='description')
    description = desc_tag.get_text(strip=True) if desc_tag else ''
    
    apply_link = card.find('a', string='Apply')['href']
    jobs.append((title, company, location, description, apply_link))

# Insert or update jobs in DB
for title, company, location, description, apply_link in jobs:
    cur.execute('SELECT id, description, apply_link FROM jobs WHERE title=? AND company=? AND location=?',
                (title, company, location))
    row = cur.fetchone()

    if row is None:
        cur.execute('INSERT INTO jobs (title, company, location, description, apply_link) VALUES (?, ?, ?, ?, ?)',
                    (title, company, location, description, apply_link))
        print(f"Inserted: {title} — {company} ({location})")
    else:
        job_id, old_description, old_apply_link = row
        if description != old_description or apply_link != old_apply_link:
            cur.execute('UPDATE jobs SET description=?, apply_link=? WHERE id=?',
                        (description, apply_link, job_id))
            print(f"Updated: {title} — {company} ({location})")

conn.commit()

# Filter jobs by company and location
company_filter = 'Python'  # change or set to None
location_filter = 'New York'  # change or set to None

query = 'SELECT title, company, location, apply_link FROM jobs WHERE 1=1'
params = []

if company_filter:
    query += ' AND company LIKE ?'
    params.append(f'%{company_filter}%')
if location_filter:
    query += ' AND location LIKE ?'
    params.append(f'%{location_filter}%')

cur.execute(query, params)
filtered_jobs = cur.fetchall()

# Export filtered results to CSV
filename = 'filtered_jobs.csv'
with open(filename, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Title', 'Company', 'Location', 'Apply Link'])
    writer.writerows(filtered_jobs)

print(f"Exported {len(filtered_jobs)} filtered jobs to {filename}")

# Close DB connection
conn.close()
