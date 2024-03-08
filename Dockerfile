FROM python:3.11.8-alpine
WORKDIR pyscasso
ENV PIP_ROOT_USER_ACTION=ignore

# testing is needed for tcp replay
RUN echo "@testing https://dl-cdn.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories
RUN echo "@community https://dl-cdn.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories
RUN apk update
RUN apk add linux-headers
RUN apk add build-base

RUN apk add curl
RUN apk add curl-dev
RUN apk add libcap-utils

RUN apk add tshark@community
RUN chmod 750 /usr/bin/dumpcap
RUN chown root:wireshark /usr/bin/dumpcap
RUN addgroup $(id -un) wireshark
RUN setcap cap_net_raw,cap_net_admin+eip /usr/bin/dumpcap

RUN apk add tcpreplay@testing
RUN addgroup -S tcpreplay
RUN addgroup $(id -un) tcpreplay
RUN chmod 750 /usr/bin/tcpreplay
RUN chown root:tcpreplay /usr/bin/tcpreplay
RUN setcap cap_net_raw,cap_net_admin+eip /usr/bin/tcpreplay

RUN apk add libnetfilter_queue-dev
RUN apk add libnfnetlink-dev

RUN apk add tmux

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENTRYPOINT [ "pytest" ]
