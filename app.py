#https://medium.com/analytics-vidhya/automate-gui-clicks-and-save-screenshots-fcbc9d52a08c

import pyautogui, time

repetitions = 100
page_number = 1

for i in range(repetitions):
	image = pyautogui.screenshot(region=(2561,33,995,1295))
	image.save(str(page_number) + ".png")
	page_number = page_number + 2
	pyautogui.click(2880,1361)
	time.sleep(1.5)

# region=(793,41,739,1118)
#2561
#1566