import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import email.message

import os
from dotenv import load_dotenv

load_dotenv()

HOST = os.getenv("EMAIL_HOST")
PORT = os.getenv("PORT")
USER = os.getenv("ACCOUNT_USER")
PASSWORD = os.getenv("ACCOUNT_PASS")

ALIAS_EMAIL = os.getenv("ACCOUNT_EMAIL")
ALIAS_NAME = os.getenv("ACCOUNT_NAME")

msg = email.message.Message()
msg['Subject'] = "HELLO"
msg['From']    = f"{ALIAS_NAME} <{ALIAS_EMAIL}>" # Your from name and email address
msg['To']      = USER

msg.set_payload("Hi")
server = smtplib.SMTP(host=HOST, port=587)
server.ehlo()
server.starttls()
server.login(user=USER, password=PASSWORD)
server.sendmail(msg['From'], msg['To'], msg.as_string())
server.close()
