## Mini-blog using Django + Materialize

This is a very simple mini-blog with 3 routes:
- / - main page, showing the most recent post at the top and a grid of 9 recent posts below it
- /post/new - add post page with image upload
- /post/:id - view post page

There are no restrictions as to who can create and view posts. The app is in debug mode.
This app is deployed on Heroku (the interface's in Russian): https://az-kodtest.herokuapp.com/

## Мини-блог на Django+Materialize 
-> https://az-kodtest.herokuapp.com/

### Stack
- Python3
- Django
- PostgreSQL
- Git
- Materialize 

### Страницы сайта
- Главная, последний пост сверху и до 9 свежайших в сетке -> /
- Добавление поста, ограничений для добавления нет -> /post/new/
- Просмотр поста, клик по карте или на Читать для верхнего поста /post/id/
