FROM python:3.10
LABEL authors="2109j"

ADD . .

RUN pip install flask

EXPOSE 5100d

CMD python app.py

