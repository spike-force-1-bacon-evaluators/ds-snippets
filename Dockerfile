FROM debian:jessie

RUN \
    apt-get update && \
    apt-get install -y \
    python \
    python-dev \
    python-distribute \
    python-pip

RUN pip install \
    pytest \
    pytest-cov \
    numpy \
    py2neo \
    pandas

COPY . usr/src/ds-snippets/

WORKDIR /usr/src/ds-snippets
