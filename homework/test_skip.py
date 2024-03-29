"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import pytest
from selene import browser, query


@pytest.fixture(params=[('1920', '1080'), ('1024', '768'), ('800', '600')], scope="function")
def browser_config(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    if int(width) > 800:
        yield "desktop"
    else:
        yield "mobile"

    browser.quit()


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
