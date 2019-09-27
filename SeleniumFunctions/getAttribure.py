import browser.openChrome as op
import time


op.driver.get("https://temp-mail.org/en/")

email = op.driver.find_element_by_css_selector("#mail").get_attribute("value")

print(email)
time.sleep(2)
op.driver.quit()