from selene import browser, be, have

def test_01():
    browser.open('https://google.com')
    browser.element('[name = "q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('html').should(have.text('Об этой странице'))

# по google не получилось выполнить поиск абракадабры, капча мешается, как обойти пока не понимаю

def test_02():
    browser.open('https://www.bing.com/')
    browser.element('[name="q"]').should(be.blank).type('pokjQW87888').press_enter()
    browser.element('[id="b_results"]').should(have.text('Не удалось найти ни одного результата для pokjQW87888'))

