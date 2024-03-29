"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""
import pytest
from selene import browser, query


@pytest.fixture(params=[('1920', '1080'), ('1024', '768'), ('1152', '864')], scope="function")
def browser_config_desktop(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    yield
    browser.quit()


@pytest.fixture(params=[('800', '600'), ('810', '610'), ('850', '650')], scope="function")
def browser_config_mobile(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    yield
    browser.quit()


def test_github_desktop(browser_config_desktop):
    browser.open('https://github.com/')
    browser.open(browser.element('.HeaderMenu-link--sign-in').get(query.attribute("href")))
    pass


def test_github_mobile(browser_config_mobile):
    browser.open('https://github.com/')
    browser.element('.Button-content').click()
    browser.open(browser.element('.HeaderMenu-link--sign-in').get(query.attribute("href")))
    pass