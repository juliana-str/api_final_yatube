# api_final

### Описание:

API для проекта социальной сети Yatube.

### Установка:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:juliana-str/api_final_yatube.git
```

```
cd api_final_yatube/
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

```
source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

### Аутентификация 

1. Выполнить POST-запрос http://localhost:8000/api/v1/token/ передав поля username и password.

2. Получить от API JWT-токен в формате:

```
{
  "refresh": "xxx",
  "access": "xxx"
}
```

3. В поле access вернётся токен. Данные в поле refresh будут необходимы для обновления токена.

4. При отправке запроcов передать токен в заголовке Authorization: Bearer <токен>.

### Примеры запросов:

Результат POST-запроса с токеном пользователя на добавление нового поста:

1. Пример запроса:

```
{
    "text": "Текст",
    "group": 1
}
```

2. Пример ответа:

```
{
    "id": 1,
    "text": "Текст",
    "author": "Имя",
    "image": null,
    "group": 1,
    "pub_date": "2022-05-11T08:47:10.084572Z"
}
```
