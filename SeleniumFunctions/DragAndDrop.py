import browser.openChrome as op
from selenium.webdriver.common.action_chains import ActionChains
import time

op.driver.get("http://demo.guru99.com/test/drag_drop.html")

src = op.driver.find_element_by_xpath("(//*[@id='fourth']/a)[1]")

des =  op.driver.find_element_by_xpath("//*[@id='amt7']")

ac = ActionChains(op.driver)
ac.drag_and_drop(src,des).perform()

# Context click is for right click
ac.context_click(src).perform()


time.sleep(2)
op.driver.quit()