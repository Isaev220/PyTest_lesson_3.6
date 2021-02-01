from selenium import webdriver
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_presence_button_basket(browser):
    browser.get(link)
    button = browser.find_elements_by_class_name("btn.btn-lg.btn-primary.btn-add-to-basket")
    print(button)
    assert button, 'кнопка не найдена'
