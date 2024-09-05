FROM python:3.12-slim

WORKDIR /app

COPY main.py .
COPY database.py .
COPY .env .



RUN pip install --no-cache-dir fastapi sqlalchemy geopy pydantic python-dotenv uvicorn pymysql cryptography

EXPOSE 8729

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8729"]





