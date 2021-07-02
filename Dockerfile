FROM ubuntu:20.04

# - Upgrade base security packages
RUN DEBIAN_FRONTEND=noninteractive apt-get update && \
    grep security /etc/apt/sources.list > /tmp/security.list && \
    DEBIAN_FRONTEND=noninteractive apt-get upgrade -oDir::Etc::Sourcelist=/tmp/security.list -yq && \
    rm /tmp/security.list

# - Compile and install protobuf
RUN \
    DEBIAN_FRONTEND=noninteractive apt-get install -y autoconf automake libtool curl make g++ unzip wget && \
    wget https://github.com/google/protobuf/releases/download/v3.11.3/protobuf-python-3.11.3.tar.gz && \
    tar -zxvf protobuf-python-3.11.3.tar.gz && \
    cd protobuf-3.11.3/ && \
    ./configure && \
    make -j 2 && \
    make install && \
    ldconfig

# - Tools
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y git curl wget nano vim less unzip bzip2 file rsync

# - Python 3
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y build-essential libpq-dev libxslt1-dev poppler-utils
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y python3 python3-dev python3-pip python3-setuptools python3-libxml2
RUN curl https://bootstrap.pypa.io/get-pip.py --output /tmp/get-pip.py && \
        python3 /tmp/get-pip.py && \
        rm -f /tmp/get-pip.py
RUN pip3 install --upgrade pip

# - adsmsg
RUN git clone https://github.com/adsabs/ADSPipelineMsg /app
WORKDIR /app
RUN pip3 install -r requirements.txt

CMD /bin/bash

