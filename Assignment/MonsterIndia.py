import browser.openChrome as op

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.select import Select

import time

from selenium.webdriver.common.keys import Keys

op.driver.get("https://www.monsterindia.com/")

op.driver.find_element_by_xpath("//span[@class ='mqfihd-user mr5 fs-14']").click()

time.sleep(2)

op.driver.find_element_by_id("signInName").send_keys("")

op.driver.find_element_by_id("password").send_keys("", Keys.ENTER)

time.sleep(2)
op.driver.find_element_by_xpath("//input[@name='fts']").send_keys("Ora")

jobsTitle = op.driver.find_elements_by_xpath("//*[@id='searchForm']/div/div/div[1]/div[2]/div/ul/div/div/div/li")
print("Total count: ", len(jobsTitle))

for job in jobsTitle:


    if job == "Oracle Developer":
        job.click()
        break

op.driver.find_element_by_xpath("//input[@class ='input location_ac']").send_keys("Bengaluru/Bangalore")

time.sleep(2)
op.driver.quit()
