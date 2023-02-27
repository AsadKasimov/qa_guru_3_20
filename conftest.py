import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selene import browser
from pydantic import BaseModel
import os
from dotenv import load_dotenv


@pytest.fixture(scope='session', autouse=True)
def data_search():
    load_dotenv()

    class Settings(BaseModel):
        load_dotenv()
        HAHAHA: str = os.getenv("HAHAHA")
        accessKey: str = os.getenv("ACCESSKEY")

    env_vars = Settings()
    options = UiAutomator2Options().load_capabilities({
        "app": "bs://c700ce60cf13ae8ed97705a55b8e022f13c5827c",
        "platformVersion": "9.0",
        "deviceName": "Google Pixel 3",
        'bstack:options': {
            "projectName": "First Python project",
            "buildName": "browserstack-build-1",
            "sessionName": "BStack first_test",
            "userName": env_vars.HAHAHA,
            "accessKey": env_vars.accessKey
        }
    })

    browser.config.driver = webdriver.Remote("http://hub.browserstack.com/wd/hub", options=options)

    yield

    browser.quit()
