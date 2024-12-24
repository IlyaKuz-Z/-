from pages.base_page import BasePage

class ShadowDomPage(BasePage):

    def open_page(self):
        self.driver.get("http://uitestingplayground.com/shadowdom")

    def click_generate_button(self):
        """
        Нажимаем кнопку «шестерёнка» #buttonGenerate (генерация нового GUID).
        """
        script = """
        const host = document.querySelector('guid-generator');
        const shadowRoot = host.shadowRoot;
        const generateBtn = shadowRoot.querySelector('#buttonGenerate');
        if (generateBtn) generateBtn.click();
        """
        self.driver.execute_script(script)

    def click_copy_button(self):
        """
        Нажимаем кнопку копирования (иконка с буфером).
        Предположим, она имеет id="#buttonCopy" (проверьте в DevTools).
        """
        script = """
        const host = document.querySelector('guid-generator');
        const shadowRoot = host.shadowRoot;
        const copyBtn = shadowRoot.querySelector('#buttonCopy');
        if (copyBtn) copyBtn.click();
        """
        self.driver.execute_script(script)

    def get_input_value(self):
        """
        Возвращаем текущее значение поля #editField.
        Например: "9e37d62d-a637-47a2-bce1-5dd03b887bd5"
        """
        script = """
        const host = document.querySelector('guid-generator');
        const shadowRoot = host.shadowRoot;
        const inputField = shadowRoot.querySelector('#editField');
        return inputField ? inputField.value : '';
        """
        return self.driver.execute_script(script)

    def get_clipboard_text_js(self):
        """
        Пытаемся прочитать буфер обмена средствами JS:
        return navigator.clipboard.readText()

        ВАЖНО: это может не сработать в незащищённом (HTTP) окружении
        или в некоторых браузерах без дополнительных разрешений.
        """
        script = """
        return navigator.clipboard.readText();
        """
        # execute_script не может напрямую возвращать промис,
        # поэтому придётся либо использовать_async, либо
        # сделать небольшой "хак" для ожидания промиса:
        # Но самый простой способ — pyperclip (см. ниже).
        return self.driver.execute_script(script)
