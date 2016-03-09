FROM ubuntu:14.04

MAINTAINER Claus <claus@crate.io>

RUN apt-get install -y python git curl
RUN curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"; python get-pip.py
RUN pip install locustio pyzmq
RUN git clone https://github.com/crate/crate-benchmark.git
RUN cd crate-benchmark; python bootstrap.py; bin/buildout -N;

CMD [build/<platform>/locust, ../locust/locustfile.py]
