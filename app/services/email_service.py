import smtplib
from email.mime.text import MIMEText

def send_email(to_email, subject, body):
    sender_email = "your_email@gmail.com"
    password = "your_app_password"

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = to_email

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, password)
    server.send_message(msg)
    server.quit()