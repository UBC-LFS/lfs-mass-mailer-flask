import os
from flask import Flask, jsonify, render_template, request, send_from_directory, redirect, url_for
from dotenv import load_dotenv
from flask_login import LoginManager, login_user, UserMixin, current_user
from flask_ldap3_login import LDAP3LoginManager
from flask_ldap3_login.forms import LDAPLoginForm
from ldap3 import Tls
import ssl
import exrex

import sendEmail

load_dotenv()

app = Flask(__name__)

# Setup LDAP Configuration Variables. Change these to your own settings.
# All configuration directives can be found in the documentation.

# Hostname of your LDAP Server
app.config['LDAP_HOST'] = os.getenv("LDAP_URI")

# Port number of your LDAP server
app.config['LDAP_PORT'] = 636

# Base DN of your directory
app.config['LDAP_BASE_DN'] = os.getenv("LDAP_MEMBER_DN")

# Filters for finding user
app.config['LDAP_GROUP_OBJECT_FILTER'] = os.getenv("LDAP_SEARCH_FILTER")

# The Username to bind to LDAP with
app.config['LDAP_BIND_USER_DN'] = os.getenv("LDAP_AUTH_DN")

# The Password to bind to LDAP with
app.config['LDAP_BIND_USER_PASSWORD'] = os.getenv("LDAP_AUTH_PASSWORD")

# Specify the server connection should use SSL
app.config['LDAP_USE_SSL'] = True

# Instruct Flask-LDAP3-Login to not automatically add the server
app.config['LDAP_ADD_SERVER'] = False

login_manager = LoginManager(app)              # Setup a Flask-Login Manager
ldap_manager = LDAP3LoginManager(app)          # Setup a LDAP3 Login Manager.

# Init the mamager with the config since we aren't using an app
ldap_manager.init_config(app.config)

# Create a dictionary to store the users in when they authenticate
# This example stores users in memory.
users = {}

# Declare a User Loader for Flask-Login.
# Simply returns the User if it exists in our 'database', otherwise
# returns None.
@login_manager.user_loader
def load_user(id):
    if id in users:
        return users[id]
    return None


# Declare The User Saver for Flask-Ldap3-Login
# This method is called whenever a LDAPLoginForm() successfully validates.
# Here you have to save the user, and return it so it can be used in the
# login controller.
@ldap_manager.save_user
def save_user(sessionID, cwl):
    users[sessionID] = cwl

@app.route("/")
def home():
    print(users)
    return render_template("index.html")

@app.route('/login', methods = ['POST'])
def login():
    userLogin = request.form
    cwl = userLogin["cwl"]
    password = userLogin["password"]

    ldap_manager.add_server(
        app.config.get('LDAP_HOST'),
        app.config.get('LDAP_PORT'),
        app.config.get('LDAP_USE_SSL')
    )

    response = app.ldap3_login_manager.authenticate(cwl, password)
    if (str(response.status) == "AuthenticationResponseStatus.success"):
        sessionID = exrex.getone('((\d)|[A-Z]|[a-z]){40}')
        save_user(sessionID, cwl)

    else:
        sessionID = None
    print(response.status)

    return jsonify(success=1, output=sessionID)

@app.route('/sendemails', methods = ['POST'])
def getEmailContent():
    jsdata = request.form
    formattedData = jsdata.to_dict(flat=False)
    # Render loading screen in HTML
    subject = formattedData["subject"][0]
    message = formattedData["HTMLemailContent"][0]
    variables = formattedData["varList[]"]
    sessionID = formattedData["sessionID"][0]
    
    user = load_user(sessionID)
    if (user):
        print("Valid user!")
        recipients = sendEmail.buildReceiversData(formattedData, variables)
        receivers, failedReceivers = sendEmail.sendEmails(recipients, subject, message, variables)
        # Finish sending emails, render results in HTML
        return jsonify(success=1, output={"receivers":receivers,"failedReceivers":failedReceivers}, error=None)
    else:
        print("Invalid user!")
        return jsonify(success=1, output="authFailed", error=None)

@app.route('/logout', methods=['POST'])
def logout():
    jsdata = request.form
    sessionID = jsdata.to_dict(flat=False)["data"][0]
    users.pop(sessionID, None)
    return "logged out"

if __name__ == "__main__":
    app.run(debug=True)