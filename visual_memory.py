from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import chromedriver_autoinstaller

chromedriver_autoinstaller.install()

link = "https://humanbenchmark.com/tests/memory"

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

squares = {}
squares_class = []
a = 'square active'
sequence = []

for i in range(1, 4):
    for j in range(1, 4):
        squares.append(driver.find_element(
            By.XPATH, f"//div[@class='css-hvbk5q eut2yre0']/div[{i}]/div[{j}]"))

while True:
    squares_class = [elem.get_attribute("class")[0] for elem in squares]
    print(squares_class)

    for i in range(len(squares_class)):
        if squares_class[i] == 'a':
            sequence.append(i)

    print(sequence)
