from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import chromedriver_autoinstaller
from selenium.webdriver.chrome.options import Options


def main():

    # Opening the page
    link = 'https://humanbenchmark.com/tests/typing'
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(link)

    char_element = None
    char_string = ''

    # Explicit wait until the highlighted character element exists
    char_element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".incomplete.current"))
    )

    char_string = char_element.text

    input_elem = driver.find_element(By.CSS_SELECTOR, ".letters.notranslate")

    # Typing the characters
    while True:
        if char_string.strip() == '':
            # The space read from the HTML code does not correspond to selenium spaces
            input_elem.send_keys(Keys.SPACE)
        else:
            input_elem.send_keys(char_string)

        # End condition
        # Break if the last character has been typed (i.e. highlighted character does not exist)
        try:
            char_string = driver.find_element(
                By.CSS_SELECTOR, ".incomplete.current").text
        except NoSuchElementException:
            break


if __name__ == "__main__":
    # Prevents the window from closing automaticallly after program is complete
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)

    chromedriver_autoinstaller.install()

    main()
