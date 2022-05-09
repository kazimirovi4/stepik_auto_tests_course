from selenium import webdriver
import time
import math


link = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_css_selector("[id='input_value']")
    x = x_element.text

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    y = calc(x)

    answerInput = browser.find_element_by_css_selector(".form-control")
    answerInput.send_keys(y)

    checkbox = browser.find_element_by_css_selector("[for='robotCheckbox']")
    checkbox.click()

    radiobutton = browser.find_element_by_css_selector("[for='robotsRule']")
    radiobutton.click()

    button = browser.find_element_by_css_selector(".btn-default")
    button.click()


finally:
    time.sleep(5)
    browser.close()