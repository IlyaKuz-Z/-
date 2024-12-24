import pytest
import allure
from pages.ajax_data_page import AjaxDataPage


@allure.feature("AJAX Data")
@pytest.mark.usefixtures("setup")
class TestAjaxData:

    def test_ajax_data_load(self):
        page = AjaxDataPage(self.driver)
        page.open_page()

        # Нажимаем на кнопку
        page.click_ajax_button()

        # Ждём появления текста, увеличив таймаут до 15
        text = page.wait_for_text_appearance(timeout=15)

        assert "Data loaded with AJAX get request" in text, "Текст после AJAX-загрузки не найден!"
