# vsphere-kubernetes
Infrastructure-as-Code Project to deploy a fully-automated Kubernetes environment leveraging VMware vSphere, Ubuntu,and Ansible.

## Prerequisites
The vSphere environment requires an Ubuntu 22.04LTS template to clone the VMs from.

## Ansible Playbooks for SDDC deployment
- kube-cntlr-deploy.yml: Deploy master or controller nodes for Kubernetes cluster
- kube-nodes-deploy.yml: Deploy minion nodes for Kubernetes cluster
- kube-nodes-hw.yml: Modifies the CPU and Memory configuration of minion nodes
- kube-drs-rules.yml: Create DRS anti-affinity rules for controllers
- vcenter-generate-inventory: Create Ansible inventory file with correct VM names and IP addresses

## Ansible Playbooks for Kubernetes deployment
