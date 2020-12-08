from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input_name = browser.find_element_by_css_selector("[class='form-group first_class'] input:required")
    input_name.send_keys("Timur")
    input_lastname = browser.find_element_by_css_selector("[class='form-group second_class'] input:required")
    input_lastname.send_keys("Drogan")
    input_email = browser.find_element_by_css_selector("[class='form-group third_class'] input:required")
    input_email.send_keys("super_plumbum@mail.ru")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(1)

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()