import browser.openChrome as op
import time


op.driver.get("https://mail.rediff.com/cgi-bin/login.cgi")

op.driver.find_element_by_css_selector("input[name='proceed']").click()
time.sleep(2)
# alert = op.driver.switch_to_alert()
alert =  op.driver.switch_to.alert
print(alert.text)

alert.accept()

op.driver.find_element_by_css_selector("#login1").send_keys("arvind@rediffmail.com")


op.driver.get("http://the-internet.herokuapp.com/javascript_alerts")

time.sleep(2)

op.driver.find_element_by_xpath("//button[text()='Click for JS Alert']").click()
print(alert.text)
alert.accept()

time.sleep(2)

op.driver.find_element_by_xpath("//button[text()='Click for JS Confirm']").click()
print(alert.text)
alert.dismiss()

result = op.driver.find_element_by_css_selector("#result").text

print("Result: ",result)


time.sleep(2)


op.driver.find_element_by_xpath("//button[text()='Click for JS Prompt']").click()
print(alert.text)
time.sleep(2)
alert.send_keys("Hello guys.. ")
time.sleep(2)
alert.accept()

result = op.driver.find_element_by_css_selector("#result").text

print("Result: ",result)


time.sleep(2)


op.driver.quit()