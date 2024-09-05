import smtplib
from email.message import EmailMessage
import pandas as pd

# Your email and password
your_email = 'suji.cloud.mfedu@gmail.com'
your_password = 'prkqondmezioeqgw'

# Load contacts from CSV file
contacts_df = pd.read_csv("A:\Python\SMTP Project\hr_contacts.csv")

subject = "__Highly Urgent__"
base_message = """
Respected {name},

I hope this message finds you well.

This is Test email,dont panic you are good...!
"""

# Set up the SMTP server
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(your_email, your_password)

# Send emails
for index, row in contacts_df.iterrows():
    name = row['Name']
    email = row['Email']
    
    try:
        msg = EmailMessage()
        msg['From'] = your_email
        msg['To'] = email
        msg['Subject'] = subject
        msg.set_content(base_message.format(name=name))
        
        server.send_message(msg)
        print(f"Email sent to {name} at {email}")
    except Exception as e:
        print(f"Failed to send email to {email}: {e}")

server.quit()
