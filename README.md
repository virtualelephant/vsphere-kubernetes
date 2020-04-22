# vsphere-kubernetes
Infrastructure-as-Code Project to deploy a fully-automated Kubernetes environment leveraging VMware vSphere, Ubuntu,and Ansible.

## Prerequisites
The vSphere environment requires an Ubuntu 18.04 template to clone the VMs from.

## Ansible Playbooks
- main.yml: Execute entire stand-up of a Kubernetes environment
- kube-master-deploy.yml: Deploy master or controller nodes for Kubernetes cluster
- kube-nodes-deploy.yml: Deploy minion nodes for Kubernetes cluster
- kube-nodes-hw.yml: Modifies the CPU and Memory configuration of minion nodes (OPTIONAL)
- kube-drs-rules.yml: Create DRS anti-affinity rules for controllers and minions (OPTIONAL)
- vm-config-nics.yml: Properly sets up NIC in each VM, sets it to start connected
- vm-net-workaround.yml: Workaround for open-vm-tools issue with network configuration

## In Progress
- Deploy and configure Cilium as the Kubernetes CNI
- Deploy and configure Flannel as the Kubernetes CNI
