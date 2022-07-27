from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import chromedriver_autoinstaller
from selenium.webdriver.chrome.options import Options


def main(driver):

    # Explicit wait until the start button exists
    start_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[@class='css-de05nr e19owgy710' and contains(text(), 'Start')]"))
    )

    start_button.click()

    word_element = driver.find_element(By.CLASS_NAME, "word")
    words_list = []

    for i in range(300):
        word = word_element.text

        # I am not finding the seen and new button elements before the loop
        # because they have a chance to be clicked at the same time which returns an error
        if word in words_list:
            seen_button = driver.find_element(
                By.XPATH, "//button [contains( text(), 'SEEN')]")
            seen_button.click()
        else:
            words_list.append(word)
            new_button = driver.find_element(
                By.XPATH, "//button [contains( text(), 'NEW')]")
            new_button.click()


if __name__ == "__main__":
    # Prevents the window from closing automaticallly after program is complete
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)

    chromedriver_autoinstaller.install()

    link = "https://humanbenchmark.com/tests/verbal-memory"

    # Opening the page
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(link)

    main(driver)
