from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try: 
    link = "https://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
      return str(math.log(abs(12*math.sin(int(x)))))

    x_element = browser.find_element(By.ID, 'input_value').text
    print(x_element)
    x_result = calc(x_element)

    form_input = browser.find_element(By.ID, 'answer')
    form_input.send_keys(x_result)

    check = browser.find_element(By.CSS_SELECTOR, 'input[id="robotCheckbox"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", check)
    check.click()

    radio = browser.find_element(By.CSS_SELECTOR, 'input[id="robotsRule"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio)
    radio.click()

    submit = browser.find_element(By.CSS_SELECTOR, 'button[class="btn btn-primary"]')
    submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()