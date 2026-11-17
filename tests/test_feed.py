import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from pages.constructor_page import ConstructorPage
from pages.feed_page import FeedPage
from urls import FEED_URL

@allure.title('Новый заказ увеличивает счетчик за все время')
def test_total_completed_increases(authorized_driver):
    feed = FeedPage(authorized_driver)
    constructor = ConstructorPage(authorized_driver)

    feed.open_url(FEED_URL)
    before = feed.get_total()

    constructor.click_constructor_tab()
    constructor.wait_for_title()
    constructor.drag_first_ingredient()
    constructor.drag_first_filling()
    constructor.wait_for_filling()

    constructor.click_order_button()
    order_number = constructor.get_order_number()
    assert order_number > 0
    constructor.close_popup()

    constructor.click_feed_tab()
    feed.wait_for_title()

    WebDriverWait(authorized_driver, 30).until(lambda _: feed.get_total() > before)
    assert feed.get_total() > before

@allure.title('Новый заказ увеличивает счётчик за сегодня')
def test_today_completed_increases(authorized_driver):
    feed = FeedPage(authorized_driver)
    constructor = ConstructorPage(authorized_driver)

    feed.open_url(FEED_URL)
    before = feed.get_today()

    constructor.click_constructor_tab()
    constructor.wait_for_title()
    constructor.drag_first_ingredient()
    constructor.drag_first_filling()
    constructor.wait_for_filling()

    constructor.click_order_button()
    order_number = constructor.get_order_number()
    assert order_number > 0
    constructor.close_popup()

    constructor.click_feed_tab()
    feed.wait_for_title()

    WebDriverWait(authorized_driver, 30).until(
        lambda _: feed.get_today() > before
    )
    assert feed.get_today() > before

@allure.title('Номер нового заказа появляется в разделе «В работе»')
def test_order_number_appears_in_progress(authorized_driver):
    constructor = ConstructorPage(authorized_driver)
    feed = FeedPage(authorized_driver)

    constructor.wait_for_title()
    constructor.drag_first_ingredient()
    constructor.drag_first_filling()

    try:
        constructor.wait_for_filling()
    except TimeoutException:
        authorized_driver.save_screenshot('filling_error.png')
        raise

    constructor.click_order_button()
    order_number = constructor.get_order_number()
    constructor.close_popup()

    constructor.click_feed_tab()
    feed.wait_for_title()

    WebDriverWait(authorized_driver, 30).until(
        lambda _: order_number in feed.get_in_progress_numbers()
    )
    assert order_number in feed.get_in_progress_numbers()