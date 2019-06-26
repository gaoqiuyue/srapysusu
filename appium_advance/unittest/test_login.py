from appium_advance.unittest.myunit import StartEnd
from appium_advance.page_object.loginView import LoginView
import unittest
import logging

class TestLogin(StartEnd):
    def test_login_test1(self):
        logging.info("====test_login_test1========")
        l=LoginView(self.driver)
        l.login_action("苏苏","20182018")

    def test_login_test2(self):
        logging.info("====test_login_test2========")
        l = LoginView(self.driver)
        l.login_action("苏苏2", "201820182")

    def test_login_test3(self):
        logging.info("====test_login_test3========")
        l = LoginView(self.driver)
        l.login_action("苏苏3", "201820183")
if __name__ == '__main__':
    unittest.main()