## <h1 align="center"> Проект API для социальной сети YaTube </h1>
>"Post and patch your life" 

![](https://img.shields.io/badge/Developed%20by-Kondr-blue)

## Описание
Данный проект представляет собой социальную сеть, в которой реализованы следующие возможности:  

* Создние поста
* Возможность прокомментировать чей-либо пост
* Подписаться или отписаться на какого-либо автора

### Используемые технологии:

* Python 3.8
* Django 2.2
* Django Rest Framework 3.12
* JWT + Joser

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:AlexeyKondrukevich/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

```
source venv/bin/activate
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
Примеры запросов к API и документацию можно посмотреть [тут](http://127.0.0.1:8000/redoc/) **(при запущенном проекте)**
