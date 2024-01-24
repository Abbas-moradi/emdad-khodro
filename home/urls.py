from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('register/', views.Register.as_view(), name='register'),
    path('verifycode/', views.VerifyCode.as_view(), name='verifycode'),
    path('gallery/', views.GalleryImage.as_view(), name='gallery'),
    path('newsletter/', views.UserEmailReg.as_view(), name='newsletter'),
    path('contactus/', views.ContactUs.as_view(), name='contactus'),
]