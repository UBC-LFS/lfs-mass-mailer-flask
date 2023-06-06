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


def buildReceiversData(data, variables):
    recipients = []
    # Data is sent by ajax in a weird format
    # len(data) - 2 (removes the subject and email content from the data count)
    # divide by # of variables
    numOfRecipients = int((len(data) - 2)/len(variables))
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
                msg['From'] = USER
                msg.add_header('Content-Type','text/html')
                emailService = SMTP(host=HOST, port=PORT)
                emailService.ehlo()
                emailService.starttls()
                emailService.login(user=USER, password=PASSWORD, initial_response_ok=True)

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

# to = input("Who would you like to send this email to?: ")
# sendEmail(to)