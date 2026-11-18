from pages.base_page import BasePage
import allure
from locators.feed_locators import FeedLocators


class FeedPage(BasePage):
    @allure.step('Дождаться заголовка ленты заказа')
    def wait_for_title(self):
        return self.wait_visible(FeedLocators.TITLE)

    @allure.step('Получить количество выполненных заказов за все время')
    def get_total(self):
        return int(self.get_text(FeedLocators.TOTAL_COMPLETED_COUNTER))

    @allure.step('Получить количество выполненных заказов за сегодня')
    def get_today(self):
        return int(self.get_text(FeedLocators.TODAY_COMPLETED_COUNTER))

    @allure.step('Получить номера заказов в работе')
    def get_in_progress_numbers(self):
        items = self.driver.find_elements(*FeedLocators.IN_PROGRESS_ORDER_ITEMS)

        return [
            int(item.text.strip())
            for item in items
            if item.text.strip().isdigit()
        ]
