# -*- coding: utf-8 -*-

import googlectl.credentials
from googleapiclient.discovery import build

class Client(object):
    def __init__(self):
        self.credentials = googlectl.credentials.get_credentials()
        self.service = build('admin', 'directory_v1', credentials=self.credentials, cache_discovery=False)

    def yes_no(self, question):
        while "the answer is invalid":
            reply = str(input(question + ' (y/n): ')).lower().strip()
            if reply[:1] == 'y':
                return True
            if reply[:1] == 'n':
                return False

    def list_users(self, number):
        print("Getting the first {} users in the domain".format(str(number)))
        result = self.service.users().list(
            customer='my_customer', maxResults=number,
            orderBy='email').execute()
        users = result.get('users', [])
        if not users:
            return {}
        users = {
            user['primaryEmail']: user['isAdmin']
            for user in result['users']
        }
        return users

    def list_groups(self, userkey, number):
        print("Getting the first {} groups in the domain".format(str(number)))
        if userkey:
            result = self.service.groups().list(
                userKey=userkey, maxResults=number).execute()
        else:
            result = self.service.groups().list(
                customer='my_customer', maxResults=number).execute()
        groups = result.get('groups', [])
        if not groups:
            return {}
        groups = {
            group['email']: group['description']
            for group in result['groups']
        }
        return groups

    def list_members(self, groupkey, number):
        print("Getting the first {} members in the group {}".format(
            str(number), groupkey))
        result = self.service.members().list(
            groupKey=groupkey, maxResults=number).execute()

        members = result.get('members', [])
        if not members:
            return {}
        members = {
            member['email']: member['role']
            for member in result['members']
        }
        return members

    def show_user(self, email):
        print("Getting the infomation details: {}".format(email))
        result = self.service.users().get(userKey=email).execute()
        groups = self.service.groups().list(
            userKey=email, maxResults=200).execute()
        if not result:
            return {}
        data = {
            'primaryEmail':
            result['primaryEmail'],
            'fullName':
            result['name']['fullName'],
            'isAdmin':
            result['isAdmin'],
            'creationTime':
            result['creationTime'],
            'lastLoginTime':
            result['lastLoginTime'],
            'ipWhitelisted':
            result['ipWhitelisted'],
            'isDelegatedAdmin':
            result['isDelegatedAdmin'],
            'isMailboxSetup':
            result['isMailboxSetup'],
            'suspended':
            result['suspended'],
            'emails':
            result['emails'],
            'customerId':
            result['customerId'],
            'includeInGlobalAddressList':
            result['includeInGlobalAddressList'],
            'changePasswordAtNextLogin':
            result['changePasswordAtNextLogin'],
            'agreedToTerms':
            result['agreedToTerms'],
            'joinedGroups': [
                groups['groups'][i]['email']
                for i in range(len(groups['groups']))
            ]
        }
        return data

    def show_group(self, groupkey):
        print("Getting the infomation details: {}".format(groupkey))
        result = self.service.groups().get(groupKey=groupkey).execute()
        if not result:
            return {}
        data = {
            'email': result['email'],
            'name': result['name'],
            'description': result['description'],
            'directMembersCount': result['directMembersCount'],
            'id': result['id'],
            'adminCreated': result['adminCreated']
        }
        return data

    def insert_user(self, userinfo):
        print("Inserting user in the domain")
        result = self.service.users().insert(body=userinfo).execute()
        return result

    def insert_group(self, groupinfo):
        print("Inserting a group in the domain")
        result = self.service.groups().insert(body=groupinfo).execute()
        return result

    def insert_member(self, groupkey, memberinfo):
        print("Inserting {} into {} as {} role".format(memberinfo[
            'email'], groupkey, memberinfo['role']))
        result = self.service.members().insert(
            groupKey=groupkey, body=memberinfo).execute()
        return result

    def delete_user(self, email):
        print("Deleting a user {} in the domain".format(email))
        result = self.service.users().delete(userKey=email).execute()
        return result

    def delete_group(self, groupkey):
        print("Deleting a group {} in the domain".format(groupkey))
        result = self.service.groups().delete(groupKey=groupkey).execute()
        return result

    def delete_member(self, groupkey, email):
        print("Deleting {} from {}".format(email, groupkey))
        result = self.service.members().delete(
            groupKey=groupkey, memberKey=email).execute()
        return result

    def update_user(self, email, userinfo):
        print("Updating userinfo of {} in the domain".format(email))
        result = self.service.users().update(
            userKey=email, body=userinfo).execute()
        return result

    def update_group(self, groupkey, groupinfo):
        print("Updating groupinfo of {} info in the domain".format(groupkey))
        result = self.service.groups().update(
            groupKey=groupkey, body=groupinfo).execute()
        return result

    def update_member(self, groupkey, email, memberinfo):
        print("Updating {} in {} as {} role".format(memberinfo[
            'email'], groupkey, memberinfo['role']))
        result = self.service.members().update(
            groupKey=groupkey, memberKey=email, body=memberinfo).execute()
        return result
