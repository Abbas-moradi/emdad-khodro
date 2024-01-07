from django.shortcuts import render, redirect
from django.views import View
from .forms import UserRegisterationForm
from .forms import UserRegisterationForm, VerifyCodeForm, UserCommentForm
from utils import send_otp_code
from django.contrib import messages
from django.shortcuts import get_object_or_404
from .tasks import email_sender
import random
from .models import OtpCodeRegister, User


class UserRegisterView(View):
    form_class = UserRegisterationForm
    template_name = 'register.html'

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            code_instance = OtpCodeRegister.objects.filter(phone=form.cleaned_data['phone']).exists()
            if code_instance:
                code_instance = OtpCodeRegister.objects.get(phone=form.cleaned_data['phone'])
                random_code = code_instance.code
            else:
                random_code = random.randint(10000, 99999)
                OtpCodeRegister.objects.create(phone=form.cleaned_data['phone'], code=random_code)
            
            user_phone = User.objects.filter(phone=form.cleaned_data['phone']).exists()
            user_email = User.objects.filter(email=form.cleaned_data['email']).exists()

            if user_phone or user_email:
                return redirect('home:errore', errore='phone_or_email')

            send_otp_code(form.cleaned_data['phone'], random_code)
            email_sender(random_code, form.cleaned_data['email'])
            
            request.session['user_register_info'] = {
                'phone_number': form.cleaned_data['phone'],
                'user_email': form.cleaned_data['email'],
            }
            return redirect('accounts:verify_code')
        return render(request,'register.html', {'form':form})


class UserRegisterVerifyCode(View):
    form_class = VerifyCodeForm
    template_name = 'verify_code.html'

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        user_session = request.session['user_register_info']
        code_instance = OtpCodeRegister.objects.get(phone=user_session['phone_number'])
        form = self.form_class(request.POST)
        if form.is_valid():
            clean_data = form.cleaned_data
            if clean_data['code'] == code_instance.code:
                User.objects.create(phone=user_session['phone_number'], email=user_session['user_email'],
                                     full_name='Anonymous', password=user_session['phone_number'])
                code_instance.delete()
                return redirect('home:home')
            else:
                bug = 'otp_code'
                return redirect('home:errore', errore=bug)
        return redirect('home:home')


class UserComment(View):
    form_class = UserCommentForm

    def get(self, request):
        pass
