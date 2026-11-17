from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from pages.base_page import BasePage
import allure

class FeedPage(BasePage):
      # "Выполнено за всё время"
    TOTAL_COMPLETED_COUNTER = (
        By.XPATH,
        "//p[normalize-space()='Выполнено за все время:']"
        "/following-sibling::p[1]"
      )
      # "Выполнено за сегодня"
    TODAY_COMPLETED_COUNTER = (
        By.XPATH,
        "//p[normalize-space()='Выполнено за сегодня:']"
        "/following-sibling::p[1]"
    )
    IN_PROGRESS_ORDERS = (By.XPATH, "//p[normalize-space()='В работе:']/following-sibling::ul[2]")
    TITLE = (By.XPATH, "//h1[normalize-space()='Лента заказов']")

    @allure.step('Дождаться заголовка ленты заказа')
    def wait_for_title(self):
        return self.wait_visible(self.TITLE)

    @allure.step('Получить количество выполненных заказов за все время')
    def get_total(self):
        return int(self.get_text(self.TOTAL_COMPLETED_COUNTER))

    @allure.step('Получить количество выполненных заказов за сегодня')
    def get_today(self):
        return int(self.get_text(self.TODAY_COMPLETED_COUNTER))

    @allure.step('Получить номера заказов в работе')
    def get_in_progress_numbers(self):
        items = self.driver.find_elements(
            By.XPATH,
            self.IN_PROGRESS_ORDERS[1] + '/li'
        )

        return [
            int(item.text.strip())
            for item in items
            if item.text.strip().isdigit()
        ]