# Команда для build локального образа

```
sudo docker build -f Dockerfile --force-rm -t chromedriver-superset:2.1.1 .
```

## Заменить в docker-compose-non-dev.yml
Заходим в скачанный репозиторий superset.

В файле docker-compose-non-dev.yml Меняем строку 

```x-superset-image: &superset-image apache/superset:${TAG:-latest-dev}```

на

```x-superset-image: &superset-image chromedriver-superset:2.1.1```

## Добавляем настройки в superset_config.py
Копируем настройки из файла add_to_superset_config.py в файл superset_config.py

# Запускаем развертывание apache superset с образом firefox-superset
```sudo docker-compose -f docker-compose-non-dev.yml up```