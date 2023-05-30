from flask import Flask, render_template, request, send_from_directory, redirect, url_for
from dotenv import load_dotenv

import sendEmail

load_dotenv()

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/sendemails', methods = ['POST'])
def sendEmails():
    jsdata = request.form
    formattedData = jsdata.to_dict(flat=False)
    subject = formattedData['data[subject]'][0]
    print(subject)
    message = formattedData['data[HTMLemailContent]'][0]
    print(message)
    return "Received email"

if __name__ == "__main__":
    app.run(debug=True)