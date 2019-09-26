import browser.openChrome as op
import time

op.driver.get("https://www.hdfcbank.com")
try:
    op.driver.find_element_by_css_selector(".popupCloseButton").click()
except:
    print("NO popup")

win1 = op.driver.current_window_handle
print("First window Page title: ",op.driver.title)

print("First Window id: ",win1)

cur = op.driver.current_url
try:
    if cur == "https://newsite.hdfcbank.com/personal?utm_source=current_website&utm_medium=hp_redirection&utm_campaign=newwebsitecampaign":

        op.driver.get("https://www.hdfcbank.com")
        op.driver.find_element_by_css_selector(".popupCloseButton").click()
except:
        print("Url was correct")

# /Users/aravindanathdm/Documents/Chandrayan3Proj


op.driver.find_element_by_xpath("//*[text()='Login' and @id='loginsubmit']").click()
time.sleep(1)


win2 = op.driver.window_handles

# [CDwindow-508E882670399F5BAEC6C198CE2B7F64,CDwindow-9363CD9A5969597A1BDBE548E8D06CA7]


print("First window:", win2[0] )
print("Second window:", win2[1] )

op.driver.switch_to.window(win2[1])

print("Second win Page title: ",op.driver.title)

op.driver.find_element_by_xpath("/html/body/div[4]/div[2]/div[1]/a").click()
op.driver.close()
time.sleep(2)
op.driver.switch_to.window(win2[0])
print("Page title: ",op.driver.title)
time.sleep(2)
op.driver.quit()