#!/bin/bash
set -x
set -e

if [ "`docker images adsmsg | grep adsmsg`" = "" ]; then
    docker build -t adsmsg .
    #docker run -it --name adsmsg adsmsg
fi

docker run --rm -v `pwd`:/app --name adsmsg adsmsg make
