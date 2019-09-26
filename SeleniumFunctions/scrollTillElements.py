import browser.openChrome as op

import time


op.driver.get("https://www.amazon.in")

btt= op.driver.find_element_by_xpath("//*[text()='Back to top']")



op.driver.execute_script("arguments[0].scrollIntoView();",btt)

time.sleep(2)
btt.click()
time.sleep(2)
op.driver.quit()