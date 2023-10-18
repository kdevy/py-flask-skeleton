# syntax=docker/dockerfile:1

ARG PYTHON_VERSION=3.11.5
FROM python:${PYTHON_VERSION}-slim-bullseye as base

WORKDIR /app
COPY . .

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update
RUN apt-get -y install locales && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8

ENV LANG ja_JP.UTF-8
ENV LANGUAGE jp_JP:ja
ENV LC_ALL ja_JP.UTF-8

RUN apt-get install -y vim
RUN apt-get install -y gcc
RUN apt-get install -y libmariadb-dev
RUN apt-get install -y apache2
RUN apt-get install -y apache2-dev
RUN apt-get clean
RUN rm -rf /var/lib/apt/lists/*

RUN chown -R www-data:www-data /app


RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=requirements.txt,target=requirements.txt \
    python -m pip install -r requirements.txt

CMD ["apachectl", "-D", "FOREGROUND"]