import browser.openChrome as op
import time
from selenium.webdriver.common.keys import Keys

op.driver.get("https://www.icicibank.com/")
op.driver.find_element_by_class_name("pl-login-ornage-box").click()

time.sleep(3)
op.driver.quit()