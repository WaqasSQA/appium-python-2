import unittest


from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy




desired_cap = dict(
    deviceName='emulator-5554',
    platformName='Android',
    automationName='UiAutomator2',
    app='C:\\Users\\dev\\Desktop\\HVIE APKS\\24 August\\Uat 24 AUG.apk'

    # Other Capabilities
)

driver = webdriver.Remote("http://127.0.0.1:4723", desired_cap)

driver.find_element(MobileBy.XPATH, "//android.widget.Button[@text='Allow']").click()


