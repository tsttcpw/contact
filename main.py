#!/usr/bin/env python
import requests
from flask import Flask, render_template, request
import os
from datetime import datetime
from telegram import send_message

send_message("test message")
app = Flask(__name__, root_path=os.getcwd())
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
