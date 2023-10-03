from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try: 
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
      return str(math.log(abs(12*math.sin(int(x)))))

    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)

    
    form_input = browser.find_element(By.ID, 'answer')
    form_input.send_keys(y)

    check = browser.find_element(By.CSS_SELECTOR, 'input[id="robotCheckbox"]')
    check.click()

    radio = browser.find_element(By.CSS_SELECTOR, 'input[id="robotsRule"]')
    radio.click()

    submit = browser.find_element(By.CSS_SELECTOR, 'button[class="btn btn-default"]')
    submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()