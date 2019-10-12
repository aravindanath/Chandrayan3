
import pytest
from selenium import webdriver 

a = 1
@pytest.mark.skipif(a>100, reason="Skip")
def test_case_a():
    driver = webdriver.Chrome(executable_path="/Users/aravindanathdm/Documents/Aravinda/chromedriver")
    driver.get("https://www.amazon.com")

def test_case_b():
    driver = webdriver.Chrome(executable_path="/Users/aravindanathdm/Documents/Aravinda/chromedriver")
    driver.get("https://www.facebook.com")