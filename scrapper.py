import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Env variables
CHROME_BIN = os.environ.get("CHROME_BIN", None)
CHROME_DRIVER = os.environ.get("CHROME_DRIVER", None)

# Start driver instance
def start_driver():
    if CHROME_BIN is None:
        return None, "Need to install Google Chrome & its Driver"
    try:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--ignore-certificate-errors")
        chrome_options.add_argument("--test-type")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.binary_location = CHROME_BIN
        driver = webdriver.Chrome(chrome_options=chrome_options)
        return driver, None
    except Exception as err:
        return None, str(err)
    
# Main scraper function
driver, err = start_driver()
if err:
    print(err)
else:
    driver.get("https://qcpi.questcdn.com/cdn/posting/?group=1950787&provider=1950787")
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="table_id"]/tbody/tr[1]/td[2]/a').click()
    time.sleep(1)
    for i in range(1, 6):
        print(f"Data: {i}")
        value_notes = driver.find_element(By.XPATH,"//td[contains(text(), 'Est. Value Notes:')]/following-sibling::td")
        print(f"Est. Value Notes: {value_notes.text.strip()}")
        description = driver.find_element(By.XPATH,"//td[contains(text(), 'Description:')]/following-sibling::td")
        print(f"Description: {description.text.strip()}")
        closing_date = driver.find_element(By.XPATH,"//td[contains(text(), 'Closing Date:')]/following-sibling::td")
        print(f"Closing Date: {closing_date.text.strip()}\n\n")
        if i != 6:
            driver.find_element(By.ID, "id_prevnext_next").click()
            time.sleep(1)
