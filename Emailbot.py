import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def get_info():
    try:
        with sr.Microphone() as source:
            print('Listening.....')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            # print(info)
            return info.lower()
    except:
        pass

def send_email(receiver,subject,message):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('ks.auto82@gmail.com','ks1234567890')
    # server.sendmail('ks.auto82@gmail.com','harsh.harshu@hotmail.com','Hi THis is test automated mail' )
    email=EmailMessage()
    email['From'] = 'ks.auto82@gmail.com'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)

email_list = {
    'Manoj':'Harshautomobile62@gmail.com',
    'Manoj1':'Harshautomobile62@yahoo.com',
    'kunal': 'ks.auto82@gmail.com'
}
def get_email_info():
    talk('to whom you want to send email')
    name = get_info()
    receiver = email_list[name]
    print(receiver)
    talk('What si the subject of your email?')
    subject = get_info()
    talk('Tell me the text in your email')
    message = get_info()
    send_email(receiver,subject,message)
    talk('Hey lazy ass. Your email is sent')
    talk('do you want to set sent more email')
    send_more = get_info()
    if 'yes' in send_more:
        get_email_info()
