import allure

from pages.constructor_page import ConstructorPage

@allure.title('Авторизованному пользователю доступно оформление заказа')
def test_authorization_user(authorized_driver):
    page = ConstructorPage(authorized_driver)
    page.drag_first_ingredient()
    page.drag_first_filling()

    assert page.wait_for_order_button().is_displayed()
    assert page.wait_for_order_button().is_displayed()

    page.click_order_button()
    order_number = page.get_order_number()

    assert order_number > 0