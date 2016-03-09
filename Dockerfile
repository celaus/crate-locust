FROM ubuntu:14.04

MAINTAINER Claus <claus@crate.io>

FROM celaus/crate-locust

RUN DEBIAN_FRONTEND=noninteractive apt-get -y update
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install python python-pip
RUN pip install locustio crate

WORKDIR /locust

ENTRYPOINT ["locust"]
