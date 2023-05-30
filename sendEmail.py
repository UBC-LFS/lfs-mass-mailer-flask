from smtplib import SMTP
import os
from dotenv import load_dotenv

load_dotenv()

HOST = os.getenv("HOST")
PORT = os.getenv("PORT")
USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")

def sendEmail(to):
    try:
        emailService = SMTP(host=HOST, port=PORT)
        emailService.ehlo()
        emailService.starttls()
        emailService.login(user=USER, password=PASSWORD, initial_response_ok=True)
        emailService.sendmail(
            USER,
            to,
            'Subject: Test \n\n This is a test email!')
        emailService.quit()
        print("Successfully sent email")

    except Exception as e:
       print("\nError:\n" + str(e) + "\n")

# to = input("Who would you like to send this email to?: ")
# sendEmail(to)