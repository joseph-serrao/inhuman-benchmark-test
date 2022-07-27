from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import chromedriver_autoinstaller
from selenium.webdriver.chrome.options import Options


def main(drivers):

    # Explicit wait until the start button exists
    start_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[@class='css-de05nr e19owgy710' and contains(text(), 'Start')]"))
    )

    start_button.click()

    squares = []
    squares_class = []
    active = 'square active'

    # Getting and storing the div element objects inside squares
    for i in range(1, 4):
        for j in range(1, 4):
            squares.append(driver.find_element(
                By.XPATH, f"//div[@class='squares']/div[{i}]/div[{j}]"))

    # Dictionary is used to avoid duplication of the same square
    sequence = {}

    level = driver.find_element(
        By.XPATH, "//span[@class='css-dd6wi1']/span[2]")
    level_no = 0
    count = 1

    start_time = float('inf')
    end_time = 0.3
    waiting = False

    game_level_limit = 35

    while level_no < (game_level_limit + 1):
        level_no = int(level.text)

        # If the level has increased, increment the time it takes to wait for all the squares' animation
        if level_no > count:
            count += 1
            end_time = (0.55 * level_no) + 0.1

        # Get the class names from the list of square elements
        squares_class = [elem.get_attribute("class") for elem in squares]

        # check for the squares whose animation has started
        if active in squares_class:
            sequence[level_no] = squares_class.index(active)

        # Start waiting for all the squares to light up
        # The first if condition is always true when the first square lights up
        if len(sequence.values()) == level_no and not waiting:
            start_time = time.time()
            waiting = True

        # If the waiting time is complete, start clicking the squares
        if (time.time() - start_time) > end_time:
            # If specified game limit hasn't reached, click on the correct square else wrong one
            if level_no < game_level_limit:
                for i in sequence.values():
                    squares[i].click()
            else:
                squares[tuple(sequence.values())[1]].click()

            waiting = False

            start_time = float('inf')


if __name__ == "__main__":
    # Prevents the window from closing automaticallly after program is complete
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)

    chromedriver_autoinstaller.install()

    link = "https://humanbenchmark.com/tests/sequence"

    # Opening the page
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(link)

    main(driver)
