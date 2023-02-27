from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


def test_search():
    browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
    browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).send_keys("BrowserStack")
    browser.all((AppiumBy.CLASS_NAME, "android.widget.TextView")).should(have.size_greater_than(0))


def test_search_volkswagen():
    browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
    browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).send_keys("volkswagen")
    browser.all((AppiumBy.CLASS_NAME, "android.widget.TextView")).should(have.size_greater_than(0))
