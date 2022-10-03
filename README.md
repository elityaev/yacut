<h2 align="center">Yacut</h2>


<h3 >Описание</h3>
Yacut - это сервис по укорачиванию длинных url-ссылок. 

<h3 >Технологии</h3>

- Python 3.7
- Flask 2.0.2

<h3>API</h3>

 - /api/id/ - POST-запрос на создание короткой ссылки

```
{
  "url": "string",
  "custom_id": "string"
}
```
- /api/id/<short_id/ - GET-запрос на получение 
оригинальной ссылки по указанному идентификатору

```
{
  "url": "string"
}
```

<h3>Установка и запуск</h3>
Клонировать репозиторий и перейти в него в командной строке:

```
git@github.com:elityaev/yacut.git
```

```
cd yacut
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/MacOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```
Также необходимо создать в корневой директории и заполнить env-файл 
по следующему шаблону:

```
FLASK_APP=yacut
FLASK_ENV=development
DATABASE_URI=sqlite:///db.sqlite3
SECRET_KEY=SECRET_KEY
```
Запустить сервер 

```
flask run
```

<h3 >Автор</h3>
Литяев Евгений