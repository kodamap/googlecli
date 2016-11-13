# googlecli
Google Client that request to  Google Directory Api

# Function
- user list
- group list
- member list
- user show
- group show

# Prerequisites
- Python Quickstart
https://developers.google.com/admin-sdk/directory/v1/quickstart/python
 - Create a New Project
 - Enable Admin SDK API
 - Create credentials (OAuth client ID)
 - Input the Product name shown to users in OAuth consent screen tab
 - Select "Other" Application type and input the name of Client ID
 - Download the json file (client_secret_xxxxxxxxx.json)
 - Move this file to your working directory and rename it "client_secret.json"
 
- Python3 (Optinal)
https://github.com/yyuu/pyenv
```
# yum install zlib-devel bzip2 bzip2-devel readline-devel sqlite sqlite-devel openssl-devel -y
```
you may also need patch and gcc.
```
# yum -y install patch gcc git
```
install python3
```
$ git clone https://github.com/yyuu/pyenv.git ~/.pyenv
$ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
$ echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
$ echo 'eval "$(pyenv init -)"' >> ~/.bash_profile
$ echo 'test -r ~/.bashrc && . ~/.bashrc' >> ~/.bash_profile
$ . ~/.bash_profile
$ pyenv install --list
$ pyenv install 3.5.2
$ pyenv global 3.5.2
$ python --version # Python 3.5.2
```

# Install 
- CentOS7
```
$ git clone https://github.com/kodamap/googlecli
$ cd googlecli
$ pip install --upgrade google-api-python-client
$ pip install -r requirements.txt
$ python setup.py build
$ python setup.py install
```
- store the client_secret.json that you creatd earlier.
```
$ ls  ~/client_secret.json
$ /home/user/client_secret.json
```

# How to use
You need to permit the access to your directory at the first time.
The permissons you will asked for are 
 - View users on your domain
 - View groups on your domain
 - View group subscriptions on your domain

Paste the URL to your browser and permit the access, then you will get the verification code.
```sh
$ googlectl user list
Go to the following link in your browser:
    https://accounts.google.com/o/oauth2/auth?scope=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
Enter verification code: <---- ** Input the verification code**
```
## examle
list command returns 20 results ( no -n option : default value 20)
- user list
```
$ googlectl user list
+-----------------------------+---------+
| PrimaryEmail                | isAdmin |
+-----------------------------+---------+
| alice@yourdomain.com        | False   |
| bob@yourdomain.com          | True    |
+-----------------------------+---------+
```
you can use it like openstack client
```sh
$ googlectl
(googlectl) user list
```
- group list
```
$ googlectl group list
+----------------------+-------------+
| Email                | Description |
+----------------------+-------------+
| members@yourdomain.com  | test     |
+----------------------+-------------+
```
- member list (Getting the first 3 members in the group)
```sh
$ googlectl member list -n 3 members@yourdomain.com
+-----------------------------+--------+
| Email                       | Role   |
+-----------------------------+--------+
| alice@yourdomain.com        | OWNER  |
| bob@yourdomain.com          | MEMBER |
| john@yourdomain.com         | MEMBER |
+-----------------------------+--------+
```
- Show detail infomation of the user
```sh
$ googlectl user show alice@yourdomain.com
```
- Show detail infomation of the group
```sh
$ googlectl group show members@yourdomain.com
```
- Misc
To rset credentilas , just remove credentials directory
```sh
$ rm -rf ~/.credentials/
```

# Reference
- Admin Directory API
https://developers.google.com/resources/api-libraries/documentation/admin/directory_v1/python/latest/index.html
- Python Quickstart
https://developers.google.com/admin-sdk/directory/v1/quickstart/python
