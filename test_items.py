
import pytest
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def test_button_add_to_basket(browser):
    
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.implicitly_wait(30)
    browser.get(link)
    
    try:
        button = browser.find_element(By.CSS_SELECTOR, "#add_to_basket_form .btn")
    except NoSuchElementException:
        assert False, "Button not found"
   

