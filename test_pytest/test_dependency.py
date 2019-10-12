


"""

install package called pytest-dependency

pip install pytest-dependency
"""
from selenium import webdriver

import pytest

@pytest.fixture(scope="session")
def setUp():
    global driver
    driver = webdriver.Chrome(executable_path="/Users/aravindanathdm/Documents/Aravinda/chromedriver")
#     After all the test case execution
    yield
    driver.close()


@pytest.mark.run(order = 3)
def test_case_a(setUp):
    driver.get("https://www.amazon.com")


@pytest.mark.run(order = 2)
@pytest.mark.dependency(depends ="test_case_c")
def test_case_b(setUp):
    driver.get("https://www.flipkart.com")


@pytest.mark.run(after ="test_case_c")
def test_case_d(setUp):
    driver.get("https://www.google.com")


@pytest.mark.run(order = 1)
def test_case_c(setUp ):
    driver.get("https://www.yahoo.com")
    assert False


