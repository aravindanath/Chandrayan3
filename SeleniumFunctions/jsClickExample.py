import browser.openChrome as op

import time



class JSClick():

    def openUrl(self):

        op.driver.get("https://www.amazon.in")


    def scroll(self):

        btt= op.driver.find_element_by_xpath("//*[text()='Back to top']")
        JSClick.scrollTillEnd(self)
        JSClick.jsClick(self,btt)


    def close(self):
        op.driver.quit()

    def jsClick(self,element):
        op.driver.execute_script("arguments[0].click()", element)


    def scrollTillEnd(self):
        op.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")




j = JSClick()
j.openUrl()
j.scroll()
j.close()