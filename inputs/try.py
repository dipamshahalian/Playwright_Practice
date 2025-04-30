import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Load credentials from environment variables
EMAIL = os.getenv("EMAIL", "your_email_here")
PASSWORD = os.getenv("PASSWORD", "your_password_here")

if not EMAIL or not PASSWORD:
    raise ValueError("Please set EMAIL and PASSWORD environment variables.")

# Set up Chrome options
opt = Options()
opt.add_argument("--disable-blink-features=AutomationControlled")

# Set up WebDriver
serv = Service(r"C:\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=serv, options=opt)
driver.implicitly_wait(10)

try:
    # Open the target website
    driver.get("https://accounts.google.com/v3/signin/identifier?service=mail")
    driver.maximize_window()

    # Enter Email and Click 'Next'
    email_tb = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='identifierId']"))
    )
    email_tb.send_keys(EMAIL)
    driver.find_element(By.XPATH, "//span[normalize-space()='Next']").click()

    # Enter Password and Click 'Next'
    pwd_tb = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@name='Passwd']"))
    )
    pwd_tb.send_keys(PASSWORD)
    driver.find_element(By.XPATH, "//span[normalize-space()='Next']").click()

    print("Email Login Passed")

    # Search for specific email
    search = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search mail']"))
    )
    search.send_keys("Alian Hub have sent you an invitation")
    search.send_keys(Keys.RETURN)

    # Wait for the first email and click it
    mail = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//table//tr[1]//span/span/span[1]"))
    )
    mail.click()

    # Click the link in the email
    e_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Click here to Join']"))
    )
    e_link.click()

    # Switch to the new tab
    driver.switch_to.window(driver.window_handles[-1])

    # Login process
    log_email = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='email']"))
    )
    log_email.send_keys("riap1330+104@gmail.com")

    log_pwd = driver.find_element(By.XPATH, "//input[@id='password']")
    log_pwd.send_keys("Abc@223133")

    log_btn = driver.find_element(By.XPATH, "//button[normalize-space()='Login']")
    log_btn.click()

    print("Test Case Passed!")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Ensure the browser is closed
    driver.quit()