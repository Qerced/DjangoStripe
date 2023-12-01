# Тестовое задание ООО Простые Решения

## Описание

- [x] Реализовать Django + Stripe API бэкенд со следующим функционалом и условиями:
- [x]	Django Модель Item с полями (name, description, price)
- [x] API с двумя методами:
- [x] GET /buy/{id}, c помощью которого можно получить Stripe Session Id для оплаты выбранного Item. При выполнении этого метода c бэкенда с помощью python библиотеки stripe должен выполняться запрос stripe.checkout.Session.create(...) и полученный session.id выдаваться в результате запроса
- [x] GET /item/{id}, c помощью которого можно получить простейшую HTML страницу, на которой будет информация о выбранном Item и кнопка Buy. По нажатию на кнопку Buy должен происходить запрос на /buy/{id}, получение session_id и далее с помощью JS библиотеки Stripe происходить редирект на Checkout форму stripe.redirectToCheckout(sessionId=session_id)
- [x] Запуск используя Docker
- [x] Использование environment variables
- [x] Просмотр Django Моделей в Django Admin панели
- [ ] Запуск приложения на удаленном сервере, доступном для тестирования
- [x] Модель Order, в которой можно объединить несколько Item и сделать платёж в Stripe на содержимое Order c общей стоимостью всех Items
- [ ] Модели Discount, Tax, которые можно прикрепить к модели Order и связать с соответствующими атрибутами при создании платежа в Stripe - в таком случае они корректно отображаются в Stripe Checkout форме.
- [ ] Добавить поле Item.currency, создать 2 Stripe Keypair на две разные валюты и в зависимости от валюты выбранного товара предлагать оплату в соответствующей валюте
- [ ] Реализовать не Stripe Session, а Stripe Payment Intent.

## Запуск

```
docker-compose -f infra/docker-compose.yml up
```

Шаблон заполнения `.env` в [.env.example]()

## Доступ к админ-панели

```dotenv
username=admin
password=test_admin
```
