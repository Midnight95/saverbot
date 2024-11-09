FROM ubuntu:24.04

WORKDIR /app

RUN apt update && apt install ffmpeg python3 python3-pip -y

RUN pip install poetry --break-system-packages

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

COPY . .

RUN poetry install --without dev

CMD ["poetry", "run", "bot"]
