# -*- coding: utf-8 -*-
#
# Reference:
# Python Quickstart https://developers.google.com/admin-sdk/directory/v1/quickstart/python
#

from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

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
    credential_path = os.path.join(credential_dir, 'token.pickle')

    if os.path.exists(credential_path):
        with open(credential_path, 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                CLIENT_SECRET_FILE, SCOPES)
            # https://google-auth-oauthlib.readthedocs.io/en/latest/reference/google_auth_oauthlib.flow.html
            # Run the flow using the server strategy.
            # creds = flow.run_local_server()
            # Run the flow using the console strategy
            creds = flow.run_console()
        # Save the credentials for the next run
        with open(credential_path, 'wb') as token:
            pickle.dump(creds, token)

    return creds
