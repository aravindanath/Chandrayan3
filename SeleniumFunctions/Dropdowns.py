import browser.openChrome as op
import time
from selenium.webdriver.support.select import Select


class DropDown():


    def selectBySendKeys(self):
        op.driver.get("https://www.wikipedia.org/")
        time.sleep(2)
        op.driver.find_element_by_css_selector("#searchLanguage").send_keys("हिन्दी")
        time.sleep(2)

    def selectByVisibleText(self):
        # op.driver.get("https://www.wikipedia.org/")
        time.sleep(2)
        lang = op.driver.find_element_by_css_selector("#searchLanguage")
        sel = Select(lang)
        sel.select_by_visible_text("Bahasa Indonesia")
        time.sleep(2)


    def selectByIndex(self):
        # op.driver.get("https://www.wikipedia.org/")
        time.sleep(2)
        lang = op.driver.find_element_by_css_selector("#searchLanguage")
        sel = Select(lang)
        sel.select_by_index(37)
        time.sleep(2)


    def selectByValue(self):
        # op.driver.get("https://www.wikipedia.org/")
        time.sleep(2)
        lang = op.driver.find_element_by_css_selector("#searchLanguage")
        sel = Select(lang)
        sel.select_by_value("ja")
        time.sleep(2)




    def close(self):

        op.driver.quit()



d =  DropDown()
d.selectBySendKeys()

d.selectByVisibleText()
d.selectByIndex()
d.selectByValue()

d.close()
