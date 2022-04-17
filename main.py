import os
from export_credentials import ExportCredentials
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

export_cred = ExportCredentials().setup_environment()

LINKEDIN_USERNAME = os.environ.get('LINKEDIN_USERNAME')
LINKEDIN_PASSWORD = os.environ.get('LINKEDIN_PASSWORD')

chrome_driver_path = "/Users/william/Developer/Python/chromedriver"
s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)

wait = WebDriverWait(driver, 30)

# url = "https://www.linkedin.com/jobs/search/?f_AL=true&geoId=107161656&keywords=ios&location=Oxfordshire%2C%20England%2C%20United%20Kingdom"
# url = "https://www.linkedin.com/jobs/search/?currentJobId=3025654523&f_AL=true&f_E=2%2C3&f_WT=2&geoId=102257491&keywords=python&location=London%2C%20England%2C%20United%20Kingdom&sortBy=R"
url = "https://www.linkedin.com/jobs/search/?f_AL=true&geoId=92000000&keywords=ios&location=Worldwide"

driver.get(url)

# sign_in = driver.find_element(By.LINK_TEXT, "Sign in"
sign_in = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Sign in")))
sign_in.click()

# username = driver.find_element(By.ID, "username")
username = wait.until(EC.presence_of_element_located((By.ID, "username")))
username.send_keys(LINKEDIN_USERNAME)

password = driver.find_element(By.ID, "password")
password.send_keys(LINKEDIN_PASSWORD)

login = driver.find_element(By.CLASS_NAME, "login__form_action_container")
login.click()

# Create list of openings
openings = driver.find_elements(By.CSS_SELECTOR, "li.jobs-search-results__list-item")
# openings = driver.find_elements(By.CLASS_NAME, "job-card-container")
print(len(openings))

openings[0].click()
save_button = driver.find_element(By.CLASS_NAME, "jobs-save-button")
print(save_button.text)
save_button.click()

# #ember889 > section > div.jobs-company__box >
# //*[@id="ember889"]/section/div[1]/div[1]/button
# button.msg-overlay-bubble-header__control.msg-overlay-bubble-header__control--new-convo-btn artdeco-button.artdeco-button--circle artdeco-button--muted artdeco-button--1.artdeco-button--tertiary.ember-view

# Minimise message pane
messages_min = driver.find_element(By.CLASS_NAME, "msg-overlay-bubble-header__details")
messages_min.click()

# follow_button = openings[0].get_attribute("aria-label")
# print(follow_button)
# follow_button = driver.find_element(By.CLASS_NAME, "follow")
follow_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "follow")))
# print(follow_button)
follow_button.click()


jobs = []
for opening in openings:
    # job_id = opening.get_attribute("id")
    job_id = opening.get_attribute("data-occludable-job-id")
    # job_id = opening.get_attribute("data-job-id")
    # link = opening.find_element(By.CSS_SELECTOR, f"a#{job_id}")
    jobs.append(job_id)
    # print(job_id, link)
print(jobs)

job_links = []
base_job_url = "https://www.linkedin.com/jobs/view/"
for job in jobs:
    job_url = f"{base_job_url}{job}"
    job_links.append(job_url)

print(job_links)

# job_links = []
# for job_id in jobs:


# Find and Click the "easy apply" button
# easy_apply = driver.find_element(By.CLASS_NAME, "jobs-apply-button")
# easy_apply.click()
#
# time.sleep(3)
# Enter a phone number
# phone = driver.find_element(By.CSS_SELECTOR, "input.ember-text-field.ember-view.fb-single-line-text__input")
# phone.send_keys("1234567890")

# Find and Click the "submit application" button
# submit = driver.find_element(By.CSS_SELECTOR, "button.artdeco-button.artdeco-button--2.artdeco-button--primary ember-view")
# submit.click()

# driver.quit()
