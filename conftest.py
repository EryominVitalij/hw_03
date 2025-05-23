import pytest
from selene import browser

@pytest.fixture(scope="session")
def browser_window():
    browser.config.window_width = 640
    browser.config.window_height = 480
    yield browser
    browser.quit()


@pytest.fixture
def open_browser(browser_window):
    browser_window.open('https://google.com')