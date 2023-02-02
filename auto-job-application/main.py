from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

ACCOUNT_EMAIL = "basharu83@gmail.com"
ACCOUNT_PASSWORD = "Oracle_1"
PHONE = "08038272560"

chrome_driver_path = "C:\\Users\\Public\\anaconda\\chromedriver_win32\\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)
driver.get("https://www.linkedin.com/jobs/search?keywords=PHP%20developer&location=Abuja%2C%20Federal%20Capital%20Territory%2C%20Nigeria&geoId=101711968&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0")

time.sleep(2)
sign_in_button = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in_button.click()

time.sleep(5)

email_field = driver.find_element(By.ID, "username")
email_field.send_keys(ACCOUNT_EMAIL)
password_field = driver.find_element(By.ID, "password")
password_field.send_keys(ACCOUNT_PASSWORD)
password_field.send_keys(Keys.ENTER)

time.sleep(5)

all_listings = driver.find_elements(
    By.CSS_SELECTOR, ".job-card-container--clickable")

for listing in all_listings:
    print("called")
    listing.click()
    time.sleep(2)
    try:

        apply_button = driver.find_element(
            By.CSS_SELECTOR, ".jobs-s-apply button")
        apply_button.click()

        time.sleep(5)

        phone = driver.find_element(
            By.CLASS_NAME, "fb-single-line-text__input")
        if phone.text == "":
            phone.send_keys(PHONE)

        submit_button = driver.find_element(By.CSS_SELECTOR, "footer button")
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
            close_button = driver.find_element(
                By.CLASS_NAME, "artdeco-modal__dismiss")
            close_button.click()

            time.sleep(2)

            discard_button = driver.find_elements(
                By.CLASS_NAME, "artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("Complex application, skipped.")
            continue
        else:
            submit_button.click()

        time.sleep(2)

        close_button = driver.find_element(
            By.CLASS_NAME, "artdeco-modal__dismiss")
        close_button.click()

    except NoSuchElementException:
        print("No application button, skipped.")
        continue

time.sleep(5)
driver.quit()
