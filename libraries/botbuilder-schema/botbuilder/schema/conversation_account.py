# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ConversationAccount(Model):
    """Channel account information for a conversation.

    :param is_group: Is this a reference to a group
    :type is_group: bool
    :param id: Channel id for the user or bot on this channel (Example:
     joe@smith.com, or @joesmith or 123456)
    :type id: str
    :param name: Display friendly name
    :type name: str
    """

    _attribute_map = {
        'is_group': {'key': 'isGroup', 'type': 'bool'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ConversationAccount, self).__init__(**kwargs)
        self.is_group = kwargs.get('is_group', None)
        self.id = kwargs.get('id', None)
        self.name = kwargs.get('name', None)
