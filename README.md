# REST API для Yatube

## Это интерфейс для передачи данных приложениям и фронтенда. 

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Nastasia153/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

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

## Примеры запросов

Пример POST-запроса с токеном Бильбо Бэггинса: добавление нового поста
_POST .../api/v1/posts/_
```
{
    "text": "В поход, беспечный пешеход, уйду, избыв печаль, - спешит дорога от ворот в заманчивую даль..."
    "group": 1
}
```
Пример ответа:
```
{
    "id": 10,
    "text": "В поход, беспечный пешеход, уйду, избыв печаль, - спешит дорога от ворот в заманчивую даль...",
    "author": "bilbo",
    "image": null,
    "group": 1,
    "pub_date": "2991-09-22T08:47:11.084589Z"
}
```
