
from selenium import  webdriver
ops = webdriver.ChromeOptions()
ops.add_argument("--disable-notifications")
env =  "mac"

if  env is "win":
    # web = ChromeDriverManager().install()
    path = "..//driver//chromedriver.exe"
    driver = webdriver.Chrome(executable_path=path, options=ops)
    driver.fullscreen_window()
elif env is "mac":

    path = "..//driver//chromedriver"
    driver = webdriver.Chrome(executable_path=path, options=ops)
    driver.fullscreen_window()


import time

driver.get("http://the-internet.herokuapp.com/")

driver.find_element_by_partial_link_text("File Download").click()

time.sleep(2)

path = "/Users/aravindanathdm/Desktop/demo.png"

driver.find_element_by_partial_link_text("demo.png").click()


time.sleep(2)
driver.quit()