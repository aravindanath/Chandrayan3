import browser.openChrome as op

import time


op.driver.get("https://www.amazon.in")

op.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

time.sleep(3)
op.driver.quit()