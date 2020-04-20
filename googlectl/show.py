# -*- coding: utf-8 -*-
import logging
import os

from cliff.show import ShowOne

import googlectl.libgooglectl


class UserShow(ShowOne):
    "Show detail information of user"

    log = logging.getLogger(__name__)

    def get_parser(self, prog_name):
        parser = super(UserShow, self).get_parser(prog_name)
        parser.add_argument('email', nargs=None, default=None)
        return parser

    def take_action(self, parsed_args):
        client = googlectl.libgooglectl.Client()
        result = client.show_user(parsed_args.email)
        #print(result)
        columns = ('primaryEmail',
                   'id',
                   'fullName',
                   'isAdmin',
                   'creationTime',
                   'lastLoginTime',
                   'ipWhitelisted',
                   'isDelegatedAdmin',
                   'isMailboxSetup',
                   'suspended',
                   'emails',
                   'customerId',
                   'includeInGlobalAddressList',
                   'changePasswordAtNextLogin',
                   'agreedToTerms',
                   )
        data = (result.get('primaryEmail'), 
                result.get('id'),
                result.get('fullName'),
                result.get('isAdmin'),
                result.get('creationTime'),
                result.get('lastLoginTime'),
                result.get('ipWhitelisted'),
                result.get('isDelegatedAdmin'),
                result.get('isMailboxSetup'),
                result.get('suspended'),
                result.get('emails'),
                result.get('customerId'),
                result.get('includeInGlobalAddressList'),
                result.get('changePasswordAtNextLogin'),
                result.get('agreedToTerms'),
                )
        return (columns, data)


class GroupShow(ShowOne):
    "Show detail information of group"

    log = logging.getLogger(__name__)

    def get_parser(self, prog_name):
        parser = super(GroupShow, self).get_parser(prog_name)
        parser.add_argument('groupkey', nargs=None, default=None)
        return parser

    def take_action(self, parsed_args):
        client = googlectl.libgooglectl.Client()
        result = client.show_group(parsed_args.groupkey)
        #print(result)
        columns = ('email',
                   'id',
                   'name',
                   'directMembersCount',
                   'description',
                   'AdminCreated', )
        data = (result.get('email'),
                result.get('id'),
                result.get('name'), 
                result.get('directMembersCount'),
                result.get('description'),
                result.get('adminCreated'),
                )
        return (columns, data)
