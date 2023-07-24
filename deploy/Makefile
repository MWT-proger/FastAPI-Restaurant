up_build:
	docker-compose --env-file .env  up --build

up:
	docker-compose --env-file .env  up

build:
	docker-compose --env-file .env  build

db_generate:
	docker-compose --env-file .env  exec app alembic init -t async models/migrations

db_migrate:
	docker-compose --env-file .env  exec app alembic revision --autogenerate -m "updated"

db_upgrade:
	docker-compose --env-file .env  exec app alembic upgrade head

