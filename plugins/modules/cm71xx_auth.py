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
The module file for cm71xx_auth
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
module: cm71xx_auth
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
      auth_type:
        type: str
        description: The auth type
      use_remote_groups:
        description: Use remote groups
        type: bool
      tacas:
        type: dict
        description: The tacas configuration
        suboptions:
          auth_server:
            type: str
            description: The auth server
          auth_method:
            type: str
            description: The auth method
          service:
            type: str
            description: The service
      radius:
        type: dict
        description: The radius configuration
        suboptions:
          password:
            type: str
            description: The password
          auth_server:
            type: str
            description: The auth server
          acct_server:
            type: str
            description: The acct server
      ldap:
        type: dict
        description: The ldap configuration
        suboptions:
          server:
            type: str
            description: The server
          bind_dn:
            type: str
            description: The bind DN
          base_dn:
            type: str
            description: The base DN
          bind_password:
            type: str
            description: The bind password
          username_attr:
            type: str
            description: The username attribute
          group_membership_attr:
            type: str
            description: The group membership attribute
          protocol:
            type: str
            description: The protocol
            choices:
              - ldaps_preferred
              - ldaps_only
              - ldap_only
            default: ldaps_preferred
          ignore_ssl_errors:
            type: bool
            description: Ignore SSL errors
            default: false
          ca_cert:
            type: str
            description: The CA certificate
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
from ansible_collections.opengear.cm71xx.plugins.module_utils.network.cm71xx.argspec.auth.auth import AuthArgs
from ansible_collections.opengear.cm71xx.plugins.module_utils.network.cm71xx.config.auth.auth import Auth


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    module = AnsibleModule(argument_spec=AuthArgs.argument_spec,
                           supports_check_mode=True)

    result = Auth(module).execute_module()
    module.exit_json(**result)


if __name__ == '__main__':
    main()
