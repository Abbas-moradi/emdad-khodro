import os
import yagmail
from emkho import settings


dotenv_path = ".env"
try:
    with open(dotenv_path, 'r') as file:
        for line in file:
            key, value = line.strip().split('=')
            os.environ[key] = value
except FileNotFoundError:
    print(f"File {dotenv_path} not found.")


def send_mail(subject, body, to)-> bool:
    email_from = settings.EMAIL_HOST_USER
    print(email_from)
    message=body
    subject=subject
    try:
        send_mail(subject,message,email_from,[to],fail_silently=False,)
        return True
    except:
        return False