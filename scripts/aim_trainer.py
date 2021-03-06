from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import chromedriver_autoinstaller
from selenium.webdriver.chrome.options import Options


def main(driver):

    # Explicit wait until the target button exists
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "css-ad1j3y"))
    )

    # Repeatedly find the target button and then click on it
    # else quit if it doesn't exist
    while True:
        try:
            target_button = driver.find_element(By.CLASS_NAME, "css-ad1j3y")
            webdriver.ActionChains(driver).click(target_button).perform()
        except NoSuchElementException:
            break

    # click on save score button
    if __name__ != "__main__":
        driver.find_element(
            By.CSS_SELECTOR, ".css-qm6rs9.e19owgy710").click()


if __name__ == "__main__":
    # Prevents the window from closing automaticallly after program is complete
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)

    chromedriver_autoinstaller.install()

    link = 'https://humanbenchmark.com/tests/aim'

    # Opening the page
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(link)

    main(driver)
