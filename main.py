from flask import Flask, render_template, request, send_from_directory, redirect, url_for
from dotenv import load_dotenv

import sendEmail

load_dotenv()

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/sendemails', methods = ['POST'])
def getEmailContent():
    jsdata = request.form
    formattedData = jsdata.to_dict(flat=False)
    subject = formattedData["subject"][0]
    message = formattedData["HTMLemailContent"][0]
    variables = formattedData["varList[]"]
    recipients = sendEmail.buildReceiversData(formattedData, variables)
    sendEmail.sendEmails(recipients, subject, message, variables)
    return "Received email"

if __name__ == "__main__":
    app.run(debug=True)