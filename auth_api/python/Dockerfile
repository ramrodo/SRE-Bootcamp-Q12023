# sre-bootcamp-q12023
FROM python:3-alpine

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8000

CMD python ./api.py
