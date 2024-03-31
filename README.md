# Web_4_Rest_Api
json Rest API Server
https://www.cleverence.ru/articles/elektronnaya-kommertsiya/rest-api-chto-eto-takoe-prostymi-slovami-primery-zaprosov-varianty-ispolzovaniya-servisa-metody/
Необходимо реализовать простое web-приложение, позволяющее управлять личным списком задач (TODO-лист) посредством простого Rest API (json). 
Список ручек(методов): добавление пользователя - POST /user, 
получить список задач пользователя - GET /todo (если пользователя не существует, то возвращать 4XX код ошибки), 
добавить задачу пользователя - POST /todo, 
удалить задачу пользователя - DELETE /todo/{id}, 
обновить задачу пользователя - PUT /todo/{id}. 
Анализ задачи
Исследование источников
Установить и настроить web-сервер Nginx
Установить и настроить Symfony + Doctrine (или иную связку на другом языке)
Реализовать добавление юзеров
Проверить API, используя curl/Postman/Insomnia
Реализовать ручки управления задачами
Проверить API, используя curl/Postman/Insomnia
Форма отчета: репозиторий на GitHub, с исходным кодом полученного web-приложения и скриншотами проверки API с помощью curl/Postman/Insomnia
