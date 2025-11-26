import os
import pytest
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils import allure_attach

# Явно загружаем .env из корня проекта
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))


@pytest.fixture(scope='function')
def setup_browser():
    # Берём секреты из .env
    user = os.getenv("SELENOID_USER")
    password = os.getenv("SELENOID_PASS")
    host = os.getenv("SELENOID_HOST")
    port = os.getenv("SELENOID_PORT")
    browser_version = os.getenv("BROWSER_VERSION")

    selenoid_url = f"https://{user}:{password}@{host}/wd/hub"

    options = Options()
    options.set_capability("browserName", "chrome")
    options.set_capability("browserVersion", browser_version)
    options.set_capability("selenoid:options", {
        "enableVNC": True,
        "enableVideo": True
    })

    driver = webdriver.Remote(
        command_executor=selenoid_url,
        options=options
    )

    yield driver

    # Аттачменты
    allure_attach.add_screenshot(driver)
    allure_attach.add_logs(driver)
    allure_attach.add_html(driver)
    allure_attach.add_video(driver)

    driver.quit()
