from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
  link = 'http://suninjuly.github.io/redirect_accept.html'
  browser = webdriver.Chrome()
  browser.get(link)

  def calc(x):
      return str(math.log(abs(12*math.sin(int(x)))))
  
  btn_first_submit = browser.find_element(By.CSS_SELECTOR, 'button[class="trollface btn btn-primary"]')
  btn_first_submit.click()
  
  second_window = browser.window_handles[1]
  browser.switch_to.window(second_window)

  x_value = browser.find_element(By.ID, 'input_value').text
  x_result = calc(x_value)

  answer = browser.find_element(By.ID, 'answer')
  answer.send_keys(x_result)

  btn_second_submit = browser.find_element(By.CSS_SELECTOR, 'button[class="btn btn-primary"]')
  btn_second_submit.click()

finally:
  print(browser.switch_to.alert.text)
