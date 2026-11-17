from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.common.exceptions import ElementClickInterceptedException
from pages.base_page import BasePage
import allure

class ConstructorPage(BasePage):
    CONSTRUCTOR_TAB = (By.XPATH,
                       "//a[@href='/' and .//p[normalize-space()='Конструктор']]"
                       )
    TITLE = (By.XPATH,
             "//h1[normalize-space()='Соберите бургер']"
             )
    FEED_TAB = (By.XPATH, "//a[@href='/feed']")
    INGREDIENT_ITEM = (By.XPATH,
                       "(//a[starts-with(@href, '/ingredient/')])[1]")
    POPUP = (
        By.XPATH,
        "//section[contains(@class, 'Modal_modal_opened')]"
        "//div[contains(@class, 'Modal_modal__container')]"
    )
    POPUP_CLOSE_BUTTON = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]"
        "//button[contains(@class, 'Modal_modal__close')]")
    INGREDIENT_COUNTER = (By.XPATH, "(//a[starts-with(@href, '/ingredient/')])[1]"
        "//p[contains(@class, 'counter_counter__num')]")
    DROP_AREA = (By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket__')]"
    )

    ORDER_BUTTON = (By.XPATH, "//button[normalize-space()='Оформить заказ']")
    FILLING_ITEM = (By.XPATH,
                    "//h2[normalize-space()='Начинки']/following-sibling::ul[1]/a[1]"
    )
    FILLING_IN_CONSTRUCTOR = (By.XPATH,
                              "//section[contains(@class, 'BurgerConstructor_basket__')]"
                              "//span[normalize-space()='Хрустящие минеральные кольца']"
                              )
    ORDER_NUMBER = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]"
        "//h2[contains(@class, 'Modal_modal__title_shadow')]" )

    @allure.step('Открыть вкладку "Конструктор"')
    def click_constructor_tab(self):
        self.click_element(self.CONSTRUCTOR_TAB)

    @allure.step('Открыть вкладку "Лента заказов"')
    def click_feed_tab(self):
        self.click_element(self.FEED_TAB)

    @allure.step('Кликнуть по первому ингредиенту')
    def click_first_ingredient(self):
        self.click_element(self.INGREDIENT_ITEM)

    @allure.step('Проверить, что попап с деталями ингредиента открыт')
    def is_popup_visible(self):
        return self.wait_visible(self.POPUP)

    @allure.step('Закрыть попап ингредиента')
    def close_popup(self):
        def click_close(driver):
            try:
                self.wait_visible(self.POPUP_CLOSE_BUTTON).click()
                return True
            except ElementClickInterceptedException:
                return False

        WebDriverWait(self.driver, 10).until(click_close)
        return self.wait_invisible(self.POPUP)

    @allure.step('Получить значение счетчика ингредиента')
    def get_ingredient_counter(self):
        return int(self.get_text(self.INGREDIENT_COUNTER))

    @allure.step('Дождать заголовка конструктора')
    def wait_for_title(self):
        return self.wait_visible(self.TITLE)

    @allure.step('Перетащить ингредиент в конструктор')
    def drag_ingredient(self, locator):
        self.wait_visible(locator)
        ingredient = self.scroll_to_element(locator)
        drop_area = self.wait_visible(self.DROP_AREA)

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
        self.drag_ingredient(self.INGREDIENT_ITEM)

    def drag_first_filling(self):
        self.drag_ingredient(self.FILLING_ITEM)

    @allure.step('Дождаться кнопки оформления заказа')
    def wait_for_order_button(self):
        return self.wait_visible(self.ORDER_BUTTON)

    @allure.step('Дождаться начинки в составе бургера')
    def wait_for_filling(self):
        return self.wait_visible(self.FILLING_IN_CONSTRUCTOR)

    @allure.step('Оформить заказ')
    def click_order_button(self):
        self.click_element(self.ORDER_BUTTON)

    @allure.step('Дождаться номера созданного заказа')
    def get_order_number(self):
        def number_is_ready(driver):
            text = self.get_text(self.ORDER_NUMBER).strip()

            if not text.isdigit():
                return False

            number = int(text)
            if number in (0, 9999):
                return False

            return number

        return WebDriverWait(self.driver, 30).until(number_is_ready)