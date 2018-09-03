# -*- coding: utf-8 -*-
import logging
import os

from cliff.show import ShowOne

import googlectl.libgooglectl

class UserInsert(ShowOne):
    "Insert a user"

    log = logging.getLogger(__name__)

    def get_parser(self, prog_name):
        parser = super(UserInsert, self).get_parser(prog_name)
        parser.add_argument('email', nargs=None, default=None)
        parser.add_argument('--password', nargs='?', required=True, default=None)
        parser.add_argument('--givenname', nargs='?', default=None)
        parser.add_argument('--familyname', nargs='?', default=None)
        parser.add_argument('--isAdmin', nargs='?', default=False)
        return parser

    def take_action(self, parsed_args):
        client = googlectl.libgooglectl.Client()

        userinfo = {
            "name": {
                "givenName": parsed_args.givenname,
                "familyName": parsed_args.familyname,
            },
            "primaryEmail": parsed_args.email,
            "password": parsed_args.password,
            "isAdmin": parsed_args.isAdmin,
        }
        result = client.insert_user(userinfo)
        columns = ('id',
                   'primaryEmail',
                   'givenName',
                   'familyName',
                   'isAdmin',
                   'isDelegatedAdmin',
                   )
        data = (result['id'],
                result['primaryEmail'],
                result['name']['givenName'],
                result['name']['familyName'],
                result['isAdmin'],
                result['isDelegatedAdmin'],
                )
        return (columns, data)

class GroupInsert(ShowOne):
    "Insert a group"

    log = logging.getLogger(__name__)

    def get_parser(self, prog_name):
        parser = super(GroupInsert, self).get_parser(prog_name)
        parser.add_argument('email', nargs=None, default=None)
        parser.add_argument('--description', nargs='?', default=None)
        parser.add_argument('--name', nargs='?', default=None)
        return parser

    def take_action(self, parsed_args):
        client = googlectl.libgooglectl.Client()
        groupinfo = {
            "email": parsed_args.email,
            "description": parsed_args.description,
            "name": parsed_args.name
        }
        result = client.insert_group(groupinfo)
        columns = ('id',
                   'email',
                   'name',
                   'description',
                   )
        data = (result['id'],
                result['email'],
                result['name'],
                result['description'],
                )
        return (columns, data)


class GroupMemberInsert(ShowOne):
    "Insert a member into the group"

    log = logging.getLogger(__name__)

    def get_parser(self, prog_name):
        parser = super(GroupMemberInsert, self).get_parser(prog_name)
        parser.add_argument('email', nargs=None, default=None)
        parser.add_argument('--groupkey', nargs=None, required=True, default=None)
        parser.add_argument('--role', nargs='?', default="MEMBER")
        return parser

    def take_action(self, parsed_args):
        client = googlectl.libgooglectl.Client()
        memberinfo = {
            'email': parsed_args.email,
            'role': parsed_args.role
        }
        result = client.insert_member(parsed_args.groupkey, memberinfo)
        columns = ('id',
                   'email',
                   'role',
                   'type',
                   'status',
                   )
        data = (result['id'],
                result['email'],
                result['role'],
                result['type'],
                result['status'],
                )
        return (columns, data)


