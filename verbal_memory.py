from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import chromedriver_autoinstaller
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

chromedriver_autoinstaller.install()

link = "https://humanbenchmark.com/tests/verbal-memory"

driver = webdriver.Chrome(options=chrome_options)
driver.get(link)

start_button = None

try:
    start_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[@class='css-de05nr e19owgy710' and contains(text(), 'Start')]"))
    )
finally:
    start_button.click()


word_elem = driver.find_element(By.CLASS_NAME, "word").text
words_list = []

for i in range(300):
    word = word_elem.text

    # NOTE: I am not finding the button elements beforehand because they have a chance to be
    # 		 clicked at the same time which gives an error
    if word in words_list:
        seen_button = driver.find_element(
            By.XPATH, "//button [contains( text(), 'SEEN')]")
        seen_button.click()
    else:
        words_list.append(word)
        new_button = driver.find_element(
            By.XPATH, "//button [contains( text(), 'NEW')]")
        new_button.click()
