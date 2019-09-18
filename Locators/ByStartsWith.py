import LaunchBrowsers.openChrome as op
import time



op.driver.get("https://www.facebook.com")
# input[id^='u_0_'] stats with css
val = op.driver.find_elements_by_xpath("//input[starts-with(@id,'u_0_')]")


print("No of elements", len(val))
#
val[11].click()
time.sleep(2)

for v in val:
    print(v.get_attribute("name"))


op.driver.quit()