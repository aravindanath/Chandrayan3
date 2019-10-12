from selenium import webdriver
import pytest

# @pytest.mark.hello
def test_case_a():
    driver = webdriver.Chrome(executable_path="/Users/aravindanathdm/Documents/Aravinda/chromedriver")
    driver.get("https://www.facebook.com")
    assert driver.title == "Login"
#     Facebook – log in or sign up


# @pytest.mark.hello
def test_case_b():
    driver = webdriver.Chrome(executable_path="/Users/aravindanathdm/Documents/Aravinda/chromedriver")
    driver.get("https://www.facebook.com")
    assert driver.current_url == "https://www.facebook.com/"
#     Facebook – log in or sign up


# pytest -k test_assertion.py -v -s