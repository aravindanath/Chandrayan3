from sharedFunctions import openChrome as op
from selenium.webdriver.common.keys import Keys
import time

url = "https://seleniumhq.github.io/selenium/docs/api/java/"

op.driver.get(url)

op.driver.switch_to.frame('packageListFrame')
# Click on the first link under the default frame
op.driver.find_element_by_xpath("//a[@href='com/thoughtworks/selenium/package-frame.html']").click()

# print the title of the default frame
# title = op.driver.find_element_by_xpath("//frame[@title='All Packages']").text
# print("Title of the first frame is: ",title)

# Switch focus to second frame
#op.driver.switch_to_frame('packageFrame')

# secondFrame = op.driver.find_element_by_xpath("//frame[@name='packageFrame']")
# op.driver.switch_to_frame(secondFrame)

frameTwo = op.driver.find_element_by_tag_name('frame')[1]
op.driver.switch_to_frame(frameTwo)

# Click on the first link under second frame
op.driver.find_element_by_xpath("//span[@class='interfaceName' and contains(text(),'CommandProcessor')]").click()

# print the title of the second frame
# title = op.driver.find_element_by_xpath("//frame[@name='packageFrame']").text
# print("Title of the second frame is: ",title)

# Switch focus to third frame
thirdFrame = op.driver.find_element_by_xpath("//frame[@name='classFrame']")
op.driver.switch_to_frame(thirdFrame)

op.driver.find_element_by_xpath("//a[contains(@href,'HttpCommandProcessor.html')]").click()

# print the title of the forth frame
# title = op.driver.find_element_by_xpath("//frame[contains(@title, 'Package, class and')]").text
# print("Title of the third frame is: ",title)

op.driver.quit()