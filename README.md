# vsphere-kubernetes
Infrastructure-as-Code Project to deploy a fully-automated Kubernetes environment leveraging VMware vSphere, Ubuntu,and Ansible.

## Prerequisites
The vSphere environment requires an Ubuntu 18.04 template to clone the VMs from.

## Ansible Playbooks for SDDC deployment
- deployment.yml: Overarching playbook for all SDDC & VM deployment components
- kube-master-deploy.yml: Deploy master or controller nodes for Kubernetes cluster
- kube-nodes-deploy.yml: Deploy minion nodes for Kubernetes cluster
- kube-nodes-hw.yml: Modifies the CPU and Memory configuration of minion nodes (OPTIONAL)
- kube-drs-rules.yml: Create DRS anti-affinity rules for controllers and minions (OPTIONAL)
- workaround-nics.yml: Properly sets up NIC in each VM, sets it to start connected
- config-ip-controllers|minions.yml: Workaround for Ansible & VMware modules cloned network issue

## Ansible Playbooks for Kubernetes deployment
- installation.yml: Overarching playbook for all OS and Kubernetes components
- kubernetes-install.yml: Base package installation for Kubernetes
- disable-swap.yml: Disable swap partition on Kubernetes controllers and minions
- update-os.yml: Update Ubuntu OS
- cilium-install.yml: Initialize Kubernetes & install Cilium CNI (OPTIONAL)
- flannel-install.yml: Initialize Kubernetes & install Flannel CNI (OPTIONAL)

