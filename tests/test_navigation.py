import allure

from pages.constructor_page import ConstructorPage
from pages.feed_page import FeedPage
from urls import BASE_URL, FEED_URL


class TestNavigation:
    @allure.title('Переход в ленту заказов')
    def test_open_order_feed(self, driver):
        page = ConstructorPage(driver)
        feed = FeedPage(driver)
        page.open_url(BASE_URL)
        page.click_feed_tab()
        feed.wait_for_title()
        page.wait_for_url(FEED_URL)

        assert page.get_current_url() == FEED_URL

    @allure.title('Переход из ленты заказов в конструктор')
    def test_open_constructor(self, driver):
        page = ConstructorPage(driver)
        page.open_url(FEED_URL)
        page.click_constructor_tab()
        page.wait_for_title()
        page.wait_for_url(BASE_URL)

        assert page.get_current_url().rstrip('/') == BASE_URL
