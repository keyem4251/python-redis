FROM python:3.9

WORKDIR /src

RUN pip install --upgrade pip && pip install poetry
COPY ./app/pyproject.toml ./app/poetry.lock ./
RUN poetry export --without-hashes -f requirements.txt > requirements.txt
RUN pip install -r requirements.txt

ENV HOST=redis

COPY /app ./

CMD ["python3", "-m", "app.main"]
