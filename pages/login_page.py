from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    URL = "https://www.saucedemo.com"
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")

    def open(self):
        self.open_url(self.URL)

    def enter_username(self, username):
        self.enter_text(self.USERNAME_INPUT, username)

    def enter_password(self, password):
        self.enter_text(self.PASSWORD_INPUT, password)

    def click_login(self):
        self.click(self.LOGIN_BUTTON)

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)
