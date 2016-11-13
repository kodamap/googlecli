import googlectl.credentials
import httplib2
from apiclient import discovery

def create_service():
    credential = googlectl.credentials.get_credentials()
    http = credential.authorize(httplib2.Http())
    service = discovery.build('admin', 'directory_v1', http=http)
    return service

class Client(object):
    def __init__(self):
        pass
        #self.client = googlectl.Credentials.get_credentials()
        #http = self.client.authorize(httplib2.Http())
        #service = discovery.build('admin', 'directory_v1', http=http)

        #if not self.service:
        #    raise RuntimeError('API test failed')

    def list_users(self, number):
        print('Getting the first ' + str(number) +' users in the domain')

        service = create_service()
        result = service.users().list(
            customer='my_customer',
            maxResults=number,
            orderBy='email').execute()

        users = result.get('users', [])

        if not users:
            return {}

        users = {user['primaryEmail']: user['isAdmin'] for user in result['users']}
        return users

    def list_groups(self, number):
        print('Getting the first ' + str(number) +' groups in the domain')

        service = create_service()
        result = service.groups().list(
            customer='my_customer',
            maxResults=number
            ).execute()

        groups = result.get('groups', [])

        if not groups:
            return {}

        groups = {group['email']: group['description'] for group in result['groups']}
        return groups

    def list_members(self, groupid, number):
        print('Getting the first ' + str(number) +' members in the group')

        service = create_service()
        result = service.members().list(
            groupKey=groupid,
            maxResults=number).execute()

        members = result.get('members', [])

        if not members:
            return {}

        members = {member['email']: member['role'] for member in result['members']}
        return members

    def show_user(self, email):
        print('Getting the infomation details: ' + email)

        service = create_service()
        result = service.users().get(userKey=email).execute()

        if not result:
            return {}

        data = {
            'primaryEmail': result['primaryEmail'],
            'fullName': result['name']['fullName'],
            'isAdmin': result['isAdmin'],
            'creationTime': result['creationTime'],
            'lastLoginTime': result['lastLoginTime'],
            'ipWhitelisted': result['ipWhitelisted'],
            'isDelegatedAdmin': result['isDelegatedAdmin'],
            'isMailboxSetup': result['isMailboxSetup'],
            'suspended': result['suspended'],
            'emails': result['emails'],
            'customerId': result['customerId'],
            'includeInGlobalAddressList': result['includeInGlobalAddressList'],
            'changePasswordAtNextLogin': result['changePasswordAtNextLogin'],
            'agreedToTerms': result['agreedToTerms']
        }
        return data

    def show_group(self, groupid):
        print('Getting the infomation details: ' + groupid)

        service = create_service()
        result = service.groups().get(groupKey=groupid).execute()

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