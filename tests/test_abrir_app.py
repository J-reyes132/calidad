from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import unittest

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Android',
    appPackage='com.amaze.filemanager',
    appActivity='com.amaze.filemanager.ui.activities.MainActivity',
)

appium_server_url = "http://127.0.0.1:4723"

class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))

    def test_abrir_app(self) -> None:

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//android.widget.Button[@resource-id="com.android.packageinstaller:id/permission_allow_button"]')))

        self.driver.find_element(by=AppiumBy.ID, value='com.android.packageinstaller:id/permission_allow_button').click()

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@resource-id="com.amaze.filemanager:id/fullpath"]')))
        assert self.driver.find_element(by=AppiumBy.ID, value='com.amaze.filemanager:id/fullpath').text == '/storage/emulated/0'

if __name__ == '__main__':
    unittest.main()