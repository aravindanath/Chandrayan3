import pytest
from selenium import webdriver


@pytest.fixture()
def setUp():
    global driver
    driver = webdriver.Chrome(executable_path="/Users/aravindanathdm/Documents/Aravinda/chromedriver")
#     After all the test case execution
    yield
    driver.close()



def test_case_a(setUp):

    driver.get("https://www.amazon.com")


def test_case_b(setUp):

    driver.get("https://www.facebook.com")