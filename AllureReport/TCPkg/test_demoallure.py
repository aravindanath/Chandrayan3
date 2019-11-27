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
@pytest.mark.run(order=1)
def test_case_a(setUp):
    with allure.step("Google search"):
        allure.title("Test case google.com")
        driver.get("https://www.google.com")
        logger.info("User is on google.com")
        logger.info(driver.current_url)
        logger.info(driver.get_cookies())
        allure.attach(driver.get_screenshot_as_png(),"Success msg ",allure.attachment_type.PNG)


@allure.step
@pytest.mark.skip(reason="Skipping..")
def test_case_b(setUp):
    with allure.step("Facebook login"):
        logger.info("User is entering URL")
        driver.get("https://www.facebook.com")
        assert driver.title == "Facebook"
        allure.attach(driver.get_screenshot_as_png(), "Sceenshot of this screen", allure.attachment_type.PNG)
        logger.info("User is on "+driver.current_url)


@allure.step
@pytest.mark.run(order=2)
def test_case_c(setUp):
    with allure.step("Facebook login"):
        logger.info("User is entering URL")
        driver.get("https://www.facebook.com")
        allure.attach(driver.get_screenshot_as_png(), "Sceenshot of this screen", allure.attachment_type.PNG)
        logger.info("User is on " + driver.current_url)
        logger.info(driver.title)
        assert driver.title == "Facebook"

