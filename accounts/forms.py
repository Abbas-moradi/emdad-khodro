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