import pytest
from selenium import webdriver

import helpers


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    driver = webdriver
    if request.param == 'chrome':
        driver = webdriver.Chrome()
        driver.get(Urls.BASE_URL)
    if request.param == 'firefox':
        driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def user():
    user = helpers.register_new_user_and_return_test_data()
    yield user
    helpers.delete_user(user["json"]["accessToken"])