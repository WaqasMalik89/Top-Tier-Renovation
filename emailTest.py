import smtplib
from email.mime.text import MIMEText

msg = MIMEText("Test email from Flask app")
msg['Subject'] = "Test Email"
msg['From'] = "your_email@gmail.com"
msg['To'] = "mail.waqas.malik@gmail.com"

try:
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login("mail.waqas.malik@gmail.com", "qbhbyodvbbjoegoj")
        server.sendmail("mail.waqas.malik@gmail.com", "mail.waqas.malik@gmail.com", msg.as_string())
    print("Email sent successfully!")
except Exception as e:
    print(f"Error: {e}")
