make build:
	docker build -t saverbot .

make start:
	docker run -t saverbot

make shell:
	docker run -t saverbot bash

make lint:
	poetry run flake8 saverbot
