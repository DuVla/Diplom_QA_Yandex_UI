import allure
from selenium.webdriver.support.ui import WebDriverWait
from pages.constructor_page import ConstructorPage
from urls import BASE_URL


class TestIngredients:
    @allure.title('Клик по ингредиенту открытие окна деталей')
    def test_open_ingredient_modal(self, driver):
        page = ConstructorPage(driver)
        page.open_url(BASE_URL)
        page.click_first_ingredient()

        assert page.is_popup_visible().is_displayed()
        assert page.get_popup_title() == 'Детали ингредиента'

    @allure.title('Крестик закрывает окно деталей ингредиента')
    def test_close_ingredient_modal(self, driver):
        page = ConstructorPage(driver)
        page.open_url(BASE_URL)
        page.click_first_ingredient()
        assert page.is_popup_visible().is_displayed()
        assert page.close_popup()

    @allure.title('Добавление булки увеличивает ее счетчик')
    def test_ingredient_counter_increases(self, driver):
        page = ConstructorPage(driver)
        page.open_url(BASE_URL)

        before = page.get_ingredient_counter()
        page.drag_first_ingredient()

        WebDriverWait(driver, 10).until(
            lambda _: page.get_ingredient_counter() > before
        )

        assert page.get_ingredient_counter() > before
