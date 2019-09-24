import browser.openChrome as op
import time

op.driver.get("http://the-internet.herokuapp.com/")

op.driver.find_element_by_partial_link_text("Inputs").click()

time.sleep(2)

op.driver.find_element_by_xpath("//input[@type='number']").send_keys("1345134134")


time.sleep(2)
op.driver.quit()