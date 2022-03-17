from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


link = 'https://humanbenchmark.com/tests/reactiontime'
driver = webdriver.Firefox()
driver.get(link)

element = driver.find_element(By.XPATH, "//div[@class='css-1gr1qbh']/div[4]/div[1]")
element.click()

status = ''

while status != 's':
	status = element.get_attribute("class")[5]
	
	if status in ('g', 'r'):
		element.click()
