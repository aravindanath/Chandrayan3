import pytest
from selenium import webdriver

from selenium.webdriver.common.keys import Keys
"""
1. Launch amazon
search a product add to cart

"""

def test_launchBrowser():
    global driver
    path = "..//driver//chromedriver"
    driver = webdriver.Chrome(executable_path=path)
    driver.fullscreen_window()
    driver.implicitly_wait(40)
    driver.get("https://www.flipkart.com")



def test_search():
    # driver.find_element_by_css_selector("#twotabsearchtextbox").send_keys("MOSISO MacBook Pro 13 inch Case 2019 2018 2017 2016 Release A2159 A1989 A1706 A1708, Plastic Pattern Hard Shell & Keyboard Cover & Screen Protector Compatible with MacBook Pro 13, White Marble",Keys.ENTER)
    title = driver.title;
    print(title)

def test_close():
    driver.close()

# test_TC001.py
#  pytest -v -s test_TC001.py
# pytest -v -s
