#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2019 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

#############################################
#                WARNING                    #
#############################################
#
# This file is auto generated by the resource
#   module builder playbook.
#
# Do not edit this file manually.
#
# Changes to this file will be over written
#   by the resource module builder.
#
# Changes should be made in the model used to
#   generate this file or in the resource module
#   builder template.
#
#############################################

"""
The module file for cm71xx_node_description
"""

from __future__ import absolute_import, division, print_function
__metaclass__ = type

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': '<support_group>'
}

DOCUMENTATION = """
---
module: cm71xx_node_description
version_added: 2.9
short_description: 'Manages <xxxx> attributes of <network_os> <resource>.'
description: 'Manages <xxxx> attributes of <network_os> <resource>'
author: Ansible Network Engineer
notes:
  - 'Tested against <network_os> <version>'
options:
  config:
    description: The provided configuration
    type: dict
    suboptions:
      model_number:
        type: str
        description: The model
      serial_number:
        type: str
        description: The serial number
      hostname:
        type: str
        description: The hostname
      mac_address:
        type: str
        description: The MAC address
      firmware_version:
        type: str
        description: The version of the firmware
      interfaces:
        type: list
        elements: dict
        description: The interfaces
        suboptions:
          name:
            type: str
            description: The name of the interface
          ipv4_address:
            type: list
            elements: str
            description: The IPv4 addresses of the interface
          ipv6_address:
            type: list
            elements: str
            description: The IPv6 addresses of the interface
  state:
    description:
    - The state the configuration should be left in
    type: str
    choices:
    - merged
    - replaced
    - overridden
    - deleted
    default: merged
"""
EXAMPLES = """
"""
RETURN = """
before:
  description: The configuration prior to the model invocation.
  returned: always
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
after:
  description: The resulting configuration model invocation.
  returned: when changed
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
commands:
  description: The set of commands pushed to the remote device.
  returned: always
  type: list
  sample: ['command 1', 'command 2', 'command 3']
"""


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.opengear.cm71xx.plugins.module_utils.network.cm71xx.argspec.node_description.node_description import NodeDescriptionArgs
from ansible_collections.opengear.cm71xx.plugins.module_utils.network.cm71xx.config.node_description.node_description import NodeDescription


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    module = AnsibleModule(argument_spec=NodeDescriptionArgs.argument_spec,
                           supports_check_mode=True)

    result = NodeDescription(module).execute_module()
    module.exit_json(**result)


if __name__ == '__main__':
    main()
