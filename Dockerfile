FROM python:3.10.6-buster

COPY app.py app.py
COPY rnn_logic rnn_logic
COPY requirements.txt requirements.txt
COPY service_account.json service_account.json


RUN pip install -r requirements.txt


CMD uvicorn app:app --host 0.0.0.0 --port $PORT
