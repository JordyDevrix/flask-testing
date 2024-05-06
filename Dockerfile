FROM python:3.10
LABEL authors="2109j"

ADD . .

RUN pip install flask

CMD python app.py

