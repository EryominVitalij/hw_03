from selene import browser, be, have

def test_01(open_browser):
    browser.element('[name = "q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('html').should(have.text('Об этой странице'))

def test_02(open_browser):
    browser.element('[name="q"]').should(be.blank).type('q12w3e4r5t555').press_enter()
    browser.element('[class="card-section"]').should(have.text('Поиск по запросу q12w3e4r5t555 не принёс результатов.'))

