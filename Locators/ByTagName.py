import browser.openChrome as op
import time

op.driver.get("https://www.google.com")

links = op.driver.find_elements_by_tag_name("a")

print("Total no of links: ",len(links))

for link in links:
    print(link.text,"--->" , link.get_attribute("href"))



op.driver.quit()