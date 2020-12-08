from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    y = calc(x)
    
    input1 = browser.find_element_by_css_selector("#answer")
    input1.send_keys(y)
    
    check_box = browser.find_element_by_css_selector("#robotCheckbox")
    check_box.click()
    
    rad_butt = browser.find_element_by_css_selector("#robotsRule")
    rad_butt.click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    
    time.sleep(10)
    browser.quit()