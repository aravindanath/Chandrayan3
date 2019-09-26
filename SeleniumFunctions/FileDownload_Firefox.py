
# https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Complete_list_of_MIME_types


from selenium import webdriver

import time

profile = webdriver.FirefoxProfile()
profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/x-gzip,application/zip,application/pdf,	application/vnd.ms-excel")
profile.set_preference("browser.download.folderList", 2)
profile.set_preference("browser.download.manager.showWhenStarting", False)
profile.set_preference("browser.download.dir", '/Users/aravindanathdm/Desktop/')
profile.set_preference("pdfjs.disabled",True)


path = "../driver/geckodriver"
driver = webdriver.Firefox(firefox_profile=profile,executable_path=path)

driver.implicitly_wait(20)
driver.fullscreen_window()

driver.get("https://www.seleniumhq.org/download/")

driver.find_element_by_xpath("//*[@id='mainContent']/table[1]/tbody/tr[1]/td[4]/a").click()


time.sleep(2)
driver.quit()
