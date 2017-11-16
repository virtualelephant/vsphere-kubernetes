#!/bin/bash

wget https://s3-us-west-1.amazonaws.com/s3-kube-coreos/stateful-config.ign
sudo coreos-install -d /dev/sda -i stateful-config.ign -C stable -V current -o vmware_raw
sudo reboot
