from bs4 import BeautifulSoup
import requests

url = "https://realpython.github.io/fake-jobs/"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Extract job titles using list comprehension
job_titles = [job.get_text(strip=True) for job in soup.find_all("h2", class_="title")]
print(job_titles)
