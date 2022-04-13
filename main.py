import os
from export_credentials import ExportCredentials
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

export_cred = ExportCredentials().setup_environment()

LINKEDIN_USERNAME = os.environ.get('LINKEDIN_USERNAME')
LINKEDIN_PASSWORD = os.environ.get('LINKEDIN_PASSWORD')

chrome_driver_path = "/Users/william/Developer/Python/chromedriver"
s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)

url = "https://www.linkedin.com/jobs/search/?f_AL=true&geoId=107161656&keywords=ios&location=Oxfordshire%2C%20England%2C%20United%20Kingdom"

driver.get(url)

time.sleep(5)

sign_in = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in.click()

time.sleep(5)

username = driver.find_element(By.ID, "username")
username.send_keys(LINKEDIN_USERNAME)

password = driver.find_element(By.ID, "password")
password.send_keys(LINKEDIN_PASSWORD)

# This didn't work for me so, I opted to click on the Sign In button below
# password.send_keys(Keys.ENTER)

login = driver.find_element(By.CLASS_NAME, "login__form_action_container")
login.click()



# driver.quit()
