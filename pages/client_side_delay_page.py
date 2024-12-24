from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class ClientSideDelayPage(BasePage):
    BUTTON_TRIGGER = (By.ID, "ajaxButton")  # кнопка "Button Triggering Client Side Logic"

    def open_page(self):
        self.driver.get("http://uitestingplayground.com/clientdelay")

    def click_on_trigger_button(self):
        # Находим и кликаем по кнопке
        self.driver.find_element(*self.BUTTON_TRIGGER).click()

    def wait_for_data(self, timeout=15):
        """
        Ждём появления текста:
        <p class="bg-success">Data calculated on the client side.</p>
        """
        wait = WebDriverWait(self.driver, timeout)
        element = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "p.bg-success"))
        )
        return element.text
