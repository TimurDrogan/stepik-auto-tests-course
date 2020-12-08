from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(treasure_valued)))))


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    secret_treasure = browser.find_element_by_id("treasure")
    treasure_valued = secret_treasure.get_attribute("valuex")
    y = calc(treasure_valued)

    input1 = browser.find_element_by_id("answer")
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