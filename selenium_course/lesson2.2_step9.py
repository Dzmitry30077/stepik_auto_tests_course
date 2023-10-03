from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try: 
  link = "http://suninjuly.github.io/file_input.html"
  browser = webdriver.Chrome()
  browser.get(link)

  elements = browser.find_elements(By.CSS_SELECTOR, '.form-control')
  for element in elements:
    element.send_keys('ДаДа')

  send_file = browser.find_element(By.ID, 'file')
  current_dir = os.path.abspath(os.path.dirname(__file__))
  file_path = os.path.join(current_dir, 'files\lesson2.2_file.txt')
  send_file.send_keys(file_path)

  submit = browser.find_element(By.CSS_SELECTOR, 'button[class="btn btn-primary"]')
  submit.click()

finally:
  time.sleep(5)
  browser.quit()