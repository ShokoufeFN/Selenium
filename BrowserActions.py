from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

# browser action -> open
s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("https://google.com")
# browser action -> get title
window_title = driver.title
print(window_title)
sleep(2)

# browser action -> back
driver.get("https://wikipedia.com")
sleep(2)
driver.back()
sleep(2)
driver.forward()
driver.refresh()
driver.switch_to.new_window('tab')
driver.switch_to.new_window('window')

current = driver.current_window_handle
print('Current Handler:' + str(current))

all_handler = driver.window_handles
print('All Handler: ' + str(all_handler))

driver.switch_to.window(all_handler[0])
driver.close()  # close current handel

driver.quit()
s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("https://google.com")
winsize = driver.get_window_size()
print(winsize)
window_width = winsize['width']
window_height = winsize['height']
print('width:' + str(window_width) + ' , ' + 'height: ' + str(window_height))

driver.set_window_size(500, 300)
window_size = driver.get_window_size()
assert winsize['width'] == 500
assert winsize['height'] == 300

current_position = driver.get_window_position()
print('current position: ' + str(current_position))

driver.set_window_position(200, 300, 0)
assert driver.get_window_position()['x'] == 200

driver.maximize_window()
sleep(2)
driver.minimize_window()
sleep(2)
driver.fullscreen_window()
sleep(2)


# search_field = driver.find_element("id", "input")
# search_field.send_keys("Keep it simple stupid")
# search_field.send_keys(Keys.ENTER)
driver.quit()  # close all session
