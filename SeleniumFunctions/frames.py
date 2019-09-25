import browser.openChrome as op

url = "https://seleniumhq.github.io/selenium/docs/api/java/"

op.driver.get(url)

op.driver.switch_to.frame('packageListFrame')
# Click on the first link under the default frame
op.driver.find_element_by_xpath("//a[@href='com/thoughtworks/selenium/package-frame.html']").click()


op.driver.switch_to.default_content()

op.driver.switch_to.frame("packageFrame")
# Click on the first link under second frame
op.driver.find_element_by_xpath("//span[@class='interfaceName' and contains(text(),'CommandProcessor')]").click()

op.driver.switch_to.default_content()
op.driver.switch_to.frame("classFrame")
op.driver.find_element_by_xpath("//a[contains(@href,'HttpCommandProcessor.html')]").click()

op.driver.quit()