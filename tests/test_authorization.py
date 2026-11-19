import allure

from pages.constructor_page import ConstructorPage


class TestAuthorization:
    @allure.title('Авторизованный пользователь может оформить заказ')
    def test_authorization_user(self, authorized_driver):
        page = ConstructorPage(authorized_driver)
        page.wait_for_title()
        page.drag_bun()
        page.drag_filling()
        page.wait_for_filling()
        page.wait_for_order_button()
        page.click_order_button()
        order_number = page.get_order_number()

        assert order_number > 0
