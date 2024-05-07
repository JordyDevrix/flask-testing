FROM python:3.10
LABEL authors="2109j"

ADD . .

RUN pip install flask

EXPOSE 5100

CMD python app.py

