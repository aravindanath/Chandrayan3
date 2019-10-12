import LaunchBrowsers.openBrowser as op
from selenium.webdriver.common.keys import Keys

class Cookies():

    def getCookies(self):

        op.driver.get("https://www.amazon.in")
        op.driver.find_element_by_css_selector("#twotabsearchtextbox").send_keys("iphone xr",Keys.ENTER)
        cookies = op.driver.get_cookies()
        print("No of cookies : "+str(len(cookies)))
        print(cookies)


    def addCookies(self):

        cookie = {'name': 'foo', 'value': 'bar'}

        op.driver.add_cookie(cookie)


    def delCookies(self):
        cookie = {'name': 'foo', 'value': 'bar'}

        op.driver.delete_cookie(cookie)

    def delAllCookies(self):
        op.driver.delete_all_cookies()



    def close(self):
        op.driver.quit()


c =Cookies()
c.getCookies()
c.addCookies()
c.getCookies()
c.delCookies()
c.getCookies()
c.delAllCookies()
c.getCookies()
c.close()