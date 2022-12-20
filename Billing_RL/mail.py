import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pyexpat.errors import messages

mail_content = '''Hello,
This is a test mail.
In this mail we are sending some attachments.
The mail is sent using Python SMTP library.
Thank You
'''

# server = smtplib.SMTP('smtp.office365.com', 587)
# # server.starttls()
# # server.login('Harsh.x.Gupta@questdiagnostics.com', 'Welcome22')
# # email = EmailMessage()
# # email['From'] = 'Harsh.x.Gupta@questdiagnostics.com'
# # email['To'] = 'Harsh.x.Gupta@questdiagnostics.com'
# # email['Subject'] = 'Test'
# # email.set_content("THis is first")
# # email.add_attachment(open('b.html','rb'))
# # server.send_message(email)

# Setup the MIME
message = MIMEMultipart()
# message['From'] = 'Harsh.x.Gupta@questdiagnostics.com'
message['To'] = 'Harsh.x.Gupta@questdiagnostics.com'
message['Subject'] = 'A test mail sent by Python. It has an attachment.'
# The subject line
# The body and the attachments for the mail
message.attach(MIMEText(mail_content, 'plain', 'us-ascii'))
attach_file_name = 'a.xls'
# attach_file = open(attach_file_name, 'rb')  # Open the file as binary mode
payload = MIMEBase('application', 'vnd.ms-excel')
with open('a.xls', 'rb') as attach_file:
    payload.set_payload(attach_file.read())
# attach_file.close()
encoders.encode_base64(payload)  # encode the attachment
# add payload header with filename
payload.add_header('Content-Decomposition', 'attachment', filename=attach_file_name)
message.attach(payload)

server = smtplib.SMTP('smtp.office365.com', 587)
server.starttls()
server.login('Harsh.x.Gupta@questdiagnostics.com', 'Welcome22')
text = message.as_string()
server.sendmail('QBSEDIsupport@questdiagnostics.com', 'Harsh.x.Gupta@questdiagnostics.com', text)





# sender = "QBSEDISupport@questdiagnostics.com"
# receiver = "Harsh.x.Gupta@questdiagnostics.com"
# message = "This is my First test mail"
#
# server = smtplib.SMTP(host='Edgemailrelay.qdx.com', port=25)
#
# server.sendmail(sender, receiver, message)
