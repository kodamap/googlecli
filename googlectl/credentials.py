# -*- coding: utf-8 -*-
#
# Reference:
# Python Quickstart https://developers.google.com/admin-sdk/directory/v1/quickstart/python
#

import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

# If modifying these scopes, delete your previously saved credentials "./.credentials/"
"""
SCOPES = [
    'https://www.googleapis.com/auth/admin.directory.user',
    'https://www.googleapis.com/auth/admin.directory.group',
    'https://www.googleapis.com/auth/admin.directory.group.member'
]
"""
SCOPES = [
    'https://www.googleapis.com/auth/admin.directory.user.readonly',
    'https://www.googleapis.com/auth/admin.directory.group.readonly',
    'https://www.googleapis.com/auth/admin.directory.group.member.readonly'
]
CLIENT_SECRET_FILE = './client_secret.json'
APPLICATION_NAME = 'Google Directory API Python'


def get_credentials():

    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.

    current_dir = os.path.expanduser('./')
    credential_dir = os.path.join(current_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    ##credential_path = os.path.join(credential_dir, 'token.pickle')
    credential_path = os.path.join(credential_dir, 'token.json')

    if os.path.exists(credential_path):
        creds = Credentials.from_authorized_user_file(credential_path, SCOPES)
        ##with open(credential_path, 'rb') as token:
        ##    creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                CLIENT_SECRET_FILE, SCOPES)
            # Migrate the console strategy to the local server strategy
            # [Migrate your impacted OAuth out-of-band flow to an alternative method before Oct. 3, 2022]
            # https://developers.google.com/identity/protocols/oauth2/resources/oob-migration
            # https://developers.google.com/identity/protocols/oauth2/native-app#request-parameter-redirect_uri
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(credential_path, 'w') as token:
            token.write(creds.to_json())

    return creds
