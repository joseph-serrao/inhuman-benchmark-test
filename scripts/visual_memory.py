from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import chromedriver_autoinstaller
from selenium.webdriver.chrome.options import Options


def main(driver):

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

    def get_squares(n):
        squares.clear()
        for i in range(1, n):
            for j in range(1, n):
                squares.append(driver.find_element(
                    By.XPATH, f"//div[@class='css-hvbk5q eut2yre0']/div[{i}]/div[{j}]"))

    # Initialize squares with the div elements
    get_squares(grid_length + 1)

    # Dictionary is used to avoid duplication
    sequence = {}

    level = driver.find_element(
        By.XPATH, "//span[@class='css-dd6wi1']/span[2]")
    level_no = 0
    count = 0

    start_time = float('inf')
    end_time = 1.8
    waiting = False

    grid_increased_count = 1
    level_to_increase = 3

    game_level_limit = 35

    while level_no < (game_level_limit + 1):
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
                end_time += 0.175
                grid_length += 1
                get_squares(grid_length + 1)
                grid_increased_count += 1
                level_to_increase = (
                    ((grid_increased_count ** 2) + (6 * grid_increased_count) + 2) // 3)
                # This formula finds the nth term of the above quadratic sries

            # Don't increment on the last level, since we get 3 lives
            if level_no < game_level_limit:
                count += 1

        # Get the class names of square elements while waiting
        if waiting:
            squares_class = [elem.get_attribute(
                "class")[0] for elem in squares]

        # Find the animated squares from the class list
        for i in range(len(squares_class)):
            # Get the correct or incorrect squares depending on whether the specified game limit has reached
            if level_no < game_level_limit:
                if squares_class[i] == 'a':
                    sequence[str(i)] = i
            else:
                if squares_class[i] != 'a':
                    sequence[str(i)] = i
        # If the wait time is complete, start clicking the squares
        if (time.time() - start_time) > end_time:

            for i in sequence.values():
                squares[i].click()

            waiting = False

            start_time = float('inf')

            sequence.clear()


if __name__ == "__main__":
    # Prevents the window from closing automaticallly after program is complete
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)

    chromedriver_autoinstaller.install()

    link = "https://humanbenchmark.com/tests/memory"

    # Opening the page
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(link)

    main(driver)
