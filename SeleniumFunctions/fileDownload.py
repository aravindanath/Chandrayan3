import browser.openChrome as op
import time

op.driver.get("http://the-internet.herokuapp.com/")

op.driver.find_element_by_partial_link_text("File Download").click()

time.sleep(2)

path = "/Users/aravindanathdm/Desktop/demo.png"

op.driver.find_element_by_partial_link_text("demo.png").click()


time.sleep(2)
op.driver.quit()