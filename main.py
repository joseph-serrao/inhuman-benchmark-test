from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import chromedriver_autoinstaller
from selenium.webdriver.chrome.options import Options
from scripts import (aim_trainer, chimp_test, number_memory, reaction_time,
                     sequence_memory, typing_test, verbal_memory, visual_memory)

# Prevents the window from closing automaticallly after program is complete
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

chromedriver_autoinstaller.install()

# Opening the page
link = 'https://humanbenchmark.com/tests/aim'
driver = webdriver.Chrome(options=chrome_options)
driver.get(link)

aim_trainer.main(driver)
