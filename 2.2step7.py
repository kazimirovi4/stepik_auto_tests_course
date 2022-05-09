from selenium import webdriver
import time
import os


link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)


try:
    name_input = browser.find_element_by_css_selector("[placeholder='Enter first name']")
    name_input.send_keys("Johan")

    last_input = browser.find_element_by_css_selector("[placeholder='Enter last name']")
    last_input.send_keys("Ivanov")

    email_input = browser.find_element_by_css_selector("[placeholder='Enter email']")
    email_input.send_keys("jivanov@mail.net")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')

    file_button = browser.find_element_by_id("file")
    file_button.send_keys(file_path)

    send_button = browser.find_element_by_css_selector(".btn-primary")
    send_button.click()


finally:
    time.sleep(10)
    browser.close()