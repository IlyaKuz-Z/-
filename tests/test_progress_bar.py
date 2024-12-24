import pytest
import allure
from pages.progress_bar_page import ProgressBarPage

@allure.feature("Progress Bar")
@pytest.mark.usefixtures("setup")
class TestProgressBar:

    def test_progress_bar_stop(self):
        page = ProgressBarPage(self.driver)
        page.open_page()

        # Останавливаем прогресс на значении, например, 75%
        final_value = page.run_progress_and_stop_at_value(stop_value=75)

        # Проверяем что прогресс не ушел дальше 100% (или как условие)
        assert final_value <= 100, f"Прогресс превысил 100%: {final_value}"
