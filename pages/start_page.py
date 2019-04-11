from appium.webdriver.common.touch_action import TouchAction
from webdriver import driver


class StartPage(driver.Driver):
    def __init__(self):
        pass

    def login(self):
        login_text = self.driver.find_element_by_id("com.twitter.android:id/detail_text")
        login_text_x = login_text.location['x'] + login_text.size['width'] - 5
        login_text_y = login_text.location['y'] + (login_text.size['height'] / 2)
        TouchAction(self.driver).tap(None, login_text_x, login_text_y, 1).perform()
