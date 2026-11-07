import os 
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv


load_dotenv()

SENDER = os.getenv('SENDER_EMAIL')
PASSWORD= os.getenv('SENDER_PASSWORD')
RECEIVER = os.getenv('RECIPIENT_EMAIL')

EMAIL_LIMIT = 90
SUBJECT="ACCOUNT DELETION"
BODY="""
hello 
please help me delete my account.I dont want this to get ugly

kind regards
James
"""

def send_email(subject, body):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = SENDER
    msg['To'] = RECEIVER
    msg.set_content(body)

    
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
          smtp.login(SENDER, PASSWORD)
          smtp.send_message(msg)

    print("Sent Successfully")


for i in range(EMAIL_LIMIT):
     try:
       send_email(SUBJECT,BODY)

     except Exception as e:
         print(f"Error sending Emails:{e}")
         print("Stopping execution")
         break


print("Email sending process ended")


     



