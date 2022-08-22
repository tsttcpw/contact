#!/usr/bin/env python
import requests
from flask import Flask, render_template, request
import os
from datetime import datetime
from telegram import send_message

app = Flask(__name__, root_path=os.getcwd())


@app.route('/', methods=['GET', 'POST'])
def receive_data():
    print(request.method)
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        telegram = request.form['telegram_id']
        message = request.form['message']
        agree = request.form['agree']
        message_text = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nTelegram: @{telegram}\nMessage: {message}\nAgree:{agree}"
        send_message(message_text)
        # return '<h1> Successfully Sent your message!</h1>'
        return render_template(
            'index.html', 
            h1_message='Thank you!', 
            card_title='Your message has been sent!', 
            card_text='We will respond to you as soon as it is possible.'
            )
    else:
        return render_template(
            'index.html',
            h1_message='Contact!',
            card_title='Have concerns or want to share your inputs?', 
            card_text='Feel free to post your questions, we will respond to you as soon as it is possible.'            
            )


if __name__ == "__main__":
    app.run(debug=True)
