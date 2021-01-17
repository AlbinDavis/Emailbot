import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

listener = sr.Recognizer()
engine = pyttsx3.init()


# talk
def talk(text):
    engine.say(text)
    engine.runAndWait()


# sending email
# speech recognizing
def listen_voice():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say Something")
        audio = r.listen(source)
    try:
        info = r.recognize_google(audio)
        print(info)
        return info.lower()
    except Exception as e:
        print(e)


def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('aloshy812@gmail.com', 'albin812')
    email = EmailMessage()
    email['from'] = 'aloshy812@gmail.com'
    email['to'] = receiver
    email['subject'] = subject
    email.set_content(message)
    server.send_message(email)


# Dictionary of email list of receiver
email_list = {
    'name': 'mail id',
    'hello': 'aloshy812@gmail.com'
}


def get_email_info():
    try:
        talk('Name of Sender')
        name = listen_voice()
        receiver = email_list[name]
        print(receiver)
        talk('subject of email?')
        subject = listen_voice()
        talk('text of mail')
        message = listen_voice()
        send_email(receiver, subject, message)
        talk('Email send')
        cont()
    except Exception as e:
        talk(e)
        talk('not fount')
        cont()


def cont():
    talk('Do you want to do it again yes or no')
    send_more = listen_voice()
    if 'yes' in send_more:
        get_email_info()


get_email_info()
