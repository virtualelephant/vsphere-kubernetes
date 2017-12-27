# Dockerfile for creating an specific DNS server
# to be used within the vSphere Kubernetes environment.
#
# Blog details available: http://virtualelphant.com

FROM ubuntu:artful
MAINTAINER Chris Mutchler <chris@virtualelephant.com>

RUN \
  apt-get -y update && \
  apt-get -y dist-upgrade && \
  apt-get -y install software-properties-common python-software-properties vim bind9 bind9-doc bind9-host bind9utils

COPY named.conf.default-zones /etc/bind/
COPY named.conf.options /etc/bind
COPY db.192.0 /etc/bind
COPY db.192.1 /etc/bind
COPY db.192.2 /etc/bind
COPY db.lab /etc/bind
