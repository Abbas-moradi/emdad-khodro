from django.db import models
from account.models import User

class Job(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=20, choices=[
        ('RE', 'Repairman'), # تعمیرکار
        ('CT', 'Car transport'), # حمل خودرو
        ('ES', 'Electrical specialist'), # برق خودرو
        ('OC', 'Oil Change'), # تعویض روغنی
        ('P', 'Puncture'), # آپاراتی
        ('CS', 'Car smoothing'), # صافکاری
        ('CP', 'Car painter'), # نقاش اتوموبیل
        ('U', 'Upholstery'), # تو دوزی خودرو
    ])
    descriptoin = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='gallery/')
    created = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True)
