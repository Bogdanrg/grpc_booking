FROM python:latest

WORKDIR /usr/src/app

COPY Pipfile Pipfile.lock ./

RUN apt-get update \
    && apt-get install netcat-traditional -y

RUN pip install -U pipenv \
    && pipenv install --system

COPY entrypoint.sh /usr/src/app/entrypoint.sh
COPY booking_server_ep.sh /usr/src/app/booking_server_ep.sh

COPY . .
