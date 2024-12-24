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