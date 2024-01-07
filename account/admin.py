from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import Group
from .models import User, OtpCodeRegister, UserComment, ContactUs


@admin.register(OtpCodeRegister)
class OtpCodeAdmin(admin.ModelAdmin):
    list_display = ('phone', 'code', 'created')


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('user_id', 'email', 'phone', 'full_name', 'is_admin')
    list_filter = ('is_admin',)

    fieldsets = (
        ('Main',{'fields':('email', 'phone', 'full_name', 'password')}),
        ('permission', {'fields':('is_active', 'is_admin', 'last_login')})
    )

    add_fieldsets = (
        (None, {'fields': ('phone', 'email', 'full_name', 'password1', 'password2')}),
    )

    search_fields = ('email', 'full_name')
    ordering = ('full_name', )
    filter_horizontal = ()  # because I don't have a permission yet, I put this as an empty tuple


admin.site.unregister(Group)
admin.site.register(User, UserAdmin)