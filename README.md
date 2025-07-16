### 1. Клонировать репозиторий
```bash
git clone https://github.com/BuhalBodyaga/TestWallet.git
cd TestWallet
```
### 2. Создать .env файл в корне проекта
```
DEBUG=True
SECRET_KEY="ваш-секретный-ключ"

DB_NAME=wallet_db
DB_USER=wallet_user
DB_PASSWORD=wallet_pass
DB_HOST=db
DB_PORT=5432
```
### 3. Собрать и запустить контейнеры
```bash
docker-compose up --build
```
Адрес: http://localhost:8000
### 4. Применить миграции внутри контейнера
```bash
docker-compose exec web python manage.py migrate
```
### Создать суперпользователя
```bash
docker-compose exec web python manage.py createsuperuser
```
### Тестирование
```bash
docker-compose exec web pytest
```

