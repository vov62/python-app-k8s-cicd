FROM python:3.13.3-slim

WORKDIR /app

COPY requirements.txt /app

RUN pip install -r requirements.txt

COPY ./src /app/src

EXPOSE 5000

CMD ["python", "src/app.py"]


