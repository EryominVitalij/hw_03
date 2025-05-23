import pytest
from selene import browser

@pytest.fixture(scope='function', autouse=True)
def browser_window():
    browser.config.window_width = 1900
    browser.config.window_height = 1000
    yield browser
    browser.quit()