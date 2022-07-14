from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import chromedriver_autoinstaller

chromedriver_autoinstaller.install()

link = 'https://humanbenchmark.com/tests/aim'

driver = webdriver.Chrome()
driver.get(link)

while True:
    try:
        target_button = driver.find_element(By.CLASS_NAME, "css-ad1j3y")
        webdriver.ActionChains(driver).move_to_element(
            target_button).click().perform()
    except NoSuchElementException:
        break
