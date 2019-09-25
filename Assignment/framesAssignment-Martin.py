import browser.openChrome as op
from selenium.webdriver.common.keys import Keys
import time

url = "https://seleniumhq.github.io/selenium/docs/api/java/"

op.driver.get(url)

# Since the frames are within a frame, setting the focus to the main frame
op.driver.switch_to.frame('packageListFrame')

# Print title of the first frame
print(op.driver.find_element_by_tag_name("title").get_attribute("innerHTML"))

# Click on the first link under the first frame
op.driver.find_element_by_xpath("//a[@href='com/thoughtworks/selenium/package-frame.html']").click()

# Switch focus to main window and then to second frame
op.driver.switch_to.default_content()
op.driver.switch_to.frame('packageFrame')

# print the title of the second frame
print(op.driver.find_element_by_tag_name("title").get_attribute("innerHTML"))

# Click on the first link under second frame
op.driver.find_element_by_xpath("//span[@class='interfaceName' and contains(text(),'CommandProcessor')]").click()

# Switch focus main window and then to third frame
op.driver.switch_to.default_content()
op.driver.switch_to.frame('classFrame')

# print the title of the third frame
print(op.driver.find_element_by_tag_name("title").get_attribute("innerHTML"))

op.driver.quit()