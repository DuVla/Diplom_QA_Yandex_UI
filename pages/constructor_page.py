import allure

from pages.base_page import BasePage
from locators.constructor_locators import ConstructorLocators


class ConstructorPage(BasePage):
    @allure.step('Открыть вкладку «Конструктор»')
    def click_constructor_tab(self):
        self.click_element(ConstructorLocators.CONSTRUCTOR_TAB)

    @allure.step('Открыть вкладку «Лента заказов»')
    def click_feed_tab(self):
        self.click_element(ConstructorLocators.FEED_TAB)

    @allure.step('Открыть детали булки «Краторная булка N-200i»')
    def click_ingredient(self):
        self.click_element(ConstructorLocators.INGREDIENT_ITEM)

    @allure.step('Проверить видимость окна деталей ингредиента')
    def is_popup_visible(self):
        return self.is_visible(ConstructorLocators.POPUP)

    @allure.step('Закрыть окно и дождаться исчезновения оверлея')
    def close_popup(self):
        self.click_element(ConstructorLocators.POPUP_CLOSE_BUTTON)
        self.wait_invisible(ConstructorLocators.POPUP)
        self.wait_all_invisible(ConstructorLocators.MODAL_OVERLAYS)

    @allure.step('Проверить, что окно деталей ингредиента закрыто')
    def is_popup_closed(self):
        return (
            self.are_all_invisible(ConstructorLocators.POPUP)
            and self.are_all_invisible(ConstructorLocators.MODAL_OVERLAYS)
        )

    @allure.step('Получить счётчик булки «Краторная булка N-200i»')
    def get_ingredient_counter(self):
        return int(self.get_text(ConstructorLocators.INGREDIENT_COUNTER))

    @allure.step('Дождаться увеличения счётчика ингредиента')
    def wait_for_counter_increase(self, before):
        return self.wait_until(lambda: self.get_ingredient_counter() > before)

    @allure.step('Дождаться заголовка конструктора')
    def wait_for_title(self):
        return self.wait_visible(ConstructorLocators.TITLE)

    @allure.step('Добавить булку «Краторная булка N-200i»')
    def drag_bun(self):
        self.drag_and_drop(ConstructorLocators.INGREDIENT_ITEM, ConstructorLocators.DROP_AREA)

    @allure.step('Добавить начинку «Хрустящие минеральные кольца»')
    def drag_filling(self):
        self.drag_and_drop(ConstructorLocators.FILLING_ITEM, ConstructorLocators.DROP_AREA)

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
        return self.wait_for_number(ConstructorLocators.ORDER_NUMBER, excluded_numbers=(0, 9999))

    @allure.step('Получить заголовок окна деталей ингредиента')
    def get_popup_title(self):
        return self.get_text(ConstructorLocators.POPUP_TITLE)
