import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.constructor_page import ConstructorPage
from urls import BASE_URL, FEED_URL
from pages.feed_page import FeedPage


class TestNavigation:
    @allure.title('Переход в ленту заказов')
    def test_open_order_feed(self, driver):
        page = ConstructorPage(driver)
        page.open_url(BASE_URL)
        page.click_feed_tab()

        WebDriverWait(driver, 10).until(EC.url_to_be(FEED_URL))

        feed_page = FeedPage(driver)
        assert feed_page.wait_for_title().is_displayed()
        assert page.get_current_url() == FEED_URL

    @allure.title('Переход из ленты заказов в конструктор')
    def test_open_construcktor(self, driver):
        page = ConstructorPage(driver)
        page.open_url(FEED_URL)
        page.click_constructor_tab()

        assert page.wait_for_title().is_displayed()
        assert page.get_current_url().rstrip('/') == BASE_URL
