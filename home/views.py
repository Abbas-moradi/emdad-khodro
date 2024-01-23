from django.shortcuts import render, redirect
from django.views import View
from accounts.models import User, OtpCodeRegister
from home.models import Job, Advertisement
import random
from utils import send_mail, check_time_elapsed
from django.utils import timezone
from datetime import datetime


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
    errore_temp = 'inc/errore.html'
    accept_temp = 'inc/accept.html'

    def get(self, request):
        return render(request, self.reg_temp)

    def post(self, request):
        user_enter_mail = (request.POST['email'])
        user = User.objects.filter(email=user_enter_mail).exists()
        if user:
            return render(request, self.errore_temp, {'this_errore': 'با این ایمیل قبلا ثبت نام انجام شده است'})
        
        if request.POST['password1'] != request.POST['password2']:
            return render(request, self.errore_temp, {'this_errore': 'رمز اول با تکرار رمز برابر نیست'})
        
        otp_code = random.randint(1000, 9999)
        subject = 'کد تایید ثبت نام'
        body = f'کد تایید شما \n code:{otp_code}'
        user_code_exists = OtpCodeRegister.objects.filter(email=user_enter_mail).exists()
        if user_code_exists:
            user_code_created_time = OtpCodeRegister.objects.filter(email=user_enter_mail).values_list('created', flat=True).first()
            current_time = timezone.now()
            time_difference = current_time - user_code_created_time

            if time_difference.total_seconds() > 120:
                user_code_exists = OtpCodeRegister.objects.filter(email=user_enter_mail).delete()
                OtpCodeRegister.objects.create(email=user_enter_mail, code=otp_code)

            else:
                otp_code = OtpCodeRegister.objects.filter(email=user_enter_mail).values_list('code', flat=True).first()
            
        else:
            OtpCodeRegister.objects.create(email=user_enter_mail, code=otp_code)
        
        if send_mail(subject, body, user_enter_mail):
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
            return redirect('home:verifycode')
        return render(request, self.errore_temp, {'this_errore': 'متاسفانه در ارسال ایمیل مشکلی رخ داده است'})


class VerifyCode(View):
    errore_temp = 'inc/errore.html'
    otp_code_temp = 'inc/otpcode.html'
    accept_register_temp = 'inc/accept.html'

    def get(self, request):
        return render(request, self.otp_code_temp)

    def post(self, request):
        return render(request, self.errore_temp, {'this_errore': 'این یک پیغام خطای تستی است'})