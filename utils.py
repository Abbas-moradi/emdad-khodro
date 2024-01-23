import os
from emkho import settings
from django.core.mail import send_mail, BadHeaderError
from emkho import settings
from smtplib import SMTPException


dotenv_path = ".env"
try:
    with open(dotenv_path, 'r') as file:
        for line in file:
            key, value = line.strip().split('=')
            os.environ[key] = value
except FileNotFoundError:
    print(f"File {dotenv_path} not found.")


def send_email(subject, body, to) -> bool:
    email_from = settings.EMAIL_HOST_USER
    message = body
    subject = subject
    try:
        send_mail(subject, message, email_from, [to], fail_silently=False)
        return True
    except BadHeaderError as bad_header_error:
        print(f"خطا در ساختار هدر: {bad_header_error}")
        return False
    except SMTPException as smtp_exception:
        print(f"خطا در ارسال ایمیل: {smtp_exception}")
        return False
