FROM kodamap/python3x:latest
MAINTAINER Hiroshi KODAMA

RUN git clone https://github.com/kodamap/googlecli

RUN cd googlecli; \
    pip install --upgrade pip; \
    pip install --upgrade google-api-python-client; \
    pip install -r requirements.txt; \
    python setup.py build; \
    python setup.py install; \
    . /root/.bash_profile; \
    googlectl -h

ENV LANG en_US.UTF-8
