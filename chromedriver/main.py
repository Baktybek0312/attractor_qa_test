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
)# здесь путь нашего директория, то есть путь где находиться наш драйвер

try:
    driver.get('https://the-internet.herokuapp.com/') # для того чтобы зайти в через webriver
    time.sleep(5)
    driver.get('http://admin:admin@the-internet.herokuapp.com/basic_auth') # для аутентификации
    time.sleep(5)
    driver.get('https://the-internet.herokuapp.com/login')
    login_input = driver.find_element_by_id("username")
    login_input.clear()
    login_input.send_keys("admin")
    time.sleep(10)

    password_input = driver.find_element_by_id("password")
    password_input.clear()
    password_input.send_keys("admin")
    time.sleep(10)
    password_input.send_keys(Keys.ENTER)

    login_button = driver.find_element_by_id("radius").click()
    time.sleep(10)

    driver.get('')

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()

