
import browser.openChrome as op

from selenium.webdriver.common.keys import Keys
import time

op.driver.get("https://www.amazon.com")

op.driver.find_element_by_id("twotabsearchtextbox").send_keys("Mac book pro",Keys.ENTER)
time.sleep(2)

op.driver.close()

