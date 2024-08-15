FROM python:3.12-slim

RUN pip install poetry

WORKDIR /app

COPY . .

RUN poetry install --no-dev

COPY . /app

CMD ["poetry", "run", "tx-producer"]
