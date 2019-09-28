import LaunchBrowsers.openBrowser as op
from selenium.webdriver.common.by import By
import time

class AutoSuggestion():

    def autoComplete(self):
        baseUrl = 'https://www.redbus.in/'
        op.driver.get(baseUrl)
        op.driver.implicitly_wait(10)


        # From Destination
        op.driver.find_element_by_xpath("//*[@id='src']").send_keys("Goa")

        list= op.driver.find_elements(By.XPATH,"//ul[@class='autoFill']")
        pickupPoint = "Madgaon, Goa"
        for pickList in list:
            print(pickList.text)
            op.driver.find_element_by_xpath("//ul[@class='autoFill']//li[text()='" + pickupPoint + "']").click()

        # TO Destination
        op.driver.find_element_by_css_selector("#dest").send_keys("Hubli")

        listDrp =  op.driver.find_elements_by_xpath("//ul[@class='autoFill']")
        drop = "Hubli"

        for droplist in listDrp:
            print(droplist.text)
            op.driver.find_elements_by_xpath("//ul[@class='autoFill']//li[text()='" + drop + "']")




#         Calender
        op.driver.find_element_by_xpath("//*[@class='fl search-box date-box gtm-onwardCalendar']").click()


        deptDate = op.driver.find_elements(By.XPATH, "//div[@id='rb-calendar_onward_cal']/table[1]//td")

        for d in deptDate:

            if d.text == '29':
                d.click()
                break;

#         Return

        op.driver.find_element(By.XPATH,"//*[@class='fl search-box date-box gtm-returnCalendar']").click()



        try:
            returnDate = op.driver.find_elements_by_xpath("//*[@id='rb-calendar_return_cal']/table/tbody/tr/td")
            for rd in returnDate:
                if rd.text == "Sept 2019":
                    op.driver.find_element_by_xpath("(//td[@class='next'])[2]").click()
                    time.sleep(4)
                    break
        except:
            print("Sep not found")

        returnDates = op.driver.find_elements_by_xpath("//*[@id='rb-calendar_return_cal']/table/tbody/tr/td")
        for rd in returnDates:
            if rd.text == "31":
                rd.click()
                break;

        op.driver.find_element_by_css_selector("#search_btn").click()
        time.sleep(4)
        op.driver.close()

a= AutoSuggestion()
a.autoComplete()
