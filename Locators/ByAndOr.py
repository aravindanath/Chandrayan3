import LaunchBrowsers.openChrome as op

op.driver.get("https://www.facebook.com")

val = op.driver.find_elements_by_xpath("//input[@type='radio' and @name='sex']")

print("Count of radio btn", len(val))
op.driver.quit()