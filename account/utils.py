from kavenegar import *
from emdad import settings
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse


def send_otp_code(phone, code):
    try:
        api = KavenegarAPI('2F77537067544365733452714E42516D69344B6176456854354732787363716B4B7848316F5165525155553D')
        params = { 'sender' : '1000010000808',
                   'receptor': phone,
                   'message' :f' :کد تایید شما {code}' }
        print(params)
        response = api.sms_send( params)
    except APIException as e:
        print(e)
    except HTTPException as h:
        print(h)

def email_sender(subject, email, text):
    message = text
    email_from = settings.EMAIL_HOST_USER
    try:
        send_mail(subject,message,email_from,[email],fail_silently=False,)
    except BadHeaderError:
        return HttpResponse("Invalid header found.")