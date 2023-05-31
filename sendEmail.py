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


def buildReceiversData(data):
    recipients = []
    # Data is sent by ajax in a weird format
    # len(data) - 2 (removes the subject and email content)
    # divide by 3 (each recipient has an email, first name, and last name)
    numOfRecipients = int((len(data) - 2)/3)
    for i in range(numOfRecipients):
        receivers = data[f"receivers[{i}][First Name]"][0]
        recipient = {
            "firstName": data[f"receivers[{i}][First Name]"][0],
            "lastName": data[f"receivers[{i}][Last Name]"][0],
            "email": data[f"receivers[{i}][Email]"][0]
        }
        recipients.append(recipient)
    return recipients

def sendEmails(recipients, subject, draftMessage):
    try:
        for i in range(len(recipients)):
            msg = email.message.Message()
            msg['From'] = USER
            msg.add_header('Content-Type','text/html')
            emailService = SMTP(host=HOST, port=PORT)
            emailService.ehlo()
            emailService.starttls()
            emailService.login(user=USER, password=PASSWORD, initial_response_ok=True)
            modifiedSubject = subject.replace(f"%FIRST_NAME%", recipients[i]["firstName"]).replace(f"%LAST_NAME%", recipients[i]["lastName"])
            msg['Subject'] = modifiedSubject
            modifiedDraftMessage = draftMessage.replace(f"%FIRST_NAME%", recipients[i]["firstName"]).replace(f"%LAST_NAME%", recipients[i]["lastName"])
            message = f"""\
                <html>
                <head></head>
                <body>
                    {modifiedDraftMessage}
                </body>
                </html>
            """
            msg.set_payload(message)
            msg['To'] = recipients[i]["email"] 
            emailService.sendmail(msg['From'], msg['to'], msg.as_string())
        
        emailService.quit()
        print("Successfully sent email")

    except Exception as e:
       print("\nError:\n" + str(e) + "\n")

# to = input("Who would you like to send this email to?: ")
# sendEmail(to)