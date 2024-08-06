from appium.webdriver.common.mobileby import MobileBy
from PageElements.login_locators import Locators


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.allowBtnL = Locators.allowBtnX
        self.closeBtnL = Locators.closeBtnX
        self.loginFirstBtnL = Locators.firstLoginX
        self.phoneNumFieldL = Locators.numFieldX
        self.passwordFieldL = Locators.passFieldX
        self.finalLoginBtnL = Locators.loginBtnX

    def login_actions(self, username, password):

        self.driver.find_element(MobileBy.XPATH, self.allowBtnL).click()

        self.driver.find_element(MobileBy.XPATH, self.closeBtnL).click()

        self.driver.find_element(MobileBy.XPATH, self.loginFirstBtnL).click()

        self.driver.find_element(MobileBy.XPATH, self.phoneNumFieldL).send_keys(username)

        self.driver.find_element(MobileBy.XPATH, self.passwordFieldL).send_keys(password)

        self.driver.find_element(MobileBy.XPATH, self.finalLoginBtnL).click()
