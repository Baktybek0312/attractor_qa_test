from selenium import webdriver
from selenium.webdriver.common.keys import Keys

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
    dropdown_click = driver.find_element_by_xpath('//a[@href="/key_presses"]').click()
    time.sleep(10)

    input_text = driver.find_element_by_id("target")
    input_text.clear()
    input_text1 = input()
    input_text.send_keys(input_text1)
    input_text.send_keys(Keys.ENTER)
    time.sleep(10)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
