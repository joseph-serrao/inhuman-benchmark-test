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

    game_level_limit = game_limit["chimp"]

    # Find the each number and click on it
    for i in range(4, game_level_limit):
        for j in range(1, i+1):
            driver.find_element(
                By.CSS_SELECTOR, f"div[data-cellnumber='{j}']").click()

        # Click on next round button
        try:
            driver.find_element(
                By.CSS_SELECTOR, ".css-de05nr.e19owgy710").click()
        except:
            break

    # Click on incorrect option to end the game
    if game_level_limit < 42:
        for i in range(3):
            driver.find_element(
                By.CSS_SELECTOR, f"div[data-cellnumber='{j}']").click()
            if i != 2:
                driver.find_element(
                    By.CSS_SELECTOR, ".css-de05nr.e19owgy710").click()

    # click on save score button
    if __name__ != "__main__":
        driver.find_element(
            By.CSS_SELECTOR, ".css-qm6rs9.e19owgy710").click()


if __name__ == "__main__":
    from __init__ import game_limit

    # Prevents the window from closing automaticallly after program is complete
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)

    chromedriver_autoinstaller.install()

    link = "https://humanbenchmark.com/tests/chimp"

    # Opening the page
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(link)

    main(driver)
else:
    from scripts import game_limit
