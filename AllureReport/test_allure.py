import pytest
from selenium import webdriver
import allure
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


@pytest.fixture()
def setUp():
    global driver
    driver = webdriver.Chrome(executable_path="/Users/aravindanathdm/Documents/Aravinda/chromedriver")
#     After all the test case execution
    yield
    driver.close()


@allure.step
def test_case_a(setUp):
    with allure.step("Amazon login"):
        allure.title("Test case amzxon.com")
        driver.get("https://www.amazon.com")
        logger.info("User is on amazon.com")
        logger.info(driver.current_url)
        logger.info(driver.get_cookies())
        allure.attach(driver.get_screenshot_as_png(),"Success msg ",allure.attachment_type.PNG)


@allure.step
def test_case_b(setUp):
    with allure.step("Facebook login"):

        logger.info("User is entering URL")
        driver.get("https://www.facebook.com")
        allure.attach(driver.get_screenshot_as_png(), "Sceenshot of this screen", allure.attachment_type.PNG)
        logger.info("User is on "+driver.current_url)

# /Users/aravindanathdm/PycharmProjects/PythonSeleniumProject/allureReport/=/Users/aravindanathdm/Documents/class/Python Selenium/Reports

# allureReport/StepsForAllureReport
# /Users/aravindanathdm/Documents/class/Python Selenium/Reports

# --vv --capture=fd --alluredir = /Users/aravindanathdm/Documents/class/Python Selenium/Reports


# pytest test_allure.py --verbose --capture=fd --alluredir "/demo/Users/aravindanathdm/Documents/class/Python Selenium/allureReport/demo/Reports"

