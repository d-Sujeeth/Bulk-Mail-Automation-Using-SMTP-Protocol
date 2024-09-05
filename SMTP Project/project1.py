import smtplib
from email.message import EmailMessage

your_email = 'suji.cloud.mfedu@gmail.com'
your_password = 'prkqondmezioeqgw'

hr_contacts = {
    "pradeep":"1606pradeepragul@gmail.com"
}

subject = "jenkins Server URL"                                                          
base_message = """
Hi {name}
http://35.172.150.190/index.html
"""

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(your_email, your_password)

for name, email in hr_contacts.items():
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
