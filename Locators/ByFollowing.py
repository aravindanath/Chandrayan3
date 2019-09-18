import LaunchBrowsers.openChrome as op
import time



op.driver.get("https://www.facebook.com")


op.driver.find_element_by_xpath("//input[@id='pass']//following::label/input").click()

time.sleep(2)
op.driver.quit()