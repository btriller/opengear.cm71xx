#
# -*- coding: utf-8 -*-
# Copyright 2019 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The arg spec for the cm71xx facts module.
"""


class FactsArgs(object):  # pylint: disable=R0903
    """ The arg spec for the cm71xx facts module
    """

    def __init__(self, **kwargs):
        pass

    choices = [
        'all',
        'auth',
        'groups',
        'node_description',
        'system',
        'users',
    ]

    argument_spec = {
        'gather_subset': dict(default=['!config'], type='list'),
        'gather_network_resources': dict(choices=choices,
                                         type='list'),
    }
