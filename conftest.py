import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Выберите браузер: chrome или firefox"
    )


@pytest.fixture(scope="class")
def setup(request):
    browser = request.config.getoption("--browser")
    driver = None

    try:
        if browser == "chrome":
            service = ChromeService(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service)
        elif browser == "firefox":
            service = FirefoxService(GeckoDriverManager().install())
            driver = webdriver.Firefox(service=service)
        else:
            raise ValueError(f"Browser '{browser}' не поддерживается")

        driver.maximize_window()
        request.cls.driver = driver
        yield driver

    except Exception as e:
        print(f"Произошла ошибка при настройке драйвера: {e}")
        raise
    finally:
        if driver:
            driver.quit()