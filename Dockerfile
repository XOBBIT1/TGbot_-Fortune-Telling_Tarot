FROM python:3.11 as base

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /tg_bot

COPY poetry.lock pyproject.toml ./

RUN pip install --upgrade pip
RUN pip install poetry==1.4.0

RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction

COPY ./ ./

CMD ["python", "main.py"]