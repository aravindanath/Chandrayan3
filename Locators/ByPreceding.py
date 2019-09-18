import LaunchBrowsers.openChrome as op
import time



op.driver.get("https://www.facebook.com")



btn = op.driver.find_elements_by_xpath("//label[text()='Custom']//preceding::input[@type='radio']")
btn[1].click()
time.sleep(2)
op.driver.quit()