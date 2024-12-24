import pytest
import allure
from pages.mouse_over_page import MouseOverPage

@allure.feature("Mouse Over")
@pytest.mark.usefixtures("setup")
class TestMouseOver:

    def test_mouse_over_click(self):
        page = MouseOverPage(self.driver)
        page.open_page()

        # Кликаем по ссылке 3 раза
        page.hover_and_click_multiple_times(times=3)

        # Считываем значение счётчика
        count = page.get_counter_value()

        # Проверяем, что счётчик равен 3
        assert count == "3", f"Счётчик кликов не совпадает. Ожидалось 3, получено: {count}"
