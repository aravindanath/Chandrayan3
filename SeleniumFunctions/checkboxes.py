import browser.openChrome as op
import time

op.driver.get("http://the-internet.herokuapp.com/")

op.driver.find_element_by_partial_link_text("Checkboxes").click()

time.sleep(2)

cb = op.driver.find_elements_by_xpath("//input[@type='checkbox']")

print("No of Checkbox", len(cb))
for c in cb:
    if c.is_selected():
        print("Cb is already selected!")
    else:
        c.click()

time.sleep(2)
op.driver.quit()