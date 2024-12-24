from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class AjaxDataPage(BasePage):
    BUTTON_TRIGGER = (By.ID, "ajaxButton")
    LABEL_LOADED_TEXT = (By.XPATH, "//div[@id='content']/p")

    def open_page(self):
        self.driver.get("http://uitestingplayground.com/ajax")

    def click_ajax_button(self):
        self.driver.find_element(*self.BUTTON_TRIGGER).click()

    def wait_for_text_appearance(self, timeout=15):
        wait = WebDriverWait(self.driver, timeout)
        element = wait.until(EC.visibility_of_element_located(self.LABEL_LOADED_TEXT))
        return element.text
