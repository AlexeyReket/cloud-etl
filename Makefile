build:
	docker build -t api-v3000 -f system/Dockerfile .
push:
	docker tag api-v3000 cr.yandex/${registry_id}/api-v3000
	docker push cr.yandex/${registry_id}/api-v3000
isort:
	isort --profile black app functions
black:
	black app functions
format: black isort

migrations:
	alembic revision --autogenerate

migrate:
	alembic upgrade head

downgrade:
	alembic downgrade -1

debug:
	PYTHONPATH=./app uvicorn app.main:app --reload --host 0.0.0.0

build-function:
	rm -fr functions/collect_rates/src/__pycache__/
	cd functions/collect_rates && zip -r collect_rates.zip ./*
	mv functions/collect_rates/collect_rates.zip ./

compose-up:
	docker-compose --env-file env/.compose.env up -d