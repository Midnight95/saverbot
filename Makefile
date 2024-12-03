build:
	docker build -t saverbot .

start:
	docker run -t saverbot

lint:
	poetry run flake8 saverbot

instagram-session:
	@echo 'Please enter instagram username'
	@read username; poetry run instaloader -l $$username; mv /home/$$USER/.config/instaloader/session-$$username .
	

