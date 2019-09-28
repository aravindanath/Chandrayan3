import browser.openChrome as op
import time
from datetime import datetime

class DemoScreenShots():

    def screenshots(self):
        op.driver.get("https://www.amazon.com")
        stamp = str(round(time.time()))
        date = str(datetime.now())
        st = date.replace("-", "_").replace(" ", "_").replace(":", "_").split(".")[0]

        op.driver.save_screenshot("./demo"+st+".png")
        op.driver.quit()



    def takeScreenShot(self):
        fileName = str(round(time.time() * 1000)) + ".png"
        dir = "/Users/aravindanathdm/Desktop/"
        op.driver.save_screenshot()

d =DemoScreenShots()
d.screenshots()