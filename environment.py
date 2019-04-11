from webdriver import driver
from pages import start_page
from pages import login_page
from pages import main_page


def before_all(context):
    context.driver = driver.Driver()
    context.start_page = start_page.StartPage()
    context.login_page = login_page.LoginPage()
    context.main_page = main_page.MainPage()


def after_all(context):
    context.browser.quit()
