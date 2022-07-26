from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import chromedriver_autoinstaller
from selenium.webdriver.chrome.options import Options

# Prevents the window from closing automaticallly after program is complete
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

chromedriver_autoinstaller.install()

# Opening the page
link = "https://humanbenchmark.com/tests/memory"
driver = webdriver.Chrome(options=chrome_options)
driver.get(link)

start_button = None

# Explicit wait until the start button exists
start_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "//button[@class='css-de05nr e19owgy710' and contains(text(), 'Start')]"))
)

start_button.click()

squares = []
squares_class = []
a = 'square active'
grid_length = 3

# Get the grid of squares from given length


def getSquares(n):
    squares.clear()
    for i in range(1, n):
        for j in range(1, n):
            squares.append(driver.find_element(
                By.XPATH, f"//div[@class='css-hvbk5q eut2yre0']/div[{i}]/div[{j}]"))


# Initialize squares with the div elements
getSquares(grid_length + 1)

# Dictionary is used to avoid duplication
sequence = {}

level = driver.find_element(By.XPATH, "//span[@class='css-dd6wi1']/span[2]")
level_no = 0
count = 0

start_time = float('inf')
end_time = 1.5
waiting = False

grid_increased_count = 1
level_to_increase = 3

while level_no < 40:
    level_no = int(level.text)

    # If level has increased
    if level_no > count:
        # Start waiting for the animation to complete
        if not waiting:
            start_time = time.time()
            waiting = True

        # Increase the size of the grid according to a quadratic series
        # The size of the grid increases at levels 3, 6, 9, 14, 19, 24, 31, 38, 45...
        if level_no == level_to_increase:
            grid_length += 1
            getSquares(grid_length + 1)
            grid_increased_count += 1
            level_to_increase = (
                ((grid_increased_count ** 2) + (6 * grid_increased_count) + 2) // 3)
            # This formula finds the nth term of the above quadratic sries

        count += 1

    # Get the class names of square elements while waiting
    if waiting:
        squares_class = [elem.get_attribute("class")[0] for elem in squares]

    # Find the animated squares from the class list
    for i in range(len(squares_class)):
        if squares_class[i] == 'a':
            sequence[str(i)] = i

    # If the wait time is complete, start clicking the squares
    if (time.time() - start_time) > end_time:

        for i in sequence.values():
            squares[i].click()

        waiting = False

        start_time = float('inf')

        sequence.clear()
