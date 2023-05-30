from flask import Flask, render_template, send_from_directory, redirect, url_for
from dotenv import load_dotenv

import sendEmail

load_dotenv()

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)