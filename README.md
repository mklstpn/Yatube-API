## Описание:

Учебный проект в котором созданы основные элементы API для социальной сети. 

## Как развернуть проект:

- Клонировать репозиторий и перейти в него в командной строке:

```console

git clone https://github.com/mklstpn/api_final_yatube.git

cd api_final_yatube
```

- Cоздать и активировать виртуальное окружение:

```console
python3 -m venv env

source env/bin/activate

python3 -m pip install --upgrade pip
```
- Установить зависимости из файла requirements.txt:

```console
pip install -r requirements.txt
```
- Выполнить миграции:

```console
python3 manage.py migrate
```
- Запустить проект:

```console
python3 manage.py runserver
```

## Примеры запросов к API:

### Создание публикации:

При POST запросе на /api/v1/posts/ 
```json
{
  "text": "string",
  "image": "string",
  "group": 0
}
```
Response будет примерно такого содержания:
```json
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
```json
{
  "text": "string",
  "image": "string",
  "group": 0
}
```
Response будет примерно такого содержания:
```json
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
```json
{
  "text": "string"
}
```
Response будет примерно такого содержания:
```json
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
```json
{
  "username": "string",
  "password": "string"
}
```
Response будет примерно такого содержания:
```json
{
  "username": "string"
}
```
