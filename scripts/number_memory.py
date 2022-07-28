from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import chromedriver_autoinstaller
from selenium.webdriver.chrome.options import Options
from __init__ import game_limit


def main(driver):

    # Explicit wait until the start button exists
    start_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[@class='css-de05nr e19owgy710' and contains(text(), 'Start')]"))
    )

    start_button.click()

    game_level_limit = game_limit["number"]
    input = None

    for i in range(game_level_limit - 1):
        number = driver.find_element(By.CSS_SELECTOR, ".big-number").text

        # Get the number and send it as input
        input = WebDriverWait(driver, 300).until(
            EC.presence_of_element_located(
                (By.TAG_NAME, "input"))
        )

        input.send_keys(number)

        # Go to next level
        driver.find_element(By.CSS_SELECTOR, ".css-de05nr.e19owgy710").click()
        driver.find_element(By.CSS_SELECTOR, ".css-de05nr.e19owgy710").click()

    # Send wrong input to end the game
    input = WebDriverWait(driver, 300).until(
        EC.presence_of_element_located(
            (By.TAG_NAME, "input"))
    )
    input.send_keys("whatever")
    driver.find_element(By.CSS_SELECTOR, ".css-de05nr.e19owgy710").click()

    # click on save score button
    if __name__ != "__main__":
        driver.find_element(
            By.CSS_SELECTOR, ".css-qm6rs9.e19owgy710").click()


if __name__ == "__main__":
    # Prevents the window from closing automaticallly after program is complete
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)

    chromedriver_autoinstaller.install()

    link = "https://humanbenchmark.com/tests/number-memory"

    # Opening the page
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(link)

    main(driver)
