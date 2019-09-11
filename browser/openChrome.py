
from selenium import  webdriver

ops = webdriver.ChromeOptions()
ops.add_argument("--disable-notifications")
driver =  webdriver.Chrome(executable_path="../driver/chromedriver",options=ops)
driver.fullscreen_window()



