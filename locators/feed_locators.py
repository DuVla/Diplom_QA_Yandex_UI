from selenium.webdriver.common.by import By


class FeedLocators:
    # Количество выполненных заказов за всё время.
    TOTAL_COMPLETED_COUNTER = (By.XPATH, "//p[normalize-space()='Выполнено за все время:']/following-sibling::p[1]")
    # Количество выполненных заказов за сегодня.
    TODAY_COMPLETED_COUNTER = (By.XPATH, "//p[normalize-space()='Выполнено за сегодня:']/following-sibling::p[1]")
    # Список заказов в разделе «В работе».
    IN_PROGRESS_ORDERS = (By.XPATH, "//p[normalize-space()='В работе:']/following-sibling::ul[2]")
    # Заголовок для проверки загрузки ленты заказов.
    TITLE = (By.XPATH, "//h1[normalize-space()='Лента заказов']")
    # Отдельные номера заказов в работе: найти номер созданного заказа.
    IN_PROGRESS_ORDER_ITEMS = (By.XPATH, IN_PROGRESS_ORDERS[1] + "/li")
