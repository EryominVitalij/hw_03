from selene import browser, be, have

def test_01(open_browser):
    browser.element('[name = "q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('html').should(have.text('Об этой странице'))

def test_02(open_browser):
    browser.element('[name="q"]').should(be.blank).type('Йцукенгшщзхъ').press_enter()
    browser.element('[class="card-section"]').should(have.text('Поиск по запросу Йцукенгшщзхъ не принёс результатов.'))

