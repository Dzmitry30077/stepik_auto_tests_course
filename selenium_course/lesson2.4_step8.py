from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

try:
  link = 'http://suninjuly.github.io/explicit_wait2.html'
  browser = webdriver.Chrome()
  browser.get(link)

  def calc(x):
      return str(math.log(abs(12*math.sin(int(x)))))
  

  WebDriverWait(browser, 12).until(
     EC.text_to_be_present_in_element((By.ID, 'price'), '100')
  )
  book_btn = browser.find_element(By.ID, 'book')
  book_btn.click()

  time.sleep(1)
  x_value = browser.find_element(By.ID, 'input_value').text
  x_result = calc(x_value)

  answer = browser.find_element(By.ID, 'answer')
  answer.send_keys(x_result)

  submit = browser.find_element(By.ID, 'solve')
  submit.click()
  
finally:
  print(browser.switch_to.alert.text)
  time.sleep(5)
