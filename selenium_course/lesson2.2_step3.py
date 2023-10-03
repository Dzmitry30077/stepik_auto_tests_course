from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

try: 
    link = "https://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element(By.ID, 'num1').text
    num2 = browser.find_element(By.ID, 'num2').text
    result = int(num1) + int(num2)
    print(result)

    select = Select(browser.find_element(By.ID, 'dropdown'))
    select.select_by_value(str(result))

    submit = browser.find_element(By.CSS_SELECTOR, 'button[class="btn btn-default"]')
    submit.click()

finally:
    time.sleep(5)
    browser.quit()