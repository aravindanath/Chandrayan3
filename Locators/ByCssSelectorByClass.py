import browser.openChrome as op
import time
from selenium.webdriver.common.keys import Keys

op.driver.get("https://www.icicibank.com/")
# For id u need to use '.' symbol
op.driver.find_element_by_css_selector(".pl-login-ornage-box").click()




time.sleep(3)
# input[type='email']