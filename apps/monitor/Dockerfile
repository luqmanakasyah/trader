# Monitor Service Dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install prometheus_client fastapi uvicorn
CMD ["uvicorn", "monitor:app", "--host", "0.0.0.0", "--port", "9100"]
