# vsphere-kubernetes
Infrastructure-as-Code Project to deploy a fully-automated Kubernetes environment leveraging VMware vSphere, Ubuntu,and Ansible.

To deploy the environment, perform the following steps:
1. Modify the 'envanswer.yml' file to include the environment-specific URLS, usernames, passwords, and additional configuration information.
2. Run the Ansible playbook 'deploy_kubernetes.yml'

## Prerequisites
The vSphere environment requires an Ubuntu 22.04LTS template to clone the VMs from.

## Ansible Playbooks for SDDC deployment
These are the individual Ansible Playbooks leveraged to deploy Kubernetes inside a VMware SDDC environment

- kube-cntlr-deploy.yml: Deploy master or controller nodes for Kubernetes cluster
- kube-nodes-deploy.yml: Deploy minion nodes for Kubernetes cluster
- kube-nodes-hw.yml: Modifies the CPU and Memory configuration of minion nodes
- kube-drs-rules.yml: Create DRS anti-affinity rules for controllers
- vcenter-generate-inventory: Create Ansible inventory file with correct VM names and IP addresses

## Ansible Playbooks for Kubernetes deployment
