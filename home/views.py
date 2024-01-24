from django.shortcuts import render, redirect
from django.views import View
from accounts.models import User, OtpCodeRegister, Newsletters
from home.models import Job, Advertisement, Gallery
import random
from utils import send_email
from django.utils import timezone


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
        
        if send_email(subject, body, user_enter_mail):
            print(request.POST,'<---------------------->')
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
        code = request.POST['code']
        user_email = request.session['user_register_info']['user_email']
        database_code = OtpCodeRegister.objects.filter(email=user_email).values_list('code', flat=True).first()
        if int(code)==int(database_code):
            User.objects.create(
                email=user_email,
                phone=request.session['user_register_info']['phone_number'],
                full_name=request.session['user_register_info']['full_name'],
                profile_picture=request.session['user_register_info']['pic'],
                description=request.session['user_register_info']['description'],
                password=request.session['user_register_info']['password'],
                city=request.session['user_register_info']['city'],
                job_type=request.session['user_register_info']['job']
            )
            return render(request, self.accept_register_temp)
        else:
            return render(request, self.errore_temp, {'this_errore': 'کد وارد شده با کد ارسالی برای شما مغایرت دارد'})


class GalleryImage(View):
    gallery_temp = 'inc/gallery.html'

    def get(self, request):
        images = Gallery.objects.filter(status=True)
        advertis = Advertisement.objects.filter(status=True, expiration=False)
        random_advertis = random.choice(advertis)
        return render(request, self.gallery_temp, {'images': images,
                                                   'advertis': random_advertis
                                                   })

    def post(self, request):
        pass


class UserEmailReg(View):
    email_accept_temp = 'inc/email-accept.html'
    errore_temp = 'inc/errore.html'

    def get(self, request):
        pass

    def post(self, request):
        user_mail = request.POST['email']
        if Newsletters.objects.filter(email=user_mail).exists():
            return render(request, self.errore_temp, {'this_errore':'این ایمیل قبلا ثبت شده است، از توجه شما سپاسگذاریم'})
        
        Newsletters.objects.create(email=user_mail)
        return render(request, self.email_accept_temp)
