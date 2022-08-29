# googlecli

Google Client that request to  Google Directory Api

# Function

| command | description |
| -- | --- |
| (user, group, group member) list | list objects in your domain |
| (user, group, group member) insert | insert(create) objects into your domain |
| (user, group, group member) update | update objects |
| (user, group, group member) delete | delete objects |
| (user, group) show | list details of the objects |


API Reference : 
https://developers.google.com/admin-sdk/directory/v1/reference/

# Prerequisites

- [Python Quickstart](https://developers.google.com/admin-sdk/directory/v1/quickstart/python)
  - Create a New Project
  - Enable Admin SDK API
  - Create credentials (OAuth client ID)
  - Input the Product name shown to users in OAuth consent screen tab
  - Select "Other" Application type and input the name of Client ID
  - Download the json file (client_secret_xxxxxxxxx.json)
  - Store this file into the `googlecli` directory (which is this repository's clone) and rename it "client_secret.json"

- Python 3.6+

# Install 

- This is an installation example on Linux

This example create `venv` into the `googlecli` folder, you can ajust where to create it. 

```sh
$ git clone https://github.com/kodamap/googlecli
$ python3 -m venv googlecli
$ cd googlecli; . bin/activate
(googlecli) $ pip install --upgrade pip
(googlecli) $ pip install -r requirements.txt
(googlecli) $ python setup.py build
(googlecli) $ python setup.py install
```

- Store the `client_secret.json`, which you created at the `Prerequisites`, into the `googlecli` directory.

```sh
(googlecli) $ ls /home/<username>/googlecli/client_secret.json
/home/<username>/googlecli/client_secret.json
```


# Role and Scopes

Default Scopes is `readonly`(see credentials.py). You need to have `G Suite Admin Role` in your domain. 

```py
# If modifying these scopes, delete your previously saved credentials "./.credentials/"
SCOPES = [
    'https://www.googleapis.com/auth/admin.directory.user.readonly',
    'https://www.googleapis.com/auth/admin.directory.group.readonly',
    'https://www.googleapis.com/auth/admin.directory.group.member.readonly'
]
```

if you want to `insert`, `update`, `delete` your resources using cli, change the scopes as below.

**Warning:** Before making these changes, you need to fully understand the meaning. I strongly recommend to verify  in the test environment.

```py
# If modifying these scopes, delete your previously saved credentials "./.credentials/"
SCOPES = [
    'https://www.googleapis.com/auth/admin.directory.user',
    'https://www.googleapis.com/auth/admin.directory.group',
    'https://www.googleapis.com/auth/admin.directory.group.member'
]
```


# How to use

```sh
$ googlectl user list
```

The first time it is run, the browser will launch and redirect to the following URL:

```
https://accounts.google.com/o/oauth2/auth/oauthchooseaccount?response_type=code&client_id=xxxx
```

Login to Google and authorize the permissions on the OAuth consent screen.

You need to permit the access to your Google Directory..
The permissions that you will be asked for are as below.

 - View and manage group subscriptions on your domain
 - View and manage the provisioning of groups on your domain
 - View and manage the provisioning of users on your domain


## examle

show usage (-h option)

```sh
$ googlectl user list -h
usage: googlectl user list [-h] [-f {csv,json,table,value,yaml}] [-c COLUMN]
                           [--quote {all,minimal,none,nonnumeric}]
                           [--noindent] [--max-width <integer>] [--fit-width]
                           [--print-empty] [--sort-column SORT_COLUMN]
                           [-n [NUMBER]]
```

list command returns 20 results ( no -n option : default value 20)

- user list

```sh
$ googlectl user list
+----------------------+--------------+---------+-------------+-----------+--------------------------+--------------------------+
| primaryEmail         | fullName     | isAdmin | orgUnitPath | suspended | creationTime             | lastLoginTime            |
+----------------------+--------------+---------+-------------+-----------+--------------------------+--------------------------+
| alice@yourdomain.com | alice aaa    | True    | /           | False     | 2010-01-01T00:00:00.000Z | 2018-01-01T00:00:00.000Z |
| bob@yourdomain.com   | bob bbb      | False   | /           | False     | 2010-01-01T00:00:00.000Z | 2018-01-01T00:00:00.000Z |
+----------------------+--------------+---------+-------------+-----------+--------------------------+--------------------------+
```

- group list

```sh
$ googlectl group list
+-----------------------------+------------------+--------------------+--------------+--------------+
| email                       | name             | directMembersCount | description  | adminCreated |
+-----------------------------+------------------+--------------------+--------------+--------------+
| group1@yourdomain.com       | group mail1      | 2                  | xxxxxxxxx    |  False       |
| group2@yourdomain.com       | group mail2      | 1                  | xxxxxxxxx    |  True        |
| group3@yourdomain.com       | group mail2      | 1                  | xxxxxxxxx    |  True        |
+-----------------------------+------------------+--------------------+--------------+--------------+
```

- member list (Getting the first 3 members in the group)

```sh
$ googlectl group member list -n 3 group1@yourdomain.com
+----------------------+--------+-------+--------+
| email                | role   | type  | status |
+----------------------+--------+-------+--------+
| alice@yourdomain.com | OWNER  | USER  | ACTIVE |
| bob@yourdomain.com   | MEMBER | USER  | ACTIVE |
| group@yourdomain.com | MEMBER | GROUP | ACTIVE |
+----------------------+--------+-------+--------+
```

- member list joined groups per user

```sh
googlectl group list -u alice@yourdomain.com
+-----------------------------+------------------+--------------------+--------------+--------------+
| email                       | name             | directMembersCount | description  | adminCreated |
+-----------------------------+------------------+--------------------+--------------+--------------+
| group1@yourdomain.com       | group mail1      | 3                  | xxxxxxxxx    |  False       |
| group2@yourdomain.com       | group mail2      | 3                  | xxxxxxxxx    |  True        |
+-----------------------------+------------------+--------------------+--------------+--------------+
```




- Show detail infomation of the user

```sh
$ googlectl user show alice@yourdomain.com
```

- Show detail infomation of the group

```sh
$ googlectl group show members@yourdomain.com
```

# Misc

- To reset credentilas , just remove credentials directory

```sh
$ rm -rf ~/.credentials/
```


Check your LANG Environment variable. Try "export LANG=en_US.UTF-8".

```sh
$ googlectl user show alice@yourdomain
'ascii' codec can't encode characters in position 371-373: ordinal not in range(128)
```

# Reference

- Admin Directory API

https://developers.google.com/admin-sdk/directory/reference/rest

- Python Quickstart

https://developers.google.com/admin-sdk/directory/v1/quickstart/python
