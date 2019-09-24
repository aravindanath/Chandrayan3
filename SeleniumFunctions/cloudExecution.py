import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
"""
https://cloud.seetest.io
"""

class examplePython(unittest.TestCase):
    dc = {}
    testName = 'Quick Start Chrome Browser Demo'
    driver = None

    def setUp(self):
        self.dc['testName'] = self.testName
        self.dc['browserName'] = "chrome"
        self.dc['browserVersion'] = "76.0.3809.132"
        self.dc['platform'] = "WINDOWS 10"
        self.dc['accessKey'] = "PLEASE ADD YOUR KEY"
        self.driver = webdriver.Remote('https://cloud.seetest.io/wd/hub', self.dc)

    def testExperitest(self):
            self.driver.get("http://www.google.in")
            WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.NAME, 'q')))
            searchBar = self.driver.find_element_by_name('q')
            searchBar.click()
            searchBar.send_keys('selenium jobs in bangalore')
            searchBar.send_keys(Keys.ENTER)

    def tearDown(self):
        print ('Report URL: ' + self.driver.capabilities["reportUrl"])
        self.driver.quit()

    if __name__ == '__main__':
        unittest.main()