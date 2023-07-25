from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_button_add_to_basket_exist(browser):
	browser.get(link)
	#browser.implicitly_wait(5)
	time.sleep(10)
	browser.find_element(By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")
	time.sleep(10)

