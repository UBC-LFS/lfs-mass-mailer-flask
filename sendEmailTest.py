from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import email.message

import os
from dotenv import load_dotenv

load_dotenv()

HOST = ""
ALIAS_EMAIL = ""
ALIAS_NAME = ""
TRANSPORTER_OPTIONS = "smtpRelay"

if (TRANSPORTER_OPTIONS == "smtpRelay"):
    msg = email.message.Message()
    msg.add_header('Content-Type','text/html')
    msg['From'] = f"{ALIAS_NAME} <{ALIAS_EMAIL}>" 
    PORT = 25
    emailService = SMTP(host=HOST, port=PORT)

    msg['Subject'] = "Hello"
    message = f"""\
        <html>
        <head></head>
        <body>
            <p>Hello, World!</p>
        </body>
        </html>
    """
    msg.set_payload(message)
    msg['To'] = ""
    emailService.sendmail(msg['From'], msg['to'], msg.as_string())
    emailService.quit()
