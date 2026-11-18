from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions as EC
import allure


class BasePage:
    TIMEOUT = 10

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открыть страницу {url}')
    def open_url(self, url):
        self.driver.get(url)

    @allure.step('Дождаться видимости элемента{locator}')
    def wait_visible(self, locator):
        return WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step('Проскролить к элементу{locator}')
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script('arguments[0].scrollIntoView({block: "center"});', element)
        return element

    @allure.step('Кликнуть по элементу {locator}')
    def click_element(self, locator):
        self.wait_visible(locator)
        self.scroll_to_element(locator)

        def try_click(driver):
            element = EC.element_to_be_clickable(locator)(driver)
            if not element:
                return False

            try:
                element.click()
                return True
            except ElementClickInterceptedException as error:
                print('Клик перекрыт:', error.msg)
                return False

        WebDriverWait(self.driver, self.TIMEOUT).until(try_click)

    @allure.step('Ввести текст "{text}" в поле {locator}')
    def set_text(self, locator, text):
        element = self.wait_visible(locator)
        element.clear()
        element.send_keys(text)

    @allure.step('Получить текст элемента{locator}')
    def get_text(self, locator):
        return self.wait_visible(locator).text

    @allure.step('Получить текущий URL')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Дождаться исчезновения элемент{locator}')
    def wait_invisible(self, locator):
        return WebDriverWait(self.driver, self.TIMEOUT).until(EC.invisibility_of_element_located(locator))
