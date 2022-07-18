from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import chromedriver_autoinstaller
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

chromedriver_autoinstaller.install()


link = 'https://humanbenchmark.com/tests/typing'
driver = webdriver.Chrome(options=chrome_options)
driver.get(link)

char_elem = None
char = ''

# explicit wait until the word element exists
try:
    char_elem = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".incomplete.current"))
    )
finally:
    char = char_elem.text

input_elem = driver.find_element(By.CSS_SELECTOR, ".letters.notranslate")

# typing the words
while True:
    if char.strip() == '':
        input_elem.send_keys(Keys.SPACE)
    else:
        input_elem.send_keys(char)

    # end condition
    # break if the last word has been typed (i.e. highlighted word does not exist)
    try:
        char = driver.find_element(By.CSS_SELECTOR, ".incomplete.current").text

    except NoSuchElementException:
        print("reached end of text")
        break
