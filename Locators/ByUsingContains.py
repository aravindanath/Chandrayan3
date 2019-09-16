
import browser.openChrome as op
from selenium.webdriver.common.keys import Keys
import time

op.driver.get("http://demo.guru99.com/payment-gateway/index.php")

time.sleep(3)

op.driver.find_element_by_xpath("//*[contains(@value,'B')]").click()

val = op.driver.find_element_by_xpath("//font[2][contains(text(),'$')]").text
print("Amount", val)
time.sleep(3)
op.driver.quit()

#