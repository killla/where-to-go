# Куда пойти в Москве

Простой сайт на django с картой интересных мест куда можно сходить в Москве. 

### Как установить

Скачать код.

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, если есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
### Как запустить
Для запуска программы нужно перейти в данную папку и выполнить команду:

```
python manage.py runserver
```

### Загрузить новые локации 
Новые локации загружаются в проект через management команду:
```
python manage.py add_places http://example.com/location.json
```

Например:

```
python manage.py add_places https://github.com/devmanorg/where-to-go-places/raw/master/places/Антикафе%20Bizone.json
```

### Настройка
Настройка проекта осуществлется через нижеперечисленные переменные окружения. Все переменные являются необязательными.

`SECRET_KEY` - секретный ключ django

`DEBUG` - включение дебаг режима

`ALLOWED_HOSTS` - список хостов с которых доступен вебсервер django

### Демонстрация
Проект доступен по адресу: [https://killla.pythonanywhere.com](https://killla.pythonanywhere.com)

### Цель проекта
Проект написан в целях обучения Django и Vue.