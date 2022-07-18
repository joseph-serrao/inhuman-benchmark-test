from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import chromedriver_autoinstaller

chromedriver_autoinstaller.install()

link = "https://humanbenchmark.com/tests/number-memory"

driver = webdriver.Chrome()
driver.get(link)

start_button = None

try:
    start_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[@class='css-de05nr e19owgy710' and contains(text(), 'Start')]"))
    )
finally:
    start_button.click()

for i in range(20):
    number = driver.find_element(By.CSS_SELECTOR, ".big-number").text

    input = WebDriverWait(driver, 300).until(
        EC.presence_of_element_located(
            (By.TAG_NAME, "input"))
    )

    input.send_keys(number)

    driver.find_element(By.CSS_SELECTOR, ".css-de05nr.e19owgy710").click()
    driver.find_element(By.CSS_SELECTOR, ".css-de05nr.e19owgy710").click()
