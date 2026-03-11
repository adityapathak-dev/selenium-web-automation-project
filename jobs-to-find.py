from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
url = "https://www.indeed.com"
driver.get(url)
job = driver.find_element(By.NAME, "q")
job.send_keys("data scientist")
job.send_keys(Keys.RETURN)
time.sleep(4)
jobs = driver.find_elements(By.CSS_SELECTOR, ".css-1ac2h1w.eu4oa1w0")
data = []
data.append("title,company,location")
for j in jobs:
    title = j.find_element(By.TAG_NAME, "h2").text
    company = j.find_element(By.CLASS_NAME, "companyName").text
    location = j.find_element(By.CLASS_NAME, "companyLocation").text
    data.append(f'"{title}","{company}","{location}"')
with open("jobs.csv","w",encoding="utf-8") as f:
    f.write("\n".join(data))
driver.quit()