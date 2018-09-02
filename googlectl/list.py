# -*- coding: utf-8 -*-
import datetime
import logging
import os

from cliff.lister import Lister

import googlectl.libgooglectl

def _append_global_args(parser):
    parser.add_argument('-n', '--number', \
        action='store', \
        nargs='?', \
        const=None, \
        default=20, \
        type=str, \
        choices=None, \
        help='The numbers of list (default: 20)', \
        metavar=None)
    return parser

class UserList(Lister):
    "Show a list of Users in the domain."

    log = logging.getLogger(__name__)

    def get_parser(self, prog_name):
        parser = super(UserList, self).get_parser(prog_name)
        parser = _append_global_args(parser)
        return parser

    def take_action(self, parsed_args):
        client = googlectl.libgooglectl.Client()
        users = client.list_users(parsed_args.number)
        #print(users)
        return (('PrimaryEmail', 'isAdmin'),
                ((primaryemail, users[primaryemail]) for primaryemail in users)
                )

class GroupList(Lister):
    "Show a list of groups in the domain."

    log = logging.getLogger(__name__)

    def get_parser(self, prog_name):
        parser = super(GroupList, self).get_parser(prog_name)
        parser = _append_global_args(parser)
        return parser

    def take_action(self, parsed_args):
        client = googlectl.libgooglectl.Client()
        groups = client.list_groups(parsed_args.number)
        return (('Email', 'Description'),
                ((email, groups[email]) for email in groups)
                )

class GroupMemberList(Lister):
    "Show a Group Member List of the group in the domain."

    log = logging.getLogger(__name__)

    def get_parser(self, prog_name):
        parser = super(GroupMemberList, self).get_parser(prog_name)
        parser = _append_global_args(parser)
        parser.add_argument('groupkey', nargs=None, default=None)
        return parser

    def take_action(self, parsed_args):
        client = googlectl.libgooglectl.Client()
        members = client.list_members(parsed_args.groupkey,parsed_args.number)

        return (('Email', 'Role'),
                ((email, members[email]) for email in members)
                )
