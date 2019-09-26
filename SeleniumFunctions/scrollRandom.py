import browser.openChrome as op

import time


op.driver.get("https://www.amazon.in")


op.driver.execute_script("window.scrollBy(0,3000)","")

time.sleep(2)
op.driver.quit()