import allure

from pages.base_page import BasePage
from locators.feed_locators import FeedLocators


class FeedPage(BasePage):
    @allure.step('Дождаться заголовка ленты заказов')
    def wait_for_title(self):
        return self.wait_visible(FeedLocators.TITLE)

    @allure.step('Получить количество выполненных заказов за всё время')
    def get_total(self):
        return int(self.get_text(FeedLocators.TOTAL_COMPLETED_COUNTER))

    @allure.step('Получить количество выполненных заказов за сегодня')
    def get_today(self):
        return int(self.get_text(FeedLocators.TODAY_COMPLETED_COUNTER))

    @allure.step('Дождаться увеличения счётчика заказов за всё время')
    def wait_for_total_increase(self, before):
        return self.wait_until(lambda: self.get_total() > before)

    @allure.step('Дождаться увеличения счётчика заказов за сегодня')
    def wait_for_today_increase(self, before):
        return self.wait_until(lambda: self.get_today() > before)

    @allure.step('Получить номера заказов в работе')
    def get_in_progress_numbers(self):
        texts = self.get_texts(FeedLocators.IN_PROGRESS_ORDER_ITEMS)
        return [int(text.strip()) for text in texts if text.strip().isdigit()]

    @allure.step('Дождаться заказа {order_number} в разделе «В работе»')
    def wait_for_order_in_progress(self, order_number):
        return self.wait_until(lambda: order_number in self.get_in_progress_numbers())
