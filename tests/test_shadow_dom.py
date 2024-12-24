import pytest
import allure
import pyperclip
import time
from pages.shadow_dom_page import ShadowDomPage
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

# @allure.feature("Shadow DOM Clipboard")
# @pytest.mark.usefixtures("setup")
class TestShadowDomClipboard:
    def test_generate_and_copy_local_clipboard(self):
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=options)
        # page = ShadowDomPage(self.driver)
        # page.open_page()
        #
        # # Генерация GUID
        # page.click_generate_button()
        # generated_guid = page.get_input_value()
        # assert generated_guid, "GUID не был сгенерирован!"

        driver.get("http://uitestingplayground.com/shadowdom")
        # time.sleep(20)

        host = driver.find_element(By.CSS_SELECTOR, "guid-generator")
        shadow_root = host.shadow_root  # Может не работать, если драйвер не поддерживает

        generate_button = shadow_root.find_element(By.CSS_SELECTOR, "#buttonGenerate")
        generate_button.click()

        # generate_button = driver.find_element(By.ID, "buttonGenerate")
        # generate_button.click()
        edit_field = driver.find_element(By.ID, "editField").get_attribute("value")
        clone_icon = driver.find_element(By.CLASS_NAME, "fa-clone")
        copy_value = clone_icon.click()
        assert edit_field == copy_value

        driver.quit()
        # Копирование
        # page.click_copy_button()
        #
        # # Считываем буфер обмена из ОС
        # clipboard_text = pyperclip.paste()
        #
        # # Сравниваем
        # assert clipboard_text == generated_guid, \
        #     f"GUID в буфере обмена не совпадает: {clipboard_text} vs {generated_guid}"
