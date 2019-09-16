import browser.openChrome as op
from selenium.webdriver.common.keys import Keys
import time

op.driver.get("https://www.google.com")

time.sleep(3)
#
try:
   ok =  op.driver.find_element_by_xpath("//a[text()='No, thanks']")
   if ok.is_displayed():
       ok.click()

except:
    print("Privacy alert did not appear!")

op.driver.find_element_by_xpath("//input[@name='q']").send_keys("Selenium openings in bangalore",Keys.ENTER)

time.sleep(2)
op.driver.quit()