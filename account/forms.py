from django import forms
from .models import User
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='confirm password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'phone', 'full_name', )

        def clean_password2(self):
            clean_data = self.cleaned_data
            if clean_data['password1'] and clean_data['password2'] and clean_data['password1'] != clean_data['password2']:
                raise ValidationError('password dont match...')
            return clean_data['password2']
        
        def save(self, commit=True):
            user = super().save(commit=False)
            user.set_password(self.clean_data['password1'])
            if commit:
                user.save()
            return user
        
class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(help_text = 'you cant change password using <a href=\"../password/\"> this form</a>.')

    class Meta:
        model = User
        fields = ('email', 'phone', 'full_name', 'password', 'last_login')


class UserRegisterationForm(forms.Form):
    phone = forms.CharField(max_length=12)
    email = forms.EmailField()

    # def clean_phone(self):
    #     phone = self.cleaned_data['phone']
    #     user = User.objects.filter(phone=self.cleaned_data['phone']).exists()
    #     if user:
    #         raise ValidationError('این شماره تلفن از قبل وجود دارد')
    #     return phone
    
    # def clean_email(self):
    #     email = self.cleaned_data['email']
    #     user = User.objects.filter(email=self.cleaned_data['email']).exists()
    #     if user:
    #         messages.error('کد وارد شده اشتباه است', 'danger')
    #         raise ValidationError('این ایمیل از قبل وجود دارد')
    #     return email


class VerifyCodeForm(forms.Form):
    code = forms.IntegerField()


class ContactUsForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    subject = forms.CharField()
    description = forms.Textarea()

class UserCommentForm(forms.Form):
    user_name = forms.CharField()
    email = forms.EmailField()
    comment = forms.Textarea()
    subject = forms.CharField()
    
    

    