#
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
The arg spec for the cm71xx_node_description module
"""


class NodeDescriptionArgs(object):  # pylint: disable=R0903
    """The arg spec for the cm71xx_node_description module
    """

    def __init__(self, **kwargs):
        pass

    argument_spec = {'config': {'options': {'firmware_version': {'type': 'str'},
                        'hostname': {'type': 'str'},
                        'interfaces': {'elements': 'dict',
                                       'options': {'ipv4_address': {'elements': 'str',
                                                                    'type': 'list'},
                                                   'ipv6_address': {'elements': 'str',
                                                                    'type': 'list'},
                                                   'name': {'type': 'str'}},
                                       'type': 'list'},
                        'mac_address': {'type': 'str'},
                        'model_number': {'type': 'str'},
                        'serial_number': {'type': 'str'}},
            'type': 'dict'},
 'state': {'choices': ['merged', 'replaced', 'overridden', 'deleted'],
           'default': 'merged',
           'type': 'str'}}  # pylint: disable=C0301
