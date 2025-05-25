FROM python:3.9-slim

WORKDIR /app

RUN pip install --no-cache-dir fastapi[standard] uvicorn

# could be removed if docker-compose volume is mounting the source code
COPY . .  

CMD ["fastapi", "dev", "books2.py", "--reload", "--host", "0.0.0.0", "--port", "8000"]