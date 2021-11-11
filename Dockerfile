FROM ubuntu:latest
RUN ln -snf /usr/share/zoneinfo/Europe/Moscow /etc/localtime && echo Europe/Moscow > /etc/timezone

RUN set -ex && apt-get update && apt-get install -y \
    iputils-ping=3:20190709-3 \
    curl=7.68.0-1ubuntu2.7 \
    python3=3.8.2-0ubuntu2 \
    python3-pip=20.0.2-5ubuntu1.6 \
    cron=3.0pl1-136ubuntu1 \
    vim=2:8.1.2269-1ubuntu5.3 \
    ntp=1:4.2.8p12+dfsg-3ubuntu4.20.04.1 \
    && apt-get clean && rm -rf /var/cache/apt

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

COPY ./post_owl.py /app/post_owl.py
COPY ./start.sh /app/start.sh
RUN  chmod +x /app/post_owl.py /app/start.sh

ENTRYPOINT /app/start.sh
