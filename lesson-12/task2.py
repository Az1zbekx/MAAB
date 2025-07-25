import requests
from bs4 import BeautifulSoup
import sqlite3
import csv


URL = 'https://realpython.github.io/fake-jobs'


conn = sqlite3.connect('jobs.db')
cursor = conn.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS jobs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    company TEXT,
    location TEXT,
    description TEXT,
    apply_link TEXT,
    UNIQUE(title, company, location)
)
''')


response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')
job_elements = soup.find_all('div', class_='card-content')

new_jobs = 0
updated_jobs = 0

for job_elem in job_elements:
    title = job_elem.find('h2', class_='title').text.strip()
    company = job_elem.find('h3', class_='company').text.strip()
    location = job_elem.find('p', class_='location').text.strip()
    description = job_elem.find('div', class_='content').text.strip()
    apply_link = job_elem.find('a', text='Apply')['href']

    
    cursor.execute('SELECT description, apply_link FROM jobs WHERE title=? AND company=? AND location=?',
                   (title, company, location))
    existing = cursor.fetchone()

    if existing is None:
        
        cursor.execute('INSERT INTO jobs (title, company, location, description, apply_link) VALUES (?, ?, ?, ?, ?)',
                       (title, company, location, description, apply_link))
        new_jobs += 1
    else:
        
        if existing[0] != description or existing[1] != apply_link:
            cursor.execute('''
            UPDATE jobs SET description=?, apply_link=? 
            WHERE title=? AND company=? AND location=?
            ''', (description, apply_link, title, company, location))
            updated_jobs += 1

conn.commit()
print(f"New jobs added: {new_jobs}")
print(f"Jobs updated: {updated_jobs}")


def filter_jobs(company=None, location=None):
    query = "SELECT title, company, location, description, apply_link FROM jobs WHERE 1=1"
    params = []

    if company:
        query += " AND company LIKE ?"
        params.append(f"%{company}%")
    if location:
        query += " AND location LIKE ?"
        params.append(f"%{location}%")

    cursor.execute(query, params)
    return cursor.fetchall()


def export_to_csv(jobs, filename='filtered_jobs.csv'):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Job Title', 'Company', 'Location', 'Description', 'Application Link'])
        writer.writerows(jobs)
    print(f"Exported to {filename}")


filtered = filter_jobs(location="Remote")  
export_to_csv(filtered)

conn.close()
