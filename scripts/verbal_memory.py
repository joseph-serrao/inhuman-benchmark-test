from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import chromedriver_autoinstaller
from selenium.webdriver.chrome.options import Options
from scripts import game_limit


def main(driver):

    # Explicit wait until the start button exists
    start_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[@class='css-de05nr e19owgy710' and contains(text(), 'Start')]"))
    )

    start_button.click()

    word_element = driver.find_element(By.CLASS_NAME, "word")
    words_list = []

    game_level_limit = game_limit["verbal"]

    for i in range(game_level_limit):

        # I am not finding the seen and new button elements before the loop
        # because they have a chance to be clicked at the same time which returns an error
        if word_element.text in words_list:
            seen_button = driver.find_element(
                By.XPATH, "//button [contains( text(), 'SEEN')]")
            seen_button.click()
        else:
            words_list.append(word_element.text)
            new_button = driver.find_element(
                By.XPATH, "//button [contains( text(), 'NEW')]")
            new_button.click()

    # Send the wrong answer to end the game
    for _ in range(3):
        if word_element.text in words_list:
            driver.find_element(
                By.XPATH, "//button [contains( text(), 'NEW')]").click()
        else:
            driver.find_element(
                By.XPATH, "//button [contains( text(), 'SEEN')]").click()

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

    link = "https://humanbenchmark.com/tests/verbal-memory"

    # Opening the page
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(link)

    main(driver)
else:
    from scripts import game_limit
