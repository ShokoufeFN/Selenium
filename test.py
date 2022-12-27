import os
from pathlib import Path
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
s = Service()
# options.add_argument("--incognito")
options.add_argument("--headless")
driver = webdriver.Chrome(service=s, options=options)
driver.get("https://www.yahoo.com")

sleep(2)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(10)
current_path = Path(__file__).parent
filename = os.path.join(str(current_path), 'session2.png')
driver.save_screenshot(filename)
