#
# -*- coding: utf-8 -*-
# Copyright 2019 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The facts class for cm71xx
this file validates each subset of facts and selectively
calls the appropriate facts gathering function
"""

from ansible_collections.opengear.cm71xx.plugins.module_utils.network.cm71xx.argspec.facts.facts import FactsArgs
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.facts.facts import (
    FactsBase,
)
from ansible_collections.opengear.cm71xx.plugins.module_utils.network.cm71xx.facts.auth.auth import AuthFacts
from ansible_collections.opengear.cm71xx.plugins.module_utils.network.cm71xx.facts.groups.groups import GroupsFacts
from ansible_collections.opengear.cm71xx.plugins.module_utils.network.cm71xx.facts.node_description.node_description import NodeDescriptionFacts
from ansible_collections.opengear.cm71xx.plugins.module_utils.network.cm71xx.facts.system.system import SystemFacts
from ansible_collections.opengear.cm71xx.plugins.module_utils.network.cm71xx.facts.users.users import UsersFacts


FACT_LEGACY_SUBSETS = {}
FACT_RESOURCE_SUBSETS = dict(
    auth=AuthFacts,
    groups=GroupsFacts,
    node_description=NodeDescriptionFacts,
    system=SystemFacts,
    users=UsersFacts,
)


class Facts(FactsBase):
    """ The fact class for cm71xx
    """

    VALID_LEGACY_GATHER_SUBSETS = frozenset(FACT_LEGACY_SUBSETS.keys())
    VALID_RESOURCE_SUBSETS = frozenset(FACT_RESOURCE_SUBSETS.keys())

    def __init__(self, module):
        super(Facts, self).__init__(module)

    def get_facts(self, legacy_facts_type=None, resource_facts_type=None, data=None):
        """ Collect the facts for cm71xx

        :param legacy_facts_type: List of legacy facts types
        :param resource_facts_type: List of resource fact types
        :param data: previously collected conf
        :rtype: dict
        :return: the facts gathered
        """
        netres_choices = FactsArgs.argument_spec['gather_network_resources'].get('choices', [])
        if self.VALID_RESOURCE_SUBSETS:
            self.get_network_resources_facts(FACT_RESOURCE_SUBSETS, resource_facts_type, data)

        if self.VALID_LEGACY_GATHER_SUBSETS:
            self.get_network_legacy_facts(FACT_LEGACY_SUBSETS, legacy_facts_type)

        return self.ansible_facts, self._warnings
