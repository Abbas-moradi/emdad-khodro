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
