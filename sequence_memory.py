from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pdb

link = "https://humanbenchmark.com/tests/sequence"

driver = webdriver.Firefox()
driver.get(link)

start_button = None

try:
	start_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[@class='css-de05nr e19owgy710' and contains(text(), 'Start')]"))
    )
finally:
	start_button.click()

squares = []
squares_class = []
a = 'square active'

for i in range(1,4):
	for j in range(1,4):
		squares.append(driver.find_element(By.XPATH, f"//div[@class='squares']/div[{i}]/div[{j}]"))


sequence = {}
level = driver.find_element(By.XPATH, "//span[@class='css-dd6wi1']/span[2]")
count = 1
start_time = float('inf')
end_time = 0.3
wait_complete = False

while True:
	level_no = int(level.text)

	if level_no > count:

		count += 1
		end_time = (0.55 * level_no) + 0.1

	squares_class = [elem.get_attribute("class") for elem in squares]

	if a in squares_class:
		sequence[level_no] = squares_class.index(a)

	if len(sequence.values()) == level_no and not wait_complete:
		start_time = time.time()
		wait_complete = True

	print(sequence)
	print(time.time() - start_time)

	if (time.time() - start_time) > end_time:
		#pdb.set_trace()
		print("time to click")
		for i in sequence.values():
			squares[i].click()

		wait_complete = False

		start_time = float('inf')



