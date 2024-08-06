from appium.webdriver.common.mobileby import MobileBy
from PageElements.change_perosnal_locators import change_personal_locator
from faker import Faker


class changePerosnal():

    def __init__(self, driver):
        self.driver = driver
        self.accountBtnL = change_personal_locator.accoutnBtnX
        self.personalInfoBtnL = change_personal_locator.personalInfoBtnX
        self.firstNameFieldL = change_personal_locator.firstNameX
        self.lastNameFieldL = change_personal_locator.lastNameX
        self.ethinicityL = change_personal_locator.ethnicityX
        self.ethnicityChooseL = change_personal_locator.ethnicityChooseX
        self.icNumL = change_personal_locator.icNumX
        self.genderL = change_personal_locator.genderX
        self.saveL = change_personal_locator.saveBtnX

    def changePersonal_Actions(self):
        fake_data = Faker()
        randomFirstName = fake_data.name()
        randomLastName = fake_data.name()
        # randomString = fake_data.text(max_nb_chars=6)
        randomAlphaNumeric = fake_data.pystr_format(string_format="??????######")
        self.driver.find_element(MobileBy.XPATH, self.accountBtnL).click()
        self.driver.find_element(MobileBy.XPATH, self.personalInfoBtnL).click()
        self.driver.find_element(MobileBy.XPATH, self.firstNameFieldL).send_keys(randomFirstName)
        self.driver.find_element(MobileBy.XPATH, self.lastNameFieldL).send_keys(randomLastName)
        self.driver.find_element(MobileBy.XPATH, self.ethinicityL).click()
        self.driver.find_element(MobileBy.XPATH, self.ethnicityChooseL).click()
        self.driver.find_element(MobileBy.XPATH, self.icNumL).send_keys(randomAlphaNumeric)
        self.driver.find_element(MobileBy.XPATH, self.genderL).click()
        self.driver.find_element(MobileBy.XPATH, self.saveL).click()
