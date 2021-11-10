FROM ubuntu:latest
RUN ln -snf /usr/share/zoneinfo/Europe/Moscow /etc/localtime && echo Europe/Moscow > /etc/timezone

RUN set -ex && \
    apt-get update && \
    apt-get install -y iputils-ping && \
    apt-get install -y curl && \
    apt-get install -y python: && \
    apt-get install -y pip && \
    apt-get clean && \
    rm -rf /var/cache/apt

RUN python3 -m pip install --upgrade pip && \
    pip install exchangelib

COPY . /app

ENTRYPOINT python3 /app/mail_akkuyu.py 2> /dev/null
