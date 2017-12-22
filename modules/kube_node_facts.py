#!/usr/bin/python
# -*- coding: utf-8 -*-

# forked from http://docs.ansible.com/ansible/latest/vmware_vm_facts_module.html
# Chris Mutchler <chris () virtualelephant.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = r'''
---
module: kube_node_facts
short_description: Search the facts return by specific Kubernetes nodes for vSphere virtual machine guest
description:
- Search basic facts pertaining to a vSphere virtual machine guest.
author:
- Chris Mutchler
notes:
- Tested on vSphere 6.5
requirements:
- python >= 2.6
- PyVmomi
'''

EXAMPLES = r'''
- name: Search registered virtual machines
  kube_node_facts:
  delegate_to: localhost
  register: vmfacts
'''

RETURN = r'''
virtual_machines:
  description: dictionary of virtual machines and their facts
  returned: success
  type: dict
'''

try:
    from pyVmomi import vim, vmodl
    HAS_PYVMOMI = True
except ImportError:
    HAS_PYVMOMI = False

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.vmware import HAS_PYVMOMI, connect_to_api, get_all_objs, vmware_argument_spec

import re

def get_kube_node_virtual_machines(content):
    virtual_machines = get_all_objs(content, [vim.VirtualMachine])
    _virtual_machines = {}

    for vm in virtual_machines:
        _ip_address = ""

        if bool(re.search('node', vm.summary.config.name)):
            summary = vm.summary
            if summary.guest is not None:
                _ip_address = summary.guest.ipAddress
                if _ip_address is None:
                    _ip_address = ""
                _mac_address = []
                if vm.config is not None:
                    for dev in vm.config.hardware.device:
                        if isinstance(dev, vim.vm.device.VirtualEthernetCard):
                            _mac_address.append(dev.macAddress)

                virtual_machine = {
                    summary.config.name: {
                        "guest_fullname": summary.config.guestFullName,
                        "power_state": summary.runtime.powerState,
                        "ip_address": _ip_address,
                        "mac_address": _mac_address,
                        "uuid": summary.config.uuid
                     }
                 }

        _virtual_machines.update(virtual_machine)
    return _virtual_machines

def main():

    argument_spec = vmware_argument_spec()
    module = AnsibleModule(argument_spec=argument_spec, supports_check_mode=False)

    if not HAS_PYVMOMI:
        module.fail_json(msg='pyvmomi is required for this module')

    try:
        content = connect_to_api(module)
        _virtual_machines = get_kube_node_virtual_machines(content)
        module.exit_json(changed=False, virtual_machines=_virtual_machines)
    except vmodl.RuntimeFault as runtime_fault:
        module.fail_json(msg=runtime_fault.msg)
    except vmodl.MethodFault as method_fault:
        module.fail_json(msg=method_fault.msg)
    except Exception as e:
        module.fail_json(msg=str(e))


if __name__ == '__main__':
    main()
