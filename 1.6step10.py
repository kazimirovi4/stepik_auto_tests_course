from selenium import webdriver
import time


link = "http://suninjuly.github.io/registration1.html"
# link = "http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    nameInput = browser.find_element_by_css_selector(".first_block [placeholder='Input your first name']")
    nameInput.send_keys("Johan")

    lastnameInput = browser.find_element_by_css_selector(".first_block [placeholder='Input your last name']")
    lastnameInput.send_keys("Ivanov")

    emailInput = browser.find_element_by_css_selector(".first_block [placeholder='Input your email']")
    emailInput.send_keys("johan@mail.com")

    phoneInput = browser.find_element_by_css_selector(".second_block [placeholder='Input your phone:']")
    emailInput.send_keys("+375335554433")

    addressInput = browser.find_element_by_css_selector(".second_block [placeholder='Input your address:']")
    emailInput.send_keys("Belarus, Minsk")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(5)
    browser.close()