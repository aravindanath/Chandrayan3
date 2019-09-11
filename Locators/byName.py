import browser.openChrome as op
from selenium.webdriver.common.keys import Keys
import time

op.driver.get("https://www.google.com")

searchBox = op.driver.find_element_by_name("q")

searchBox.send_keys("Selenium python jobs",Keys.ENTER)


time.sleep(2)
op.driver.back()
searchBox = op.driver.find_element_by_name("q")

searchBox.send_keys("Selenium 4 ",Keys.ENTER)


time.sleep(2)
op.driver.quit()