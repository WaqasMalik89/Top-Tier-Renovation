from flask import Flask, render_template, request, redirect
import smtplib
from email.mime.text import MIMEText
import os

app = Flask(__name__)


@app.route('/test')
def test():
    return "Flask is working!"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    # Email content
    subject = f"New message from {name}"
    body = f"From: {name} <{email}>\n\n{message}"
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = email
    msg['To'] = 'mail.waqas.malik@gmail.com'

    # Send email via Gmail SMTP
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login('mail.waqas.malik@gmail.com', 'qbhbyodvbbjoegoj')
            server.sendmail('mail.waqas.malik@gmail.com', 'mail.waqas.malik@gmail.com', msg.as_string())
        return redirect('/')
    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    #app.run(debug=True)
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

