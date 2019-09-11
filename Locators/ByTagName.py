import browser.openChrome as op
import time

op.driver.get("https://www.google.com")

links = op.driver.find_elements_by_tag_name("a");

print("Total no of links ",len(links))


for lin in links:

    print(lin.text)
    print(lin.get_attribute("href"))

time.sleep(3)

op.driver.quit()