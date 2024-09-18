import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email():
    smtp_server = 'smtp-mail.outlook.com'
    smtp_port = 587
    # sender_email = 'ushasrimogadali123@gmail.com'
    # password = 'aqhrubyzsvfpobjzz'
    sender_email = 'ushasrimogadali123@gmail.com'
    password = 'aqhrubyzsvfpobjzz'
    recipient_email = 'likhithkanigolla@gmail.com'
    subject = 'Test Email'
    body = 'Hello, this is a test email sent from a Python script using Outlook.'

    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = recipient_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.set_debuglevel(1)
        server.login(sender_email, password)
        server.sendmail(sender_email, recipient_email, message.as_string())
        print('Email sent successfully!')
    except Exception as e:
        print(f'Error: {e}')
    finally:
        server.quit()

if __name__ == '__main__':
    send_email()
