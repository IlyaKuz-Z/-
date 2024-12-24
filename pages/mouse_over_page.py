from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class MouseOverPage(BasePage):
    LINK_MOUSE_OVER = (By.XPATH, "//a[contains(text(), 'Click me')]")
    COUNTER_VALUE = (By.ID, "clickCount")

    def open_page(self):
        self.driver.get("http://uitestingplayground.com/mouseover")

    def hover_and_click_multiple_times(self, times=2):
        """
        Основная правка: Находим элемент заново внутри цикла,
        чтобы избежать StaleElementReferenceException.
        """
        for _ in range(times):
            link = self.driver.find_element(*self.LINK_MOUSE_OVER)
            link.click()

    def get_counter_value(self):
        return self.driver.find_element(*self.COUNTER_VALUE).text
