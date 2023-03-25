# vsphere-kubernetes
Infrastructure-as-Code Project to deploy a fully-automated Kubernetes environment leveraging VMware vSphere, Ubuntu,and Ansible.

To deploy the environment, perform the following steps:
1. Modify the 'envanswer.yml' file to include the environment-specific URLS, usernames, passwords, and additional configuration information.
2. Run the Ansible playbook 'deploy_vsphere.yml' to deploy the vSphere components.
3. Run the Ansible playbook 'vcenter-generate-inventory.yml' to create the inventory file for the environment.
4. Run the Ansible playbook 'deploy_kubernetes' to install and configure Kubernetes.

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
- disable-swap.yml: Disables swap inside the OS for each nodes
- install-k8s-packages.yml: Installs all the necessary Kubernetes packages and prerequisites inside Ubuntu
- containerd-workaround.yml: (Optional) Known issue with containerd /etc/containerd/config.toml file
- initialize-kubernetes.yml: Initializes the Kubernetes cluster, deploys Antrea CNI, adds both controllers + workers to cluster