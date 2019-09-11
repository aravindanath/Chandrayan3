import browser.openChrome as op

import time

from selenium.webdriver.common.keys import Keys

op.driver.get("https://www.google.com")

op.driver.find_element_by_partial_link_text("Imag").click()

op.driver.find_element_by_name("q").send_keys("North Carolina",Keys.ENTER)

time.sleep(2)


op.driver.quit()


