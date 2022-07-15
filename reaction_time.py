from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import chromedriver_autoinstaller

chromedriver_autoinstaller.install()


link = 'https://humanbenchmark.com/tests/reactiontime'
driver = webdriver.Chrome()
driver.get(link)

try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((
            By.XPATH, "//div[@class='css-1gr1qbh']/div[4]/div[1]"))
    )
finally:
    pass

element = driver.find_element(
    By.XPATH, "//div[@class='css-1gr1qbh']/div[4]/div[1]")
element.click()

status = ''

while status != 's':
    status = element.get_attribute("class")[5]

    if status in ('g', 'r'):
        element.click()
