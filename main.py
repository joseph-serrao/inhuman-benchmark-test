from selenium import webdriver
import time
import chromedriver_autoinstaller
from selenium.webdriver.chrome.options import Options
import importlib
from scripts import __all__ as modules_list

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

chromedriver_autoinstaller.install()

driver = webdriver.Chrome(options=chrome_options)

main_path = "https://humanbenchmark.com/tests/"
pages = ["aim", "chimp", "number-memory", "reactiontime",
         "sequence", "typing", "verbal-memory", "memory"]

start = time.time()

# importing the modules dynamically and calling their main functions
for page, module in zip(pages, modules_list):
    driver.get(main_path + page)
    importlib.import_module(module).main(driver)

driver.get("https://humanbenchmark.com/dashboard")

print(time.time() - start)
