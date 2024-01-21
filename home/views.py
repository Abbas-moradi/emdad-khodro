from django.shortcuts import render, redirect
from django.views import View
from accounts.models import User, OtpCodeRegister
from home.models import Job, Advertisement
import random
from utils import send_mail


class Home(View):
    template_name = 'index.html'

    def get(self, request):
        all_user = User.objects.all()
        all_jobs = Job.objects.filter(status=True)
        advertis = Advertisement.objects.filter(status=True, expiration=False)
        random_advertis = random.choice(advertis)

        return render(request, self.template_name, {'users': all_user,
                                                    'jobs': all_jobs,
                                                    'advertis': random_advertis})
    

class Register(View):
    reg_temp = 'inc/register.html'
    otp_code_temp = 'inc/otpcode.html'
    errore_temp = 'inc/errore.html'

    def get(self, request):
        return render(request, self.reg_temp)

    def post(self, request):
        user_enter_mail = (request.POST['email'])
        user = User.objects.filter(email=user_enter_mail).exists()
        if user:
            return render(request, self.errore_temp, {'this_errore': 'با این ایمیل قبلا ثبت نام انجام شده است'})
        
        otp_code = random.randint(0, 9999)
        subject = 'کد تایید ثبت نام'
        body = f'کد تایید شما \n code:{otp_code}'
        if request.POST['password1'] != request.POST['password2']:
            return render(request, self.errore_temp, {'this_errore': 'رمز اول با تکرار رمز برابر نیست'})
        
        send_mail(subject, body, user_enter_mail)
        request.session['user_register_info'] = {
                'phone_number': request.POST['phone'],
                'user_email': request.POST['email'],
                'full_name': request.POST['name'],
                'pic': request.POST['image'],
                'description': request.POST['description'],
                'password': request.POST['password2'],
                'city': request.POST['city'],
                'job': request.POST['job'],
                }
        return render(request, self.otp_code_temp)

