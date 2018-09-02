# -*- coding: utf-8 -*-
import logging
import os

from cliff.command import Command

import googlectl.libgooglectl

class UserDelete(Command):
    "Delete the group"

    log = logging.getLogger(__name__)

    def get_parser(self, prog_name):
        parser = super(UserDelete, self).get_parser(prog_name)
        parser.add_argument('email', nargs=None, default=None)
        return parser

    def take_action(self, parsed_args):
        client = googlectl.libgooglectl.Client()
        client.delete_user(parsed_args.email)

class GroupDelete(Command):
    "Delete the group"

    log = logging.getLogger(__name__)

    def get_parser(self, prog_name):
        parser = super(GroupDelete, self).get_parser(prog_name)
        parser.add_argument('groupkey', nargs=None, default=None)
        return parser

    def take_action(self, parsed_args):
        client = googlectl.libgooglectl.Client()
        client.delete_group(parsed_args.groupkey)


class GroupMemberDelete(Command):
    "Delete a member from the group"

    log = logging.getLogger(__name__)

    def get_parser(self, prog_name):
        parser = super(GroupMemberDelete, self).get_parser(prog_name)
        parser.add_argument('email', nargs=None, default=None)
        parser.add_argument('--groupkey', nargs=None, required=True, default=None)
        return parser

    def take_action(self, parsed_args):
        client = googlectl.libgooglectl.Client()
        client.delete_member(parsed_args.groupkey, parsed_args.email)
