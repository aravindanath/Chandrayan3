import browser.openChrome as op
import time

op.driver.get("http://the-internet.herokuapp.com/")

op.driver.find_element_by_partial_link_text("File Upload").click()

time.sleep(2)

path = "/Users/aravindanathdm/Desktop/demo.png"

op.driver.find_element_by_id("file-upload").send_keys(path)


time.sleep(2)

op.driver.find_element_by_css_selector("#file-submit").click()
time.sleep(2)
op.driver.quit()