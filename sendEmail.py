from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import email.message

import os
from dotenv import load_dotenv

load_dotenv()

HOST = os.getenv("EMAIL_HOST")
USER = os.getenv("ACCOUNT_USER")
PASSWORD = os.getenv("ACCOUNT_PASS")
ALIAS_EMAIL = os.getenv("ALIAS_EMAIL")
ALIAS_NAME = os.getenv("ALIAS_NAME")
TRANSPORTER_OPTIONS = os.getenv("TRANSPORTER_OPTIONS")

def buildReceiversData(data, variables):
    recipients = []
    # Data is sent by ajax in a weird format
    # len(data) - 3 (removes the subject, email content, and sessionID from the data count)
    # divide by # of variables
    numOfRecipients = int((len(data) - 3)/len(variables))
    for i in range(numOfRecipients):
        recipient = {}
        for var in variables:
            recipient[var] = data[f"receivers[{i}][{var}]"][0]
        recipients.append(recipient)
    return recipients

def sendEmails(recipients, subject, draftMessage, variables):
    receivers = []
    try:
        for i in range(len(recipients)):
            try:
                msg = email.message.Message()
                msg.add_header('Content-Type','text/html')

                if (TRANSPORTER_OPTIONS == "smtp"):
                    msg['From'] = USER 
                    PORT = 587
                    emailService = SMTP(host=HOST, port=PORT)
                    emailService.ehlo()
                    emailService.starttls()
                    emailService.login(user=USER, password=PASSWORD, initial_response_ok=True)
                
                # smtpRelay (default)
                else:
                    msg['From'] = f"{ALIAS_NAME} <{ALIAS_EMAIL}>" 
                    PORT = 25
                    emailService = SMTP(host=HOST, port=PORT)
                    
                modifiedSubject = subject
                modifiedDraftMessage = draftMessage
                # If user adds a variable into their subject or message, replace it with the actual value
                for var in variables:
                    insertedVar = f"%{var.replace(' ', '_').upper()}%"
                    modifiedSubject = modifiedSubject.replace(insertedVar, recipients[i][var])
                    modifiedDraftMessage = modifiedDraftMessage.replace(insertedVar, recipients[i][var])

                msg['Subject'] = modifiedSubject
                message = f"""\
                    <html>
                    <head></head>
                    <body>
                        {modifiedDraftMessage}
                    </body>
                    </html>
                """
                msg.set_payload(message)
                msg['To'] = recipients[i]["Email"] 
                emailService.sendmail(msg['From'], msg['to'], msg.as_string())
                receivers.append(recipients[i])
                emailService.quit()
            # If it fails to send an email
            except Exception as e:
                print("\nError:\n" + str(e) + "\n")
                print("Failed to send email to:")
                print(recipients[i])

    except Exception as e:
       print("\nError:\n" + str(e) + "\n")
    print("Successfully sent emails")

    failedReceivers = [failedReceiver for failedReceiver in recipients if failedReceiver not in receivers]
    return receivers, failedReceivers 
