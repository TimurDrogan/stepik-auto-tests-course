from selenium import webdriver
import time
import os

file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data.txt')

if not os.path.exists(file_path):
    with open(file_path, 'w') as f:
        pass
try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")
 
    inputs = ['Aleksey', 'Bychutkin', 'test@gmail.com', file_path]
    
    for element, value in zip(browser.find_elements_by_tag_name('input'), inputs):
        element.send_keys(value)
    
    browser.find_element_by_css_selector('button.btn').click()
finally:
    time.sleep(10)
    browser.quit()