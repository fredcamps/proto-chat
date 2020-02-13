FROM python:3.8-alpine

LABEL maintainer="Fred Campos <fred.tecnologia@gmail.com>"

USER root

WORKDIR /app
ADD . /app/

RUN apk --update add --no-cache git \
    && pip install wheel \
    && pip install pipenv \
    && pipenv install \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /var/cache/apk/*
