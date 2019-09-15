import browser.openChrome as op
import time
from selenium.webdriver.common.keys import Keys

op.driver.get("https://www.amazon.com/")
# For id u need to use '#' symbol
op.driver.find_element_by_css_selector("#twotabsearchtextbox").send_keys("Mac book pro",Keys.ENTER)




time.sleep(3)
