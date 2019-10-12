import browser.openChrome as op
from selenium.webdriver.common.keys import Keys
import time

class Cookies():

    def getCookies(self):
        op.driver.get("https://www.amazon.in")

        cookies = op.driver.get_cookies()
        print("No of cookies before search : " + str(len(cookies)))
        print(cookies)
        op.driver.find_element_by_css_selector("#twotabsearchtextbox").send_keys("iphone xr", Keys.ENTER)
        cookies = op.driver.get_cookies()
        print("No of cookies after search  : " + str(len(cookies)))
        print(cookies)

    def addCookies(self):
        op.driver.get("https://www.amazon.in")
        cookie = {'name': 'arvind', 'value': 'bar','domain':"www.amazon.in"}
        op.driver.add_cookie(cookie)
        cookies = op.driver.get_cookies()
        print("No of cookies before search : " + str(len(cookies)))
        print(cookies)

    def delCookies(self):
        op.driver.get("https://www.amazon.in")
        cookie = {'name': 'arvind', 'value': 'bar','domain':"www.amazon.in"}
        op.driver.delete_cookie(cookie)

    def delAllCookies(self):
        op.driver.get("https://www.amazon.in")
        op.driver.delete_all_cookies()
        cookies = op.driver.get_cookies()
        print("No of cookies before search : " + str(len(cookies)))
        print(cookies)


    def getSpecificValueFromCookies(self):
        op.driver.get("https://www.amazon.in")
        cookies = op.driver.get_cookies()
        print("No of cookies before search : " + str(len(cookies)))
        print(cookies)
        op.driver.find_element_by_css_selector("#twotabsearchtextbox").send_keys("iphone xr", Keys.ENTER)
        cookies_list = op.driver.get_cookies()
        # Empty dict
        cookies_dict = {}
        for cookie in cookies_list:
            cookies_dict[cookie['name']] = cookie['value']

        print("Session: ",cookies_dict["session-token"])


    def close(self):
        op.driver.close()

c =  Cookies()
c.getCookies()
# c.delCookies()
c.close()