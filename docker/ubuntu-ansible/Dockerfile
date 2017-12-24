# Dockerfile for creating an Ansible Control Server with
# the VMware modules necessary to build a complete Kubernetes
# stack.
# Blog details available: http://virtualelphant.com

FROM ubuntu:artful
MAINTAINER Chris Mutchler <chris@virtualelephant.com>

RUN \
  apt-get -y update && \
  apt-get -y dist-upgrade && \
  apt-get -y install software-properties-common python-software-properties vim && \
  apt-add-repository ppa:ansible/ansible

RUN \
  apt-get -y update && \
  apt-get -y install ansible python-pip python-dev libxml2 libxml2-dev libxslt1-dev zlib1g-dev npm git && \
  pip install --upgrade pyvmomi && \
  pip install pysphere && \
  pip install nsxramlclient && \
  npm install -g https://github.com/yfauser/raml2html && \
  npm  install -g raml-fleece

RUN \
  git clone https://github.com/vmware/nsxansible && \
  rm -rf nsxansible/library/__init__.py && \
  cp nsxansible/library/*.py /usr/lib/python2.7/dist-packages/ansible/modules/cloud/vmware/
