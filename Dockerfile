FROM python:3.9.21-slim
WORKDIR /app
COPY ./src/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
ENV PYTHONPATH=/app
CMD ["python", "src/main.py"]