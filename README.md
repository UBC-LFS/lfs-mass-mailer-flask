# LFS Mass Mailer (flask)
An application to send mass emails via aliases, used internally by the LFS Learning Centre.

**Note:** Logging in with your CWL and password only works if you are connected to a UBC wifi. This means would need to be connected to UBC wifi in order to use this application

## Prerequisites
1. Install [Python 3.7 or greater](https://www.python.org/downloads/).
2. Install [Git](https://git-scm.com/downloads).

## Installing and Setup
Clone this repo:
```
git clone https://github.com/UBC-LFS/lfs-mass-mailer-flask.git
```
Set up your virtual environment
```
pip install virtualenv
virtualenv venv
venv\Scripts\activate
pip install -r requirements.txt
```

Create a .env file and specify the following with quotes:
```
# LDAP
LDAP_URI=
LDAP_MEMBER_DN=
LDAP_AUTH_DN=
LDAP_AUTH_PASSWORD=
LDAP_SEARCH_FILTER=

# "smtp.mail.ubc.ca" OR "smtp.mail-relay.ubc.ca"
EMAIL_HOST=
# Sender's email (smtp option) or alias name(smtpRelay option)
ACCOUNT_USER=
# password only for smtp option
ACCOUNT_PASS=
# Alias email for smtpRelay option
ALIAS_EMAIL=
# "smtp" (default) OR "smtpRelay"
TRANSPORTER_OPTIONS=
```
### Running the website 
1. Run `main.py`
```
python main.py
```
2. Go to: http://127.0.0.1:5000/ (localhost)
3. Login with your CWL and Password (only works with UBC wifi)
4. Upload a .csv file containing at least a "Email" column then click "submit"
    - A template .csv file can be found [here](https://github.com/UBC-LFS/lfs-mass-mailer-flask/blob/main/static/template.csv)
    - The first 10 rows will be displayed
5. Scroll down and begin writing your email
    - You can insert variables into your email from your spreadsheet by surrounding it %, capitalizing it, and replacing spaces with underlines
6. Preview your email by clicking on the preview button
    - If you inserted variables, their values will be the values in the first row
7. Send your email(s)
8. A summary page will appear when all emails are sent. It will notify you of which emails were sent and which could not be sent.

## What each file does? (For future developers)
- main.py
    - runs the web server
    - validates LDAP logins
    - formats data sent from the frontend
    - sends results back to frontend
- sendEmail.py
    - code for sending out emails and formatting recipients data
- templates
    - index.html
        - Contains HTML code for the website elements
        - Contains JS code for:
            - creating the email preview + other pop ups
            - sending login info to the backend for validation
            - sending content to be emailed to the backend
    - footer.html (the website's footer)
    - navigationbar.html (the website's navigation bar)
- static
    - css (contains css files that style index.html and the navigation bar + footer)
    - javascript
        - createPreview.js
            - renders the email preview pop up
            - renders the email summary pop up (shows successful and unsuccessful emails sent)
        - login.js
            - saves users login auth status and sessionID
            - detect form "enter" events
        - uploadTable.js
            - process uploaded .csv file and displays table rows and summary
    - richtexteditor (the richtexteditor library - no need to modify this folder)