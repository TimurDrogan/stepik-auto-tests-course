import time
import math

from selenium import webdriver
from selenium.webdriver.support.ui import Select

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    number1 = browser.find_element_by_css_selector("#num1")
    x = number1.text

    number2 = browser.find_element_by_css_selector("#num2")
    y = number2.text

    z = str(int(x)+int(y))

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(z) 
    
    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:

    time.sleep(10)
    browser.quit()