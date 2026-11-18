from selenium.webdriver.common.by import By


class ConstructorLocators:
    # Вкладка для перехода в конструктор бургера.
    CONSTRUCTOR_TAB = (By.XPATH, "//a[@href='/' and .//p[normalize-space()='Конструктор']]")
    # Заголовок для проверки загрузки конструктора.
    TITLE = (By.XPATH, "//h1[normalize-space()='Соберите бургер']")
    # Вкладка для перехода в ленту заказов.
    FEED_TAB = (By.XPATH, "//a[@href='/feed']")
    # Первый ингредиент в каталоге: открыть детали или перетащить в бургер.
    INGREDIENT_ITEM = (By.XPATH, "(//a[starts-with(@href, '/ingredient/')])[1]")
    # Содержимое открытого окна: проверить его появление и закрытие.
    POPUP = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]//div[contains(@class, 'Modal_modal__container')]")
    # Заголовок «Детали ингредиента» в открытом окне.
    POPUP_TITLE = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]//h2[normalize-space()='Детали ингредиента']")
    # Затемняющие подложки окон: дождаться исчезновения перед следующим кликом.
    MODAL_OVERLAYS = (By.XPATH, "//div[contains(@class, 'Modal_modal_overlay')]")
    # Крестик для закрытия открытого окна.
    POPUP_CLOSE_BUTTON = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]//button[contains(@class, 'Modal_modal__close')]")
    # Счётчик первого ингредиента: проверить увеличение после добавления.
    INGREDIENT_COUNTER = (By.XPATH, "(//a[starts-with(@href, '/ingredient/')])[1]//p[contains(@class, 'counter_counter__num')]")
    # Область конструктора, в которую перетаскиваются ингредиенты.
    DROP_AREA = (By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket__')]")
    # Кнопка для оформления собранного заказа.
    ORDER_BUTTON = (By.XPATH, "//button[normalize-space()='Оформить заказ']")
    # Первая начинка в каталоге для добавления в бургер.
    FILLING_ITEM = (By.XPATH, "//h2[normalize-space()='Начинки']/following-sibling::ul[1]/a[1]")
    # Добавленная начинка: проверить её появление в составе бургера.
    FILLING_IN_CONSTRUCTOR = (By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket__')]//span[normalize-space()='Хрустящие минеральные кольца']")
    # Номер созданного заказа в открытом окне.
    ORDER_NUMBER = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]//h2[contains(@class, 'Modal_modal__title_shadow')]")
