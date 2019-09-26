from selenium.webdriver import Chrome
from selenium import webdriver
import time

path = "../driver/chromedriver"
option_set = webdriver.ChromeOptions()
option_set.add_argument('disable-infobars')
option_set.add_argument('--disable-notifications')
prefs = {"download.default_directory" : "/Users/aravindanathdm/Desktop/"}
option_set.add_experimental_option("prefs",prefs)

driver = Chrome(options=option_set,executable_path=path)

driver.implicitly_wait(20)
driver.fullscreen_window()
driver.get("https://www.seleniumhq.org/download/")

driver.find_element_by_xpath("//*[@id='mainContent']/table[1]/tbody/tr[1]/td[4]/a").click()

time.sleep(2)
driver.quit()