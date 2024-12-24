import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class TestSauceDemo:
    @pytest.fixture(scope="function")
    def driver(self):
        """Fixture для создания и закрытия драйвера"""

        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")


        try:
            service = Service(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=chrome_options)
        except Exception as e:

            print(f"Ошибка при установке ChromeDriver: {e}")
            driver = webdriver.Chrome(options=chrome_options)

        driver.maximize_window()
        driver.get("https://www.saucedemo.com")
        yield driver
        driver.quit()


    VALID_USERS = [
        'standard_user',
        'problem_user',
        'performance_glitch_user'
    ]

    def test_invalid_password(self, driver):
        """
        TestCase_1: Тест с некорректным паролем
        """

        username = self.VALID_USERS[0]


        username_input = driver.find_element(By.ID, "user-name")
        password_input = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.ID, "login-button")


        username_input.send_keys(username)
        password_input.send_keys("incorrect_password")
        login_button.click()


        error_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "error-message-container"))
        )

        assert driver.current_url == "https://www.saucedemo.com/", "URL должен остаться прежним"
        assert "Epic sadface: Username and password do not match any user in this service" in error_message.text
        assert "error" in error_message.get_attribute("class")

    def test_empty_password(self, driver):
        """
        TestCase_2: Тест с пустым паролем
        """

        username = self.VALID_USERS[0]


        username_input = driver.find_element(By.ID, "user-name")
        login_button = driver.find_element(By.ID, "login-button")


        username_input.send_keys(username)
        login_button.click()


        error_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "error-message-container"))
        )

        assert driver.current_url == "https://www.saucedemo.com/", "URL должен остаться прежним"
        assert "Epic sadface: Password is required" in error_message.text
        assert "error" in error_message.get_attribute("class")

    @pytest.mark.parametrize("username", VALID_USERS)
    def test_successful_login(self, driver, username):
        """
        TestCase_3: Параметризованный тест успешной авторизации
        """

        username_input = driver.find_element(By.ID, "user-name")
        password_input = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.ID, "login-button")


        username_input.send_keys(username)
        password_input.send_keys("secret_sauce")
        login_button.click()


        WebDriverWait(driver, 10).until(
            EC.url_to_be("https://www.saucedemo.com/inventory.html")
        )


        assert driver.current_url == "https://www.saucedemo.com/inventory.html", f"Не удалось авторизоваться под пользователем {username}"

# Требования к зависимостям:
# pytest
# selenium
# webdriver-manager
# import allure
# from selenium.webdriver.common.by import By
#
# class LoginPage:
#     def __init__(self, driver):
#         self.driver = driver
#         self.url = "https://www.saucedemo.com"
#         self.username_input = (By.ID, "user-name")
#         self.password_input = (By.ID, "password")
#         self.login_button = (By.ID, "login-button")
#         self.error_message = (By.CSS_SELECTOR, "h3[data-test='error']")
#
#     @allure.step("Открыть страницу логина")
#     def open(self):
#         self.driver.get(self.url)
#         return self
#
#     @allure.step("Проверить, что открыта страница логина")
#     def is_opened(self):
#         return self.driver.current_url == self.url
#
#     @allure.step("Проверить, что поле логина пустое")
#     def check_username_empty(self):
#         return self.driver.find_element(*self.username_input).get_attribute("value") == ""
#
#     @allure.step("Проверить, что поле пароля пустое")
#     def check_password_empty(self):
#         return self.driver.find_element(*self.password_input).get_attribute("value") == ""
#
#     @allure.step("Нажать кнопку Login")
#     def click_login(self):
#         self.driver.find_element(*self.login_button).click()
#         return self
#
#     @allure.step("Проверить сообщение об ошибке")
#     def get_error_message(self):
#         error_element = self.driver.find_element(*self.error_message)
#         return {
#             'text': error_element.text,
#             'background_color': error_element.value_of_css_property('background-color')
#         }
#
# @allure.feature("Login Functionality")
# @allure.story("Empty Credentials Login Attempt")
# def test_empty_credentials_login(driver):
#     login_page = LoginPage(driver)
#
#     with allure.step("Открываем страницу логина"):
#         login_page.open()
#         assert login_page.is_opened(), "Страница логина не открылась"
#
#     with allure.step("Проверяем, что поля пустые"):
#         assert login_page.check_username_empty(), "Поле логина не пустое"
#         assert login_page.check_password_empty(), "Поле пароля не пустое"
#
#     with allure.step("Пытаемся залогиниться"):
#         login_page.click_login()
#         assert login_page.is_opened(), "Произошел переход со страницы логина"
#
#     with allure.step("Проверяем сообщение об ошибке"):
#         error = login_page.get_error_message()
#         assert error['text'] == "Epic sadface: Password is required", "Неверное сообщение об ошибке"
#         # Проверка на красный фон (rgba(226, 35, 26, 1) - примерное значение красного цвета)
#         assert "rgba(226, 35, 26" in error['background_color'], "Фон сообщения об ошибке не красный"