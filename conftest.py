import pytest
from selenium.common.exceptions import TimeoutException
from pages.constructor_page import ConstructorPage
from selenium import webdriver
from api_helpers import generate_user, register_user, delete_user
from urls import BASE_URL

def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome', help='Browser to run tests: chrome or firefox')

@pytest.fixture
def driver(request):
    browser = request.config.getoption('--browser')

    if browser == 'chrome':
        options = webdriver.ChromeOptions()
        options.page_load_strategy = 'eager'
        driver = webdriver.Chrome(options=options)
    elif browser == 'firefox':
        options = webdriver.FirefoxOptions()
        options.page_load_strategy = 'eager'
        driver = webdriver.Firefox(options=options)
    else:
        raise ValueError(f'Unsupported browser: {browser}')

    driver.set_window_size(1440, 1100)
    driver.set_page_load_timeout(45)

    yield driver

    driver.quit()

@pytest.fixture
def registered_user():
    payload = generate_user()
    response = register_user(payload)
    assert response.status_code == 200

    data = response.json()

    yield data

    delete_response = delete_user(data['accessToken'])
    assert delete_response.status_code == 202

@pytest.fixture
def authorized_driver(driver, registered_user):
    driver.get(BASE_URL)

    driver.execute_script(
        """
        localStorage.setItem('accessToken', arguments[0]);
        localStorage.setItem('refreshToken', arguments[1]);
        """,
        registered_user['accessToken'],
        registered_user['refreshToken']
    )

    try:
        driver.refresh()
    except TimeoutException:
        driver.execute_script('window.stop();')

    page = ConstructorPage(driver)
    page.wait_for_order_button()

    return driver