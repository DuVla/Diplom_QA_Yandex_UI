from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import ElementClickInterceptedException
from pages.base_page import BasePage
import allure
from locators.constructor_locators import ConstructorLocators


class ConstructorPage(BasePage):
    @allure.step('Открыть вкладку "Конструктор"')
    def click_constructor_tab(self):
        self.click_element(ConstructorLocators.CONSTRUCTOR_TAB)

    @allure.step('Открыть вкладку "Лента заказов"')
    def click_feed_tab(self):
        self.click_element(ConstructorLocators.FEED_TAB)

    @allure.step('Кликнуть по первому ингредиенту')
    def click_first_ingredient(self):
        self.click_element(ConstructorLocators.INGREDIENT_ITEM)

    @allure.step('Проверить, что попап с деталями ингредиента открыт')
    def is_popup_visible(self):
        return self.wait_visible(ConstructorLocators.POPUP)

    @allure.step('Закрыть окно и дождаться исчезновения оверлея')
    def close_popup(self):
        def click_close(driver):
            try:
                self.wait_visible(ConstructorLocators.POPUP_CLOSE_BUTTON).click()
                return True
            except ElementClickInterceptedException:
                return False

        WebDriverWait(self.driver, self.TIMEOUT).until(click_close)
        self.wait_invisible(ConstructorLocators.POPUP)

        return WebDriverWait(self.driver, self.TIMEOUT).until(
            lambda driver: all(
                not overlay.is_displayed()
                for overlay in driver.find_elements(*ConstructorLocators.MODAL_OVERLAYS)
            )
        )

    @allure.step('Получить значение счетчика ингредиента')
    def get_ingredient_counter(self):
        return int(self.get_text(ConstructorLocators.INGREDIENT_COUNTER))

    @allure.step('Дождать заголовка конструктора')
    def wait_for_title(self):
        return self.wait_visible(ConstructorLocators.TITLE)

    @allure.step('Перетащить ингредиент в конструктор')
    def drag_ingredient(self, locator):
        self.wait_visible(locator)
        ingredient = self.scroll_to_element(locator)
        drop_area = self.wait_visible(ConstructorLocators.DROP_AREA)

        self.driver.execute_script("""
            const source = arguments[0];
            const target = arguments[1];
            const dataTransfer = new DataTransfer();

            source.dispatchEvent(new DragEvent('dragstart', {
                bubbles: true, dataTransfer
            }));
            target.dispatchEvent(new DragEvent('dragenter', {
                bubbles: true, dataTransfer
            }));
            target.dispatchEvent(new DragEvent('dragover', {
                bubbles: true, cancelable: true, dataTransfer
            }));
            target.dispatchEvent(new DragEvent('drop', {
                bubbles: true, cancelable: true, dataTransfer
            }));
            source.dispatchEvent(new DragEvent('dragend', {
                bubbles: true, dataTransfer
            }));
        """, ingredient, drop_area)

    def drag_first_ingredient(self):
        self.drag_ingredient(ConstructorLocators.INGREDIENT_ITEM)

    def drag_first_filling(self):
        self.drag_ingredient(ConstructorLocators.FILLING_ITEM)

    @allure.step('Дождаться кнопки оформления заказа')
    def wait_for_order_button(self):
        return self.wait_visible(ConstructorLocators.ORDER_BUTTON)

    @allure.step('Дождаться начинки в составе бургера')
    def wait_for_filling(self):
        return self.wait_visible(ConstructorLocators.FILLING_IN_CONSTRUCTOR)

    @allure.step('Оформить заказ')
    def click_order_button(self):
        self.click_element(ConstructorLocators.ORDER_BUTTON)

    @allure.step('Дождаться номера созданного заказа')
    def get_order_number(self):
        def number_is_ready(driver):
            text = self.get_text(ConstructorLocators.ORDER_NUMBER).strip()

            if not text.isdigit():
                return False

            number = int(text)
            if number in (0, 9999):
                return False

            return number

        return WebDriverWait(self.driver, 30).until(number_is_ready)

    @allure.step('Получить заголовок окна деталей ингредиента')
    def get_popup_title(self):
        return self.get_text(ConstructorLocators.POPUP_TITLE)
