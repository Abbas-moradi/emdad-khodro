from django.shortcuts import render, redirect
from django.views import View
from accounts.models import User, OtpCodeRegister
from home.models import Job, Advertisement
import random


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
        print(request)

