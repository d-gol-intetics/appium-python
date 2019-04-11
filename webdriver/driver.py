from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium import webdriver


class Driver(object):

    # desired_caps = {
    #     'platformName': 'android',
    #     'deviceName': 'device',
    #     'udid': 'emulator-5554',
    #     'appPackage': 'com.twitter.android',
    #     'appActivity': 'com.twitter.android.StartActivity'
    # }

    desired_caps = {
        "platformName": "android",
        "deviceName": "device",
        "appPackage": "com.twitter.android",
        "appActivity": "com.twitter.android.StartActivity",
        "noReset": "true"
    }

    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
    timeout = 20
    driver.implicitly_wait(timeout)

    def find_element(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(locator))

    def close(self):
        self.driver.quit()
