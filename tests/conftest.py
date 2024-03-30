import pytest
from selene import browser


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
