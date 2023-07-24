
## Содержание
- [Использование](#использование)


## Использование
Краткое руководство по запуску и установки проекта


### Запустить в Docker контейнере

- Установите docker и docker-compose на свой компьютер

- создайте env file, заполните его необходимой информацией

```sh
cp deploy/example.env deploy/.env
```

- из каталога deploy запустите в командной строке команду

*Если есть make на компьютере*

```sh
make up_build
```
*Если нет*

```sh
docker-compose --env-file .env  up --build
```
