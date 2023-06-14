# lfs-mass-mailer-flask
An application to send mass emails via aliases, used internally by the LFS Learning Centre.

Note: Logging in with your CWL only works if you are connected to a UBC wifi

## Installation Set up

### Clone the repository
```
git clone https://github.com/UBC-LFS/lfs-mass-mailer-flask.git
```
```
pip install virtualenv
virtualenv venv
venv\Scripts\activate
pip install -r requirements.txt
```

Create a .env file and specify the following:
```
# LDAP
LDAP_URI=
LDAP_MEMBER_DN=
LDAP_AUTH_DN=
LDAP_AUTH_PASSWORD=
LDAP_SEARCH_FILTER=

# "smtp.mail.ubc.ca" OR "smtp.mail-relay.ubc.ca"
EMAIL_HOST=
# Sender's username and password (smpt option)
ACCOUNT_USER=
ACCOUNT_PASS=
# Alias (smptRelay option)
ALIAS_EMAIL=
ALIAS_NAME=
# "smpt" (default) OR "smptRelay"
TRANSPORTER_OPTIONS=
```

Run 
```
main.py
```
Go to: http://127.0.0.1:5000/ (localhost)