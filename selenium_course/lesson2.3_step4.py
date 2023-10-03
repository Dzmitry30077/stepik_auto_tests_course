from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
  link = 'http://suninjuly.github.io/alert_accept.html'
  browser = webdriver.Chrome()
  browser.get(link)

  def calc(x):
      return str(math.log(abs(12*math.sin(int(x)))))

  btn_submit = browser.find_element(By.CSS_SELECTOR, 'button[class="btn btn-primary"]')
  btn_submit.click()

  confirm = browser.switch_to.alert
  confirm.accept()

  time.sleep(1)

  x_value = browser.find_element(By.ID, 'input_value').text
  x_result = calc(x_value)

  answer = browser.find_element(By.ID, 'answer')
  answer.send_keys(x_result)

  time.sleep(1)

  btn_second_submit = browser.find_element(By.CSS_SELECTOR, 'button[class="btn btn-primary"]')
  btn_second_submit.click()

finally:
  print(browser.switch_to.alert.text)
  browser.quit()