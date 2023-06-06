from flask import Flask, jsonify, render_template, request, send_from_directory, redirect, url_for
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
    # Render loading screen in HTML
    subject = formattedData["subject"][0]
    message = formattedData["HTMLemailContent"][0]
    variables = formattedData["varList[]"]
    recipients = sendEmail.buildReceiversData(formattedData, variables)
    receivers, failedReceivers = sendEmail.sendEmails(recipients, subject, message, variables)
    # Finish sending emails, render results in HTML
    return jsonify(success=1, output={"receivers":receivers,"failedReceivers":failedReceivers}, error=None)

if __name__ == "__main__":
    app.run(debug=True)