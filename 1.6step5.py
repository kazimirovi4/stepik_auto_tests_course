import time
import math
from selenium import webdriver


link = "http://suninjuly.github.io/find_link_text"


try:
    browser = webdriver.Chrome()
    browser.get(link)
    link1 = browser.find_element_by_partial_link_text("224592")
    link1.click()

    # num = str(math.ceil(math.pow(math.pi, math.e)*10000))

    input0 = browser.find_element_by_tag_name('input')
    input0.send_keys("Johan")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Johanov")
    input3 = browser.find_element_by_class_name("city")
    input3.send_keys("Minsk")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("Belarus")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(15)
    browser.quit()
