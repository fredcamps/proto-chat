FROM python:3.7-alpine

LABEL maintainer="Fred Campos <fred.tecnologia@gmail.com>"

USER root

WORKDIR /app
ADD . /app/

RUN apk --update add --no-cache git \
    && pip install wheel \
    && pip install -r requirements.txt \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /var/cache/apk/*