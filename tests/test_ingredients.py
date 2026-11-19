import allure

from pages.constructor_page import ConstructorPage
from urls import BASE_URL


class TestIngredients:
    @allure.title('Клик по ингредиенту открывает окно деталей')
    def test_open_ingredient_modal(self, driver):
        page = ConstructorPage(driver)
        page.open_url(BASE_URL)
        page.click_ingredient()

        assert page.is_popup_visible()
        assert page.get_popup_title() == 'Детали ингредиента'

    @allure.title('Крестик закрывает окно деталей ингредиента')
    def test_close_ingredient_modal(self, driver):
        page = ConstructorPage(driver)
        page.open_url(BASE_URL)
        page.click_ingredient()
        page.close_popup()

        assert page.is_popup_closed()

    @allure.title('Добавление булки увеличивает её счётчик')
    def test_ingredient_counter_increases(self, driver):
        page = ConstructorPage(driver)
        page.open_url(BASE_URL)
        before = page.get_ingredient_counter()
        page.drag_bun()
        page.wait_for_counter_increase(before)

        assert page.get_ingredient_counter() > before
