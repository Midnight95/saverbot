make build:
	docker build -t saverbot .

make start:
	docker run -t saverbot

make lint:
	poetry run flake8 saverbot
