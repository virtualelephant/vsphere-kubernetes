# vsphere-kubernetes
Infrastructure-as-Code Project to deploy a fully-automated Kubernetes environment leveraging VMware vSphere, Ubuntu,and Ansible.

## Ansible Playbooks
- main.yml: Execute entire stand-up of a Kubernetes environment
- kube-master-deploy.yml: Deploy master or controller nodes for Kubernetes cluster
- kube-nodes-deploy.yml: Deploy minion nodes for Kubernetes cluster

## In Progress
- Deploy and configure Cilium as the Kubernetes CNI
- Deploy and configure Flannel as the Kubernetes CNI
