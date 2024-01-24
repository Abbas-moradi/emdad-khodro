from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import Group
from .models import User, OtpCodeRegister, UserComment, ContactUs, Newsletters


@admin.register(OtpCodeRegister)
class OtpCodeRegisterAdmin(admin.ModelAdmin):
    list_display = ('email', 'code', 'created')


@admin.register(Newsletters)
class NewslettersAdmin(admin.ModelAdmin):
    list_display = ('email', 'created', 'status')


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('user_id', 'phone', 'full_name', 'job_type','is_admin')
    list_filter = ('is_admin',)

    fieldsets = (
        ('Main',{'fields':('email', 'phone', 'full_name', 'job_type', 'city', 'password', 'profile_picture', 'description')}),
        ('permission', {'fields':('is_active', 'is_admin', 'last_login')})
    )

    add_fieldsets = (
        (None, {'fields': ('phone', 'email', 'full_name', 'job_type', 'city', 'description', 'password1', 'password2', 'profile_picture')}),
    )

    search_fields = ('email', 'full_name')
    ordering = ('full_name', )
    filter_horizontal = ()  # because I don't have a permission yet, I put this as an empty tuple


admin.site.unregister(Group)
admin.site.register(User, UserAdmin)