from selenium import webdriver as driver
import time
class ScreenShots():


    def take_Screenshot_A(self,driver):
        fileName = str(round(time.time() * 1000)) + ".png"
        dir = "/Users/aravindanathdm/Desktop/"
        driver.save_screenshot(dir+fileName)


    def take_ScreenShot_B(self,driver):
        fileName = str(round(time.time() * 1000)) + ".png"
        dir = "/Users/aravindanathdm/Desktop/"
        driver.get_screenshot_as_file(dir+fileName)


