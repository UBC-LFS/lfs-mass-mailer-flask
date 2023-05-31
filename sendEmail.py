from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import email.message

import os
from dotenv import load_dotenv

load_dotenv()

HOST = os.getenv("HOST")
PORT = os.getenv("PORT")
USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")

def sendEmails(to, subject, draftMessage):
    message = f"""\
        <html>
        <head></head>
        <body>
            {draftMessage}
        </body>
        </html>
    """
    msg = email.message.Message()
    msg['Subject'] = subject
    msg['From'] = to
    msg['To'] = to
    msg.add_header('Content-Type','text/html')
    msg.set_payload(message)

    try:
        emailService = SMTP(host=HOST, port=PORT)
        emailService.ehlo()
        emailService.starttls()
        emailService.login(user=USER, password=PASSWORD, initial_response_ok=True)
        emailService.sendmail(msg['From'], msg['to'], msg.as_string())
        emailService.quit()
        print("Successfully sent email")

    except Exception as e:
       print("\nError:\n" + str(e) + "\n")

# to = input("Who would you like to send this email to?: ")
# sendEmail(to)