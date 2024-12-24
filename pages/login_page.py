from pages.base_page import BasePage
from selenium.webdriver.common.by import By

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.saucedemo.com"
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.error_message = (By.CLASS_NAME, "error-message-container")

    @allure.step("Открыть страницу логина")
    def open(self):
        self.driver.get(self.url)

    @allure.step("Ввод логина: {username}")
    def enter_username(self, username):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.username_input)
        ).send_keys(username)

    @allure.step("Ввод пароля: {password}")
    def enter_password(self, password):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.password_input)
        ).send_keys(password)

    @allure.step("Нажать кнопку Login")
    def click_login(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.login_button)
        ).click()

    @allure.step("Получение сообщения об ошибке")
    def get_error_message(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.error_message)
        ).text
