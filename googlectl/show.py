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
        data = (result['primaryEmail'],
                result['fullName'],
                result['isAdmin'],
                result['creationTime'],
                result['lastLoginTime'],
                result['ipWhitelisted'],
                result['isDelegatedAdmin'],
                result['isMailboxSetup'],
                result['suspended'],
                result['emails'],
                result['customerId'],
                result['includeInGlobalAddressList'],
                result['changePasswordAtNextLogin'],
                result['agreedToTerms'],
                )
        return (columns, data)

class GroupShow(ShowOne):
    "Show detail information of group"

    log = logging.getLogger(__name__)

    def get_parser(self, prog_name):
        parser = super(GroupShow, self).get_parser(prog_name)
        parser.add_argument('groupid', nargs=None, default=None)
        return parser

    def take_action(self, parsed_args):
        client = googlectl.libgooglectl.Client()
        result = client.show_group(parsed_args.groupid)
        #print(result)
        columns = ('Email',
                   'Name',
                   'Description',
                   'directMembersCount',
                   'Id',
                   'AdminCreated',
                   )
        data = (result['email'],
                result['name'],
                result['description'],
                result['directMembersCount'],
                result['id'],
                result['adminCreated'],
                )
        return (columns, data)
