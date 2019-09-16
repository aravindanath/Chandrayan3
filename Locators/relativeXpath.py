import browser.openChrome as op
from selenium.webdriver.common.keys import Keys
import time

op.driver.get("https://www.google.com")
#                /html/body/div/div[4]/form/div[2]/div/div/div/div[2]/input
op.driver.find_element_by_xpath("//input[@name='q']").send_keys("Selenium openings in bangalore",Keys.ENTER)

time.sleep(2)
op.driver.quit()