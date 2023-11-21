FROM ubuntu:20.04

# - Upgrade base security packages
RUN DEBIAN_FRONTEND=noninteractive apt-get update && \
    grep security /etc/apt/sources.list > /tmp/security.list && \
    DEBIAN_FRONTEND=noninteractive apt-get upgrade -oDir::Etc::Sourcelist=/tmp/security.list -yq && \
    rm /tmp/security.list

# - Compile and install protobuf
RUN \
    DEBIAN_FRONTEND=noninteractive apt-get install -y autoconf automake libtool curl make g++ unzip wget && \
    wget https://github.com/google/protobuf/releases/download/v3.17.3/protobuf-python-3.17.3.tar.gz && \
    tar -zxvf protobuf-python-3.17.3.tar.gz && \
    cd protobuf-3.17.3/ && \
    ./configure && \
    make -j 2 && \
    make install && \
    ldconfig

# - Tools
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y git curl wget nano vim less unzip bzip2 file rsync

# - Python 2 & 3
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y build-essential libpq-dev libxslt1-dev poppler-utils
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y python2 python2-dev python-setuptools python-libxml2
RUN curl https://bootstrap.pypa.io/pip/2.7/get-pip.py --output /tmp/get-pip.py && \
        python2 /tmp/get-pip.py && \
        rm -f /tmp/get-pip.py
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y python3 python3-dev python3-pip python3-setuptools python3-libxml2
RUN pip2 install --upgrade pip && \
    pip3 install --upgrade pip

# - adsmsg
RUN git clone https://github.com/adsabs/ADSPipelineMsg /app
WORKDIR /app
RUN pip install -r requirements.txt && \
    pip3 install -r requirements.txt

# -Install a newer version of sed to fix issue with sed -i not handling permissions properly
RUN wget https://ftp.gnu.org/gnu/sed/sed-4.9.tar.gz && \
    tar -xzvf sed-4.9.tar.gz && \
    cd sed-4.9/ && \
    ./configure && make install

CMD /bin/bash

