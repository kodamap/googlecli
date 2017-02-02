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

- Python3 (Recommeded) 
https://github.com/yyuu/pyenv

```sh
$ sudo yum install zlib-devel bzip2 bzip2-devel readline-devel sqlite sqlite-devel openssl-devel -y
```
you may also need to install patch and gcc.
```sh
$ sudo yum -y install patch gcc make git
```
install python3
```sh
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
- Installation on CentOS7
```sh
$ git clone https://github.com/kodamap/googlecli
$ cd googlecli
$ pip install --upgrade google-api-python-client
$ pip install -r requirements.txt
$ python setup.py build
$ python setup.py install
$ . ~/.bash_profile
```
- Store the "client_secret.json" you created earlier.
```sh
$ ls  ~/client_secret.json
/home/user/client_secret.json
```

# How to use
At first You need to permit the access to your Google Directory.
The permissions that you will be asked for are as below.
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
```sh
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
```sh
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

# Misc
- To reset credentilas , just remove credentials directory
```sh
$ rm -rf ~/.credentials/
```
- ascii codec can't Error
Error occurs when you use python2.7+ . Use Python3.
```sh
$ googlectl group list -f csv
'ascii' codec can't decode byte 0xe3 in position 31: ordinal not in range(128)
```
Check your LANG Environment variable. Try "export LANG=en_US.UTF-8".
```sh
$ googlectl user show alice@yourdomain
'ascii' codec can't encode characters in position 371-373: ordinal not in range(128)
```

# for docker
```sh
$ git clone https://github.com/kodamap/googlecli
$ cd googlecli
$ docker build -t centos/googlecli:ver1.0 dockerfiles
$ docker run -itd --name googlecli centos/googlecli:ver1.0 /bin/bash
$ docker ps
CONTAINER ID        IMAGE                     COMMAND             CREATED             STATUS              PORTS               NAMES
fc3d02b55084        centos/googlecli:ver1.0   "/bin/bash"         2 minutes ago       Up 2 minutes                            googlecli
$ docker exec -it googlecli /bin/bash
[root@fc3d02b55084 /]# . /root/.bash_profile
[root@fc3d02b55084 /]# googlectl -h
usage: googlectl [--version] [-v | -q] [--log-file LOG_FILE] [-h] [--debug]
```

# Reference
- Admin Directory API
https://developers.google.com/resources/api-libraries/documentation/admin/directory_v1/python/latest/index.html
- Python Quickstart
https://developers.google.com/admin-sdk/directory/v1/quickstart/python
