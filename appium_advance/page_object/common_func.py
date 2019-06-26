import time

from appium_advance.page_object.baseView import BaseView
from appium_advance.page_object.desired_caps import appium_desired
import logging
from selenium.webdriver.common.by import By
class Common(BaseView):
    cancelBtn=(By.ID,"android:id/button2")
    skipBtn = (By.ID,"com.tal.kaoyan:id/tv_skip")
    def check_cancelBtn(self):
        logging.info("=========check_cancelBtn=======")
        try:
            cancelBtn=self.driver.find_element(*self.cancelBtn)
        except Exception:
            logging.info("no cancelBtn")
        else:
            logging.info("click cancelBtn")
            cancelBtn.click()

    def check_skipBtn(self):
        logging.info("=========check_skipBtn=======")
        try:
            skipBtn=self.driver.find_element(*self.skipBtn)
        except Exception:
            logging.info("no skipBtn")
        else:
            logging.info("click cancelBtn")
            skipBtn.click()

if __name__ == '__main__':
    driver=appium_desired()
    comm=Common(driver)
    comm.check_cancelBtn()
    time.sleep(3)
    comm.check_skipBtn()