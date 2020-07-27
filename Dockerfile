FROM python:3.6-alpine
MAINTAINER Todd Radel <todd@banyansecurity.io>
ENV PS1="\[\e[0;33m\]|> banyan <| \[\e[1;35m\]\W\[\e[0m\] \[\e[0m\]# "

WORKDIR /src
COPY . /src
RUN apk add --no-cache \
        gcc \
        libressl-dev \
        musl-dev \
        libffi-dev && \
    pip install --no-cache-dir -r requirements.txt && \
    python setup.py install && \
    apk del \
        gcc \
        libressl-dev \
        musl-dev \
        libffi-dev
WORKDIR /
ENTRYPOINT ["banyan"]
