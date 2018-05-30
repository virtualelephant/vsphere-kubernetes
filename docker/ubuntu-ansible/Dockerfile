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

# Install packages needed for NSX modules in Ansible
RUN \
  apt-get -y update && \
  apt-get -y install ansible python-pip python-dev libxml2 libxml2-dev libxslt1-dev zlib1g-dev npm git && \
  pip install --upgrade pyvmomi && \
  pip install pysphere && \
  pip install nsxramlclient && \
  npm install -g https://github.com/yfauser/raml2html && \
  npm  install -g raml-fleece

# Get NSXRAML

# Add additional Ansible modules for NSX and VM folders
RUN \
  git clone -b 6.4 https://github.com/vmware/nsxraml.git /opt/nsxraml && \
  git clone https://github.com/vmware/nsxansible && \
  git clone https://github.com/vmware/ansible-modules-extras-gpl3.git && \
  rm -rf nsxansible/library/__init__.py && \
  cp nsxansible/library/*.py /usr/lib/python2.7/dist-packages/ansible/modules/cloud/vmware/ && \
  git clone https://github.com/openshift/openshift-ansible-contrib && \
  /bin/cp openshift-ansible-contrib/reference-architecture/vmware-ansible/playbooks/library/vmware*.py /usr/lib/python2.7/dist-packages/ansible/modules/cloud/vmware/

# Add vSAN Python API modules - must be done after pyVmomi installation
COPY vsanmgmtObjects.py /usr/lib/python2.7/
COPY vsanapiutils.py /usr/lib/python2.7/

# Setup container to properly use SSH bastion host for Ansible
RUN mkdir /root/.ssh
RUN chmod 740 /root/.ssh
COPY config /root/.ssh/config
COPY ansible.cfg /etc/ansible/

# Edit MOTD to give container consumer info
COPY motd /etc/motd
RUN echo '[ ! -z "$TERM" -a -r /etc/motd ] && cat /etc/issue && cat /etc/motd' >> /etc/bash.bashrc
