import time
# import math
from selenium import webdriver
from  selenium.webdriver.common.by import By


link = "http://suninjuly.github.io/find_xpath_form"


try:
    browser = webdriver.Chrome()
    browser.get(link)
    # link1 = browser.find_element_by_partial_link_text("224592")
    # link1.click()

    # num = str(math.ceil(math.pow(math.pi, math.e)*10000))

    input0 = browser.find_element_by_xpath("/html/body/div/form/div[1]/input")
    input0.send_keys("Johan")
    input2 = browser.find_element_by_xpath("/html/body/div/form/div[2]/input")
    input2.send_keys("Johanov")
    input3 = browser.find_element_by_xpath("/html/body/div/form/div[3]/input")
    input3.send_keys("Minsk")
    input4 = browser.find_element_by_xpath("//*[@id='country']")
    input4.send_keys("Belarus")
    button = browser.find_element_by_xpath("/html/body/div/form/div[6]/button[3]")
    button.click()

finally:
    time.sleep(15)
    browser.quit()
