# Stellar Burgers · UI-тесты

Учебный дипломный проект Яндекс Практикума: автоматизация пользовательских сценариев веб-приложения Stellar Burgers. Проект прошёл ревью и принят.

**Python · Selenium · pytest · Page Object · Allure**

[Портфолио автора](https://github.com/DuVla) · [Юнит-тесты](https://github.com/DuVla/Diplom_QA_Yandex) · [API-тесты](https://github.com/DuVla/Diplom_QA_Yandex_API)

## Что проверяется

| Область | Сценарии |
|---|---|
| Навигация | Переходы в конструктор и ленту заказов |
| Ингредиенты | Открытие деталей, закрытие окна крестиком, увеличение счётчика при добавлении |
| Лента заказов | Увеличение счётчиков за всё время и за сегодня; появление номера нового заказа в работе |
| Оформление заказа | Дополнительная проверка для авторизованного пользователя |

Всего **9 тестов**, которые запускаются в **Google Chrome и Mozilla Firefox**. Заказы оформляются через интерфейс; тестовые пользователи создаются и удаляются через API.

## Организация проекта

- Классы страниц описаны по Page Object.
- Взаимодействия с WebDriver, JavaScript и ожидания собраны в `BasePage`.
- Локаторы находятся в отдельном пакете; элементы выбираются по атрибутам, классам и подписям.
- Тесты сгруппированы по функциональности. Все действия выполняются до итоговых проверок.
- Используются явные ожидания состояния интерфейса и шаги Allure.

## Результаты и отчёты

Последние полные прогоны после ревью, **19.11.2026**:

| Браузер | Результат | Готовый отчёт |
|---|---|---|
| Chrome | **9 passed** | [Скачать Allure](reports/allure-chrome.zip) |
| Firefox | **9 passed** | [Скачать Allure](reports/allure-firefox.zip) |

[Как открыть готовые отчёты](reports/README.md). Скачайте и распакуйте нужный архив. Из родительской папки запустите одну команду:

```bash
allure open allure-chrome
# или
allure open allure-firefox
```

## Установка

Нужны Python 3, Chrome, Firefox и Allure CLI. Selenium Manager загружает драйверы автоматически; для этого требуется доступ в интернет.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

На Windows для активации: `.venv\Scripts\activate`.

## Запуск

Из корня репозитория:

```bash
python -m pytest tests --browser=chrome -v
python -m pytest tests --browser=firefox -v
```

Прогоны с формированием свежих результатов Allure:

```bash
python -m pytest tests --browser=chrome --alluredir=allure-results/chrome --clean-alluredir
python -m pytest tests --browser=firefox --alluredir=allure-results/firefox --clean-alluredir
```

Просмотр результатов — одна команда за раз:

```bash
allure serve allure-results/chrome
# или
allure serve allure-results/firefox
```

Остановить сервер просмотра можно сочетанием `Ctrl+C`.

## Структура

```text
pages/           # BasePage, ConstructorPage и FeedPage
locators/        # локаторы элементов и пояснения
tests/           # навигация, ингредиенты, лента и оформление заказа
conftest.py      # выбор браузера, фикстуры пользователя и авторизации
api_helpers.py   # подготовка и удаление пользователей
urls.py          # адреса приложения и API
reports/         # готовые отчёты Allure
```

Свежие результаты в `allure-results/` исключены из Git. В `reports/` сохранены архивы проверенных прогонов. Приложение и API являются внешними учебными сервисами; их доступность влияет на выполнение тестов.
