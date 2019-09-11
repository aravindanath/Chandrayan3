import browser.openChrome as op
import time

op.driver.get("https://www.icicibank.com/")
op.driver.find_element_by_class_name("pl-login-ornage-box").click()

time.sleep(2)
op.driver.quit()

