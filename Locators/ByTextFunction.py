import browser.openChrome as op


op.driver.get("https://www.facebook.com")
# //span[contains(text(),'Create an')]

title= op.driver.find_element_by_xpath("//span[text()='Create an account']").text

print(title)

op.driver.quit()