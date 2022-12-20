import smtplib
from email.message import EmailMessage

server = smtplib.SMTP('smtp.office365.com', 587)
server.starttls()
server.login('Harsh.x.Gupta@questdiagnostics.com', 'Welcome22')
email = EmailMessage()
email['From'] = 'Harsh.x.Gupta@questdiagnostics.com'
email['To'] = 'Harsh.x.Gupta@questdiagnostics.com'
email['Subject'] = 'Test'
email.set_content("THis is first")
with open('a.xls', 'rb') as fp:
    exlread = fp.read()
email.add_attachment(exlread, maintype='application',
                     subtype='vnd.ms-excel',
                     filename='a.xls')
server.send_message(email)
