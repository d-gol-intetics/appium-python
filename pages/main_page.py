from appium.webdriver.common.mobileby import MobileBy
from webdriver import driver


class MainPage(driver.Driver):
    def __init__(self):
        self.home_tab_button = (MobileBy.ACCESSIBILITY_ID, "Home Tab")

    def is_home_tab_selected(self):
        return self.find_element(self.home_tab_button).is_selected()
