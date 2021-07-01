FROM ubuntu:20.04

ENV TZ=Europe/London
ARG DEBIAN_FRONTEND=noninteractive

ENV SRV_PORT=8090

COPY src /pyechoserver/src
COPY test /pyechoserver/test

RUN apt-get update && apt-get install -y python3 \
  && apt-get -y autoremove && apt-get -y clean

ENTRYPOINT /bin/python3 /pyechoserver/src/main.py --port $SRV_PORT
#ENTRYPOINT ["/usr/bin/bash"]
