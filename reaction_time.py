from xml.dom.minidom import Element
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import chromedriver_autoinstaller
from selenium.webdriver.chrome.options import Options

# Prevents the window from closing automaticallly after program is complete
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

chromedriver_autoinstaller.install()

# Opening the page
link = 'https://humanbenchmark.com/tests/reactiontime'
driver = webdriver.Chrome(options=chrome_options)
driver.get(link)

# Explicit wait until the start button exists
div_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((
        By.XPATH, "//div[@class='css-1gr1qbh']/div[4]/div[1]"))
)

# Start
div_element.click()

status = ''

# I have used single letters to reduce time taken to run
while status != 's':
    status = div_element.get_attribute("class")[5]

    # g - green (time to click)
    # r - ready (move to next round)
    # s - waiting to click
    if status in ('g', 'r'):
        div_element.click()
