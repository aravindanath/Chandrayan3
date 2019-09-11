import browser.openChrome as op
import time
from selenium.webdriver.common.keys import Keys


op.driver.get("https://www.google.com")

op.driver.find_element_by_link_text("മലയാളം").click()
time.sleep(2)


op.driver.find_element_by_name("q").send_keys("onam",Keys.ENTER)


time.sleep(2)
op.driver.find_element_by_xpath("//div[contains(text(),'ഓണം - വിക്കിപീഡിയ')]").click()

time.sleep(3)
op.driver.quit()
