import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select


link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)


    x_element1 = browser.find_element_by_id("num1")
    x_element2 = browser.find_element_by_id("num2")


    y = int(x_element1.text) + int(x_element2.text)
    print(y)

    sel = Select(browser.find_element_by_class_name("custom-select"))
    sel.select_by_value(str(y))

    button = browser.find_element_by_css_selector(".btn-default")
    button.click()


finally:
    time.sleep(10)
    browser.close()