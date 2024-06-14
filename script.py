from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd
import time
from dotenv import load_dotenv
import os

load_dotenv()


# LinkedIn credentials
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")

# Initialize WebDriver
driver = webdriver.Chrome(executable_path="/path/to/chromedriver")

# Login to LinkedIn
driver.get("https://www.linkedin.com/login")
time.sleep(2)

# Enter credentials
driver.find_element_by_id("username").send_keys(username)
driver.find_element_by_id("password").send_keys(password)
driver.find_element_by_xpath("//button[@type='submit']").click()
time.sleep(5)


# Function to scrape profile information
def scrape_profile(url):
    driver.get(url)
    time.sleep(5)
    soup = BeautifulSoup(driver.page_source, "html.parser")

    name = (
        soup.find("h1", {"class": "text-heading-xlarge"}).text.strip()
        if soup.find("h1", {"class": "text-heading-xlarge"})
        else None
    )
    job_title = (
        soup.find("div", {"class": "text-body-medium"}).text.strip()
        if soup.find("div", {"class": "text-body-medium"})
        else None
    )
    contact_info_url = soup.find("a", {"data-control-name": "contact_see_more"})

    if contact_info_url:
        driver.get(contact_info_url["href"])
        time.sleep(5)
        contact_soup = BeautifulSoup(driver.page_source, "html.parser")
        email = contact_soup.find(
            "a", {"href": lambda x: x and x.startswith("mailto:")}
        )
        phone = contact_soup.find("span", {"class": "t-14 t-black t-normal"})
        email = email["href"][7:] if email else None
        phone = phone.text.strip() if phone else None
    else:
        email = None
        phone = None

    return {"name": name, "job_title": job_title, "email": email, "phone": phone}


# List of company profile URLs to scrape
company_urls = [
    "https://www.linkedin.com/in/sample-profile-1/",
    "https://www.linkedin.com/in/sample-profile-2/",
    # Add more profiles as needed
]

# Scrape each profile
data = []
for url in company_urls:
    profile_data = scrape_profile(url)
    data.append(profile_data)

# Convert to DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("linkedin_contacts.csv", index=False)

# Close the driver
driver.quit()
