"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import pytest
from selene import browser, query


def test_mobile_skip(browser_config):
    if browser_config == "mobile":
        pytest.skip("Это мобильное разрешение")
    browser.open('https://github.com/')
    browser.open(browser.element('.HeaderMenu-link--sign-in').get(query.attribute("href")))


def test_desktop_skip(browser_config):
    if browser_config == "desktop":
        pytest.skip("Это десктопное разрешение")
    browser.open('https://github.com/')
    browser.element('.Button-content').click()
    browser.open(browser.element('.HeaderMenu-link--sign-in').get(query.attribute("href")))
