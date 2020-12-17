FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && \
    apt-get install -y python3-pip python3-setuptools wget git

COPY . /opt/dbxref/
RUN pip3 install /opt/dbxref/

CMD dbxref info
