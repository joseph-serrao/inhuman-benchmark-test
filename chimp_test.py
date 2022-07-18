from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import chromedriver_autoinstaller
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

chromedriver_autoinstaller.install()

link = "https://humanbenchmark.com/tests/chimp"

driver = webdriver.Chrome(options=chrome_options)
driver.get(link)

start_button = None

try:
    start_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[@class='css-de05nr e19owgy710' and contains(text(), 'Start')]"))
    )
finally:
    start_button.click()

for i in range(4, 42):
    for j in range(1, i+1):
        driver.find_element(
            By.CSS_SELECTOR, f"div[data-cellnumber='{j}']").click()

    driver.find_element(By.CSS_SELECTOR, ".css-de05nr.e19owgy710").click()
