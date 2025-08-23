# Strategy Python Service Dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY pyproject.toml .
RUN pip install poetry && poetry install --no-root

COPY . .

ENV PYTHONUNBUFFERED=1

CMD ["poetry", "run", "python", "main.py"]
