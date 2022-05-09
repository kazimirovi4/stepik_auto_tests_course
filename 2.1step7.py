from selenium import webdriver
import time
import math


link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = browser.find_element_by_id("treasure")
    x_value = x_element.get_attribute("valuex")

    y = calc(x_value)

    answerInput = browser.find_element_by_id("answer")
    answerInput.send_keys(y)

    checkbox = browser.find_element_by_id("robotCheckbox")
    checkbox.click()

    radiobutton = browser.find_element_by_id("robotsRule")
    radiobutton.click()

    button = browser.find_element_by_css_selector(".btn-default")
    button.click()


finally:
    time.sleep(5)
    browser.close()