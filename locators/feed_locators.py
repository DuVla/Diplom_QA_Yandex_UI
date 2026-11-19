from selenium.webdriver.common.by import By


class FeedLocators:
    # Счётчик рядом с подписью «Выполнено за все время».
    TOTAL_COMPLETED_COUNTER = (
        By.XPATH,
        "//p[normalize-space()='Выполнено за все время:']"
        "/following-sibling::p[contains(@class, 'OrderFeed_number')]",
    )
    # Счётчик рядом с подписью «Выполнено за сегодня».
    TODAY_COMPLETED_COUNTER = (
        By.XPATH,
        "//p[normalize-space()='Выполнено за сегодня:']"
        "/following-sibling::p[contains(@class, 'OrderFeed_number')]",
    )
    # Список заказов в работе, найденный по собственному классу.
    IN_PROGRESS_ORDERS = (By.CSS_SELECTOR, 'ul[class*="OrderFeed_orderListReady"]')
    # Заголовок для проверки загрузки ленты заказов.
    TITLE = (By.XPATH, "//h1[normalize-space()='Лента заказов']")
    # Отдельные номера заказов в списке «В работе».
    IN_PROGRESS_ORDER_ITEMS = (By.CSS_SELECTOR, 'ul[class*="OrderFeed_orderListReady"] > li')
