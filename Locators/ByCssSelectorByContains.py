import browser.openChrome as op
import time
from selenium.webdriver.common.keys import Keys

op.driver.get("https://www.facebook.com/")
# For contains need to use '*' symbol
op.driver.find_element_by_css_selector("input[type*='mai']").send_keys("aravind")




time.sleep(3)
op.driver.quit()
# input[type='email']