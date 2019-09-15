import browser.openChrome as op
import time
from selenium.webdriver.common.keys import Keys
op.driver.get("https://www.google.com")
op.driver.find_element_by_name("q").send_keys("selenium jobs in Bangalore",Keys.ENTER)
time.sleep(5)
op.driver.back()
op.driver.find_element_by_name("q").send_keys("python jobs in bangalore",Keys.ENTER)
time.sleep(5)
op.driver.quit()
