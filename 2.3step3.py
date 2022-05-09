import math

from selenium import webdriver
import time


link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)


try:
    send_button = browser.find_element_by_css_selector(".btn-primary")
    send_button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = browser.find_element_by_id("input_value")
    x_value = x_element.text

    y = calc(x_value)

    answerInput = browser.find_element_by_id("answer")
    answerInput.send_keys(y)

    send_button = browser.find_element_by_css_selector(".btn-primary")
    send_button.click()


finally:
    time.sleep(5)
    browser.close()