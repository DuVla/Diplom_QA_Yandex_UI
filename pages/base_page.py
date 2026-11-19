import allure
from selenium.common.exceptions import (
    ElementClickInterceptedException,
    StaleElementReferenceException,
    TimeoutException,
)
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    TIMEOUT = 30

    def __init__(self, driver):
        self.driver = driver

    def wait_until(self, condition, timeout=None):
        return WebDriverWait(
            self.driver,
            timeout or self.TIMEOUT,
            ignored_exceptions=(StaleElementReferenceException,),
        ).until(lambda _: condition())

    @allure.step('Открыть страницу {url}')
    def open_url(self, url):
        self.driver.get(url)

    @allure.step('Дождаться видимости элемента {locator}')
    def wait_visible(self, locator):
        return WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.visibility_of_element_located(locator)
        )

    def is_visible(self, locator):
        return self.wait_visible(locator).is_displayed()

    @allure.step('Проскроллить к элементу {locator}')
    def scroll_to_element(self, locator):
        element = self.wait_visible(locator)
        self.driver.execute_script(
            'arguments[0].scrollIntoView({block: "center"});', element
        )
        return element

    @allure.step('Кликнуть по элементу {locator}')
    def click_element(self, locator):
        self.scroll_to_element(locator)

        def try_click():
            element = EC.element_to_be_clickable(locator)(self.driver)
            if not element:
                return False
            try:
                element.click()
                return True
            except ElementClickInterceptedException:
                return False

        return self.wait_until(try_click)

    @allure.step('Получить текст элемента {locator}')
    def get_text(self, locator):
        return self.wait_visible(locator).text

    @allure.step('Получить тексты элементов {locator}')
    def get_texts(self, locator):
        def read_texts():
            texts = [element.text for element in self.driver.find_elements(*locator)]
            return True, texts

        return self.wait_until(read_texts)[1]

    @allure.step('Получить текущий URL')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Дождаться перехода на страницу {url}')
    def wait_for_url(self, url):
        return self.wait_until(
            lambda: self.get_current_url().rstrip('/') == url.rstrip('/')
        )

    @allure.step('Дождаться исчезновения элемента {locator}')
    def wait_invisible(self, locator):
        return WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.invisibility_of_element_located(locator)
        )

    def are_all_invisible(self, locator):
        return all(
            not element.is_displayed()
            for element in self.driver.find_elements(*locator)
        )

    @allure.step('Дождаться исчезновения всех элементов {locator}')
    def wait_all_invisible(self, locator):
        return self.wait_until(lambda: self.are_all_invisible(locator))

    @allure.step('Перетащить элемент {source_locator} в {target_locator}')
    def drag_and_drop(self, source_locator, target_locator):
        source = self.scroll_to_element(source_locator)
        target = self.wait_visible(target_locator)
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
        """, source, target)

    @allure.step('Дождаться номера в элементе {locator}')
    def wait_for_number(self, locator, excluded_numbers=(), timeout=30):
        def number_is_ready():
            text = self.get_text(locator).strip()
            if not text.isdigit():
                return False
            number = int(text)
            return number if number > 0 and number not in excluded_numbers else False

        return self.wait_until(number_is_ready, timeout)

    def authorize(self, access_token, refresh_token):
        self.driver.execute_script("""
            localStorage.setItem('accessToken', arguments[0]);
            localStorage.setItem('refreshToken', arguments[1]);
        """, access_token, refresh_token)
        try:
            self.driver.refresh()
        except TimeoutException:
            self.driver.execute_script('window.stop();')
