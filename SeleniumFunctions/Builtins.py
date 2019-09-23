import browser.openChrome as op
from selenium.webdriver.common.keys import Keys
import time

op.driver.fullscreen_window()
op.driver.get("https://www.google.com")
print("Current url :  ",op.driver.current_url)
op.driver.find_element_by_name("q").send_keys("Selenium jobs",Keys.ENTER)


pageTitle = op.driver.title

print("Page title is", pageTitle)
time.sleep(2)
op.driver.back()
time.sleep(2)
op.driver.forward()
print("Current url :  ",op.driver.current_url)
op.driver.refresh()
time.sleep(2)
print(op.driver.page_source)
op.driver.quit()

