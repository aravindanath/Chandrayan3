# .SeleniumFunctions/praticepage.html


import browser.openChrome as op
import time
from selenium.webdriver.support.select import Select



class DeSelect():

    def selectByVisibleText(self):

        op.driver.get("file:///Users/aravindanathdm/Documents/Chandrayan3Proj/SeleniumFunctions/praticepage.html")
        fruit = op.driver.find_element_by_css_selector("#multiple-select-example")

        sel = Select(fruit)
        sel.select_by_visible_text("Apple")
        sel.select_by_visible_text("Orange")
        sel.select_by_visible_text("Peach")


    def deSelect(self):
        fruit = op.driver.find_element_by_css_selector("#multiple-select-example")

        de = Select(fruit)
        time.sleep(2)
        de.deselect_by_visible_text("Orange")
        time.sleep(2)
        de.select_by_visible_text("Orange")
        time.sleep(2)
        de.deselect_all()
        time.sleep(2)



    def close(self):
         op.driver.quit()


d= DeSelect()

d.selectByVisibleText()
d.deSelect()
d.close()