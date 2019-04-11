from appium.webdriver.common.mobileby import MobileBy
from webdriver import driver


class LoginPage(driver.Driver):

    def __init__(self):
        self.username_editbox = (MobileBy.ID, 'com.twitter.android:id/login_identifier')
        self.password_editbox = (MobileBy.ID, 'com.twitter.android:id/login_password')
        self.login_button = (MobileBy.ID, 'com.twitter.android:id/login_login')

    def login(self, username, password):
        self.find_element(self.username_editbox).send_keys(username)
        self.find_element(self.password_editbox).send_keys(password)
        self.find_element(self.login_button).click()
