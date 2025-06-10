FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /app/TodoApp

ENV PYTHONPATH=/app/TodoApp

CMD ["fastapi", "dev", "main.py", "--reload", "--host", "0.0.0.0", "--port", "8000"]