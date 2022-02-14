from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import os.path
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
    dropdown_click = driver.find_element_by_xpath('//a[@href="/download"]').click()
    time.sleep(10)

    driver.get('http://the-internet.herokuapp.com/download')
    download_file = driver.find_element_by_id('content')
    download_file.click()

    # while not os.path.exists():
    #     time.sleep(1)
    # if os.path.isfile():
    #     print()
    # else:
    #     raise ValueError("not file" )
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
