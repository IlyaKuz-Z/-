import allure
from pages.login_page import LoginPage


@allure.feature("Функциональность логина")
@allure.story("Попытка входа с пустыми данными")
@allure.severity(allure.severity_level.CRITICAL)
@allure.testcase("TMS-003", "Попытка входа с пустыми данными")
@allure.title("Тест-кейс: Вход с пустым логином и паролем")
def test_login_with_empty_fields(driver):
    login_page = LoginPage(driver)

    with allure.step("Открыть страницу логина"):
        login_page.open()

    with allure.step("Проверить, что поля логина и пароля пустые"):
        assert login_page.is_username_empty(), "Поле логина не пустое!"
        assert login_page.is_password_empty(), "Поле пароля не пустое!"

    with allure.step("Нажать на кнопку логина"):
        login_page.click_login()

    with allure.step("Проверить, что отображается сообщение об ошибке"):
        error_message = login_page.get_error_message()
        assert error_message == "Epic sadface: Password is required", \
            "Сообщение об ошибке некорректное!"
