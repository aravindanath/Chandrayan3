import browser.openChrome as op
from selenium.webdriver.common.action_chains import ActionChains
import time

op.driver.get("https://www.icicibank.com/")

tgt = op.driver.find_element_by_link_text("Products")
ac = ActionChains(op.driver)
ac.move_to_element(tgt).perform()
time.sleep(2)

tgt2 = op.driver.find_element_by_link_text("Car Loan")
ac.click(tgt2).perform()

time.sleep(2)

op.driver.quit()

