from django.contrib import admin
from home.models import Advertisement, Job, Gallery, Article

@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['user', 'description', 'file', 
                    'created', 'status',
                    'expiration']
    
@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'image', 
                    'created', 'status',
                    'phone']
    
@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['name', 'image', 'created', 'status']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['subject', 'created', 'status']
