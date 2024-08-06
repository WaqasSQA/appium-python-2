import self
from appium import webdriver
import unittest

from Resource.creds import creds
import HTMLTestRunner
from Pages.loginPage import LoginPage
from Resource.resources import Base
from Pages.changePersonalInfo_action import changePerosnal


class TestCases(unittest.TestCase):

    def setUp(self):
        print("Setup is called")
        self.driver = webdriver.Remote(Base.host, desired_capabilities=Base.desired_cap)

    def test_001_login(self):
        print("Test 1 is called")
        driver = self.driver
        cd = creds()
        login_page = LoginPage(driver)
        login_page.login_actions(cd.phoneNumber, cd.password)

    def test_002_changePersonalINFO(self):
        print("Test 2 is called")
        driver = self.driver
        cd = creds()
        login_page = LoginPage(driver)
        login_page.login_actions(cd.phoneNumber, cd.password)
        change_Personal = changePerosnal(driver)
        change_Personal.changePersonal_Actions()

    def tearDown(self):
        print("Teared Down")

        if __name__ == '__main__':
            unittest.main(testRunner=HTMLTestRunner.__version__(output=Base.HTML_Report_Path))
