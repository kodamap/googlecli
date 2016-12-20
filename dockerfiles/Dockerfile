FROM centos:centos7
MAINTAINER Hiroshi KODAMA

RUN yum -y -q install zlib-devel bzip2 bzip2-devel readline-devel sqlite sqlite-devel openssl-devel patch gcc make git

RUN git clone https://github.com/yyuu/pyenv.git ~/.pyenv; \
    echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile; \
    echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile; \
    echo 'export LANG=en_US.UTF-8' >> ~/.bash_profile; \
    echo 'eval "$(pyenv init -)"' >> ~/.bash_profile; \
    echo 'test -r ~/.bashrc && . ~/.bashrc' >> ~/.bash_profile; \
    echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile

ENV HOME /root
ENV PYENV_ROOT $HOME/.pyenv
ENV PATH $PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH

RUN eval "$(pyenv init -)"; \
    pyenv install 3.5.2; \
    pyenv global 3.5.2; \
    pyenv rehash

RUN git clone https://github.com/kodamap/googlecli; \
    cd googlecli; \
    pip install --upgrade google-api-python-client; \
    pip install -r requirements.txt; \
    python setup.py build; \
    python setup.py install; \
    $PYENV_ROOT/versions/3.5.2/bin/googlectl -h