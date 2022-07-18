from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import chromedriver_autoinstaller
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

chromedriver_autoinstaller.install()

link = 'https://humanbenchmark.com/tests/aim'

driver = webdriver.Chrome(options=chrome_options)
driver.get(link)

try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "css-ad1j3y"))
    )
finally:
    pass

while True:
    try:
        target_button = driver.find_element(By.CLASS_NAME, "css-ad1j3y")
        webdriver.ActionChains(driver).click(target_button).perform()
    except NoSuchElementException:
        break
