import os
import smtplib
from email.message import EmailMessage

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')
EMAIL_SUBJECT = os.environ.get('EMAIL_SUBJECT')
RECEIPIENT_EMAILS = os.environ.get('RECEIPIENT_EMAILS')
FILE_PATH = os.environ.get('RESULTS_DIR')
FILE_NAME = os.environ.get('FILE_NAME')

try:
    with open(os.path.join(FILE_PATH, FILE_NAME), "r") as file:
        content = file.read()
except FileNotFoundError:
    raise FileNotFoundError(f"The file '{FILE_PATH + FILE_NAME}' does not exist.")

if RECEIPIENT_EMAILS:
    contacts = RECEIPIENT_EMAILS
else:
    contacts = ['admaskinfu@gmail.com']

msg = EmailMessage()
msg['Subject'] = EMAIL_SUBJECT
msg['From'] = EMAIL_ADDRESS
msg['To'] = contacts

msg.add_alternative(content, subtype='html')


with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)