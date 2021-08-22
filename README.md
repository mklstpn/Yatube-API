## Описание:

Учебный проект в котором созданы основные элементы API для социальной сети. 

## Как развернуть проект:

- Клонировать репозиторий и перейти в него в командной строке:

`git clone https://github.com/mklstpn/api_final_yatube.git`

`cd api_final_yatube`

- Cоздать и активировать виртуальное окружение:

`python3 -m venv env`

`source env/bin/activate`

`python3 -m pip install --upgrade pip`
- Установить зависимости из файла requirements.txt:

`pip install -r requirements.txt`
- Выполнить миграции:

`python3 manage.py migrate`
- Запустить проект:

`python3 manage.py runserver`

## Примеры запросов к API:

### Создание публикации:

При POST запросе на /api/v1/posts/ 
```
{
  "text": "string",
  "image": "string",
  "group": 0
}
```
Response будет примерно такого содержания:
```
[
  {
    "id": 0,
    "author": "string",
    "text": "string",
    "pub_date": "2019-08-24T14:15:22Z",
    "image": "string",
    "group": 0
  }
]
```
### Обновление публикации:

При PUT запросе на /api/v1/posts/{id}/ 
```
{
  "text": "string",
  "image": "string",
  "group": 0
}
```
Response будет примерно такого содержания:
```
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
}
```
### Добавление комментариев:

При POST запросе на /api/v1/posts/{id}/ 
```
{
  "text": "string"
}
```
Response будет примерно такого содержания:
```
{
  "id": 0,
  "author": "string",
  "text": "string",
  "created": "2019-08-24T14:15:22Z",
  "post": 0
}
```
### Получить JWT-токен:

При POST запросе на /api/v1/jwt/create/ 
```
{
  "username": "string",
  "password": "string"
}
```
Response будет примерно такого содержания:
```
{
  "username": "string"
}
```
