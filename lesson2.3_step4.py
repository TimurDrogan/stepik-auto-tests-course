from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
  
  link = "http://suninjuly.github.io/alert_accept.html"
  browser = webdriver.Chrome()
  browser.get(link)
  
  button_cl = browser.find_element_by_tag_name("button")
  button_cl.click()
  
  confirm = browser.switch_to.alert
  confirm.accept()
  
  x_element = browser.find_element_by_css_selector("#input_value")
  x = x_element.text
  y = calc(x)  
  
  input1 = browser.find_element_by_id("answer")
  input1.send_keys(y) 
  
  button_cl2 = browser.find_element_by_tag_name("button")
  button_cl2.click()
  
  alert = browser.switch_to.alert
  alert_text = alert.text

finally:
    time.sleep(10)
    browser.quit()
  
  