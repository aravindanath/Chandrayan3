import browser.openChrome as op
import time

op.driver.get("https://www.w3schools.com/code/tryit.asp?filename=G84J2AFMX1BD")

# Text() function
op.driver.find_element_by_xpath("//button[contains(text(),'Run »')]").click()
time.sleep(2)
op.driver.switch_to.frame("iframeResult")
# @Text Attribute
op.driver.find_element_by_xpath("//a[@text='hello']").click()

time.sleep(2)
op.driver.switch_to.default_content()
time.sleep(1)
op.driver.find_element_by_xpath("//button[contains(text(),'Run »')]").click()
time.sleep(2)
op.driver.quit()