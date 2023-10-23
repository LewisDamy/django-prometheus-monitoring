FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY ./prometheus_grafana_integration .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
