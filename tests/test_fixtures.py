"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""

from selene import browser, query


def test_github_desktop(browser_config_desktop):
    browser.open('https://github.com/')
    browser.open(browser.element('.HeaderMenu-link--sign-in').get(query.attribute("href")))
    pass


def test_github_mobile(browser_config_mobile):
    browser.open('https://github.com/')
    browser.element('.Button-content').click()
    browser.open(browser.element('.HeaderMenu-link--sign-in').get(query.attribute("href")))
    pass
