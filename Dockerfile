FROM ubuntu:15.10

MAINTAINER Claus <claus@crate.io>


RUN apt-get install -y python-setuptools gcc python git curl
RUN curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"; python get-pip.py
RUN pip install locustio pyzmq
RUN git clone https://github.com/crate/crate-benchmark.git
RUN cd crate-benchmark; python bootstrap.py; bin/buildout -N

WORKDIR /locust

ENTRYPOINT ["locust"]
