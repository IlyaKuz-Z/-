from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time

class ProgressBarPage(BasePage):
    BUTTON_START = (By.ID, "startButton")
    BUTTON_STOP = (By.ID, "stopButton")
    PROGRESS_LABEL = (By.ID, "progressBar")

    def open_page(self):
        self.driver.get("http://uitestingplayground.com/progressbar")

    def click_start(self):
        self.driver.find_element(*self.BUTTON_START).click()

    def click_stop(self):
        self.driver.find_element(*self.BUTTON_STOP).click()

    def get_progress_value(self):
        return self.driver.find_element(*self.PROGRESS_LABEL).text

    def run_progress_and_stop_at_value(self, stop_value=75):
        self.click_start()
        while True:
            current_value = int(self.get_progress_value().replace("%", ""))
            if current_value >= stop_value:
                self.click_stop()
                break
            time.sleep(0.2)
        return current_value
