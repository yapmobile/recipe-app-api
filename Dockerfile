FROM python:3.8.5-alpine
MAINTAINER Steven Lee

ENV PYTHONUNBUFFERED 1

COPY ./requirement.txt /requirement.txt
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps \
  gcc libc-dev linux-headers postgresql-dev
RUN pip install -r /requirement.txt
RUN apk del .tmp-build-deps

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D user
User user
