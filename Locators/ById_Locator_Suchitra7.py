import browser.openChrome as op
import time
from selenium.webdriver.common.keys import Keys
op.driver.get("https://www.amazon.com")
op.driver.find_element_by_id("twotabsearchtextbox").send_keys("iphone 11 pro",Keys.ENTER)
time.sleep(5)
op.driver.quit()