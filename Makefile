make build:
	docker build -t saverbot .

make start:
	docker run -t saverbot

make lint:
	poetry run flake8 saverbot

make instagram-session:
	echo 'Please enter instagram username'
	read username
	poetry run instaloader -l $username
