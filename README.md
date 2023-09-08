# "Апи социальной сети Yatube" (api_final)

## 1. [Описание](#1)
## 2. [Установка](#2)
## 3. [Создание виртуального окружения](#3)
## 4. [Команды для запуска](#4)
## 5. [Примеры запросов к api](#5)
## 6. [Об авторе](#6)

---
## 1. Описание <a id=1></a>

API для проекта социальной сети блогеров Yatube, на котором пользователи могут: 
  - регистрироваться
  - создавать посты и управлять ими (корректировать\удалять)
  - создавать свои комментарии к постам и управлять ими (корректировать\удалять)
  - просматривать посты других пользователей
  - подписываться на других пользователей

---
## 2. Установка <a id=2></a>

Перед запуском необходимо склонировать проект:
```bash
git clone git@github.com:juliana-str/api_final_yatube.git
```
```
cd api_final_yatube/
```

---
## 3. Создание виртуального окружения <a id=3></a>

Cоздать и активировать виртуальное окружение:
```bash
python -m venv venv
```
```bash
Linux: source venv/bin/activate
Windows: source venv/Scripts/activate
```

---
## 4. Команды для запуска <a id=4></a>

И установить зависимости из файла requirements.txt:
```bash
python3 -m pip install --upgrade pip
```
```bash
pip install -r requirements.txt
```
```bash
python3 manage.py makemigrations
```
```bash
python3 manage.py migrate
```
```bash
python3 manage.py runserver
```

Проект использует базу данных sqlite3.  

---
## 5. Примеры запросов к api <a id=5></a>

Аутентификация 

1. Выполнить POST-запрос http://localhost:8000/api/v1/jwt/create/ передав поля username и password.

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

---
## 6. Об авторе <a id=6></a>

Стрельникова Юлиана Сергеевна  
Python-разработчик (Backend)  
Россия, г. Санкт-Петербург                                                                                                                                                  
E-mail: julianka.str@yandex.ru  
Telegram: @JulianaStr
