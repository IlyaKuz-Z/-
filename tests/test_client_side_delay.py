import pytest
import allure
from pages.client_side_delay_page import ClientSideDelayPage

@allure.feature("Client Side Delay")
@pytest.mark.usefixtures("setup")
class TestClientSideDelay:

    def test_client_side_delay(self):
        page = ClientSideDelayPage(self.driver)

        # 1) Открываем страницу
        page.open_page()

        # 2) Кликаем по кнопке
        page.click_on_trigger_button()

        # 3) Ждём появления текста "Data calculated on the client side."
        text = page.wait_for_data(timeout=15)

        # 4) Проверка
        assert "Data calculated on the client side." in text, \
            f"Ожидаемый текст не найден. Фактический: {text}"
