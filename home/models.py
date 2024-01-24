from django.db import models
from accounts.models import User


class Advertisement(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    description = models.TextField()
    file = models.ImageField(upload_to='advertis/')
    created = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=False)
    expiration = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Advertisement'
        verbose_name_plural = 'Advertisement'
        ordering = ('created', )
    
    def __str__(self) -> str:
        return f'{self.user.full_name} - {self.description}'


class Job(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='job_pic/')
    phone = models.CharField(max_length=13)
    address = models.TextField()
    created = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Job'
        verbose_name_plural = 'Jobs'
        ordering = ('created', )

    def __str__(self) -> str:
        return f'{self.user.full_name} - {self.title} - {self.created}'
    

class Gallery(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='gallery/')
    created = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'gallery'
        verbose_name_plural = 'gallerise'
        ordering = ('created', )

    def __str__(self) -> str:
        return f'{self.name} - {self.created} - {self.status}'