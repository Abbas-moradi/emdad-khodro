from django.contrib import admin
from home.models import Advertisement

@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['user', 'description', 'file', 
                    'created', 'status',
                    'expiration']
