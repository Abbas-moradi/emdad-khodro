from emdad import settings
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse
from celery import shared_task

"""
This Celery task is designed to run asynchronously and is typically
triggered when an order is placed in the online shop. It sends an 
email notification to the user to inform them about their order, 
including the order ID and a custom message.
"""


# @shared_task()
def email_sender(code, email):
    subject = 'کد تایید ثبت نام'
    message = f':کد تایید ثبت نام شما {code}'
    email_from = settings.EMAIL_HOST_USER
    try:
        send_mail(subject,message,email_from,[email],fail_silently=False,)
    except BadHeaderError:
        return HttpResponse("Invalid header found.")