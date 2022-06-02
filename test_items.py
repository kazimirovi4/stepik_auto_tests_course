import time


def test_check_language_button_add_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    button_add_to_basket = browser.find_elements_by_class_name("btn-add-to-basket")
    assert button_add_to_basket, 'button add to basket does bot exist!'
    time.sleep(30)