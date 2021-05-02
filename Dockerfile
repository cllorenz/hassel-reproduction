FROM debian
LABEL Description="This image is used to reproduce the benchmarking results from literature for NetPlumber."

ENV APT_CONFS="-y --no-install-recommends"
ENV DIRPATH=/home/hassel-reproduction
WORKDIR $DIRPATH

RUN apt-get $APT_CONFS update
RUN apt-get $APT_CONFS upgrade

RUN apt-get $APT_CONFS install build-essential

RUN apt-get $APT_CONFS install liblog4cxx10v5
RUN apt-get $APT_CONFS install liblog4cxx-dev
RUN apt-get $APT_CONFS install libcppunit-1.14-0
RUN apt-get $APT_CONFS install libcppunit-dev

RUN apt-get $APT_CONFS install python2
RUN apt-get $APT_CONFS install python2-dev

COPY . $DIRPATH/
RUN make -j -C net_plumber/Ubuntu-NetPlumber-Release clean
RUN make -j -C net_plumber/Ubuntu-NetPlumber-Release all
RUN cd hsa-python && bash setup.sh
