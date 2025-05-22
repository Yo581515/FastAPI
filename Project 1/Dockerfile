FROM python:3.9-slim

WORKDIR /app

RUN pip install --no-cache-dir fastapi[standard] uvicorn

COPY . .

CMD ["fastapi", "dev", "books.py", "--reload", "--host", "0.0.0.0", "--port", "8000"]