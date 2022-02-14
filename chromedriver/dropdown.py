from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

import time

options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0")

driver = webdriver.Chrome(
    executable_path="./chromedriver",
    options=options
)

try:
    # Dropdown
    driver.get('http://the-internet.herokuapp.com/')
    # driver.get('http://the-internet.herokuapp.com/dropdown')
    dropdown_click = driver.find_element_by_xpath('//a[@href="/dropdown"]').click()
    time.sleep(10)

    driver.find_element_by_id("dropdown").click()
    time.sleep(5)

    driver.find_element_by_xpath("//option[@value='1']").click()
    time.sleep(5)

    driver.find_element_by_xpath("//option[@value='2']").click()
    time.sleep(10)


except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
