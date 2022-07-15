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

squares = []
squares_class = []
a = 'square active'
grid_length = 3


def getSquares(n):
    squares.clear()
    for i in range(1, n):
        for j in range(1, n):
            squares.append(driver.find_element(
                By.XPATH, f"//div[@class='css-hvbk5q eut2yre0']/div[{i}]/div[{j}]"))


getSquares(grid_length + 1)


sequence = {}

level = driver.find_element(By.XPATH, "//span[@class='css-dd6wi1']/span[2]")
level_no = 0
count = 0

start_time = float('inf')
end_time = 3.25
wait_complete = False

grid_increased_count = 1
level_to_increase = 3

while True:
    level_no = int(level.text)

    if level_no > count:
        if not wait_complete:
            start_time = time.time()
            wait_complete = True

        if level_no == level_to_increase:
            grid_length += 1
            getSquares(grid_length + 1)
            grid_increased_count += 1
            level_to_increase = (
                ((grid_increased_count ** 2) + (6 * grid_increased_count) + 2) // 3)

        count += 1

    if wait_complete:
        squares_class = [elem.get_attribute("class")[0] for elem in squares]

    for i in range(len(squares_class)):
        if squares_class[i] == 'a':
            2
            sequence[str(i)] = i

    if (time.time() - start_time) > end_time:

        for i in sequence.values():
            squares[i].click()

        wait_complete = False

        start_time = float('inf')

        sequence.clear()
