# import LaunchBrowsers.openBrowser as op
#
# from selenium import webdriver as op
import selenium.webdriver as driver


"""
https://www.w3schools.com/jsref/met_win_scrollto.asp
"""

class Scroll():

    def scrollByPixcel(self,driver,pixcel):
        driver.execute_script("window.scrollBy(0,"+pixcel+")","")

    def scrollByElement(self,driver,element):
        driver.execute_script("arguments[0].scrollIntoView();",element)

    def scrollTillEnd(self,driver):
        driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

    def colourElement(self,driver,element,colour="yellow"):
        driver.execute_script("arguments[0].style.border = '3px solid "+colour+"'", element)