# UI-тесты Stellar Burgers

Автотесты для третьего задания дипломного проекта.
Используются Python, pytest, Selenium, requests и Allure.
Страницы описаны с помощью паттерна Page Object.

## Проверяемые сценарии

- Переход в конструктор и ленту заказов.
- Открытие и закрытие окна деталей ингредиента.
- Увеличение счётчика ингредиента при добавлении.
- Увеличение счётчиков заказов за всё время и за сегодня.
- Появление номера нового заказа в разделе «В работе».
- Дополнительная проверка оформления заказа авторизованным пользователем.

Всего 9 тестов. Поддерживаются Chrome и Firefox.
Тестовые пользователи создаются через API и удаляются после тестов.
Заказы оформляются через интерфейс приложения.

## Структура проекта

- `pages/` — классы страниц, локаторы и действия.
- `tests/` — тесты.
- `conftest.py` — фикстуры браузера и пользователей.
- `api_helpers.py` — подготовка и удаление пользователей через API.
- `urls.py` — адреса приложения и API.

## Установка

Нужны Python, Google Chrome, Mozilla Firefox и Allure CLI.
Для автоматической загрузки драйверов Selenium необходим доступ в интернет.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## Запуск тестов

Команды выполняются из корня проекта:

```bash
python -m pytest tests --browser=chrome -v
python -m pytest tests --browser=firefox -v
```

## Отчёты Allure

```bash
python -m pytest tests --browser=chrome --alluredir=allure-results/chrome --clean-alluredir
python -m pytest tests --browser=firefox --alluredir=allure-results/firefox --clean-alluredir
```

Просмотр отчёта нужного браузера (запускайте одну команду за раз):

```bash
allure serve allure-results/chrome
allure serve allure-results/firefox
```

Сервер просмотра останавливается через Ctrl+C.
Результаты и отчёты Allure исключены из Git через `.gitignore`.
