## Description:

Pet-project whitch realized basic elements of API for social network.

## How to build project:

- Clone this repo and go into project dir via command promt:

```console

git clone https://github.com/mklstpn/api_final_yatube.git

cd api_final_yatube
```

- Create and activate virtual env:

```console
python3 -m venv env

source env/bin/activate

python3 -m pip install --upgrade pip
```
- Install dependencies from requirements.txt:

```console
pip install -r requirements.txt
```
- Run migrations:

```console
python3 manage.py migrate
```
- Run project:

```console
python3 manage.py runserver
```

## Examples:

### Create post:

At POST запросе на /api/v1/posts/ 
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

При POST request on /api/v1/posts/{id}/ 
```json
{
  "text": "string"
}
```
Response will contain:
```json
{
  "id": 0,
  "author": "string",
  "text": "string",
  "created": "2019-08-24T14:15:22Z",
  "post": 0
}
```
### Get JWT-token:

At POST request on /api/v1/jwt/create/ 
```json
{
  "username": "string",
  "password": "string"
}
```
Response will contain:
```json
{
  "username": "string"
}
```
