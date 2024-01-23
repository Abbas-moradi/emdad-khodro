from django.db import models
from django.contrib.auth.models import AbstractBaseUser
import uuid
from .managers import UserManager


class User(AbstractBaseUser):
    user_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    email = models.EmailField(max_length=150, unique=True)
    phone = models.CharField(max_length=12, unique=True)
    full_name = models.CharField(max_length=150)

    class Jobs(models.TextChoices):
        MECHANICAL_REPAIR = "تعمیرکار",
        PUNCTURE_CATCHER = "آپاراتی",
        CAR_GLASS = "شیشه اتوموبیل",
        ELECTRICAL_REPAIR = "برق خودرو",
        BODY_WORK = "صافکار",
        PAINTING = "نقاش",
        TRANSMISSION_REPAIR = "متخصص گیربکس",
        OIL_CHANGE = "تعویض روغن",
        TOWING = "یدک کش",
        OTHER = "سایر",
    
        def call(self):
            return f'{self.MECHANICAL_REPAIR}'

    job_type = models.CharField(
        max_length=20,
        choices=Jobs.choices,
        default=Jobs.OTHER,
    )

    class City(models.TextChoices):
        ABYEK = "آبیک",

    city = models.CharField(
        max_length=20,
        choices=City.choices,
        default=City.ABYEK
    )
    description = models.TextField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/')
    is_active = models.BooleanField(default=True)
    is_delete = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['email', 'full_name']

    def __str__(self) -> str:
        return self.email
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin 


class OtpCodeRegister(models.Model):
    email = models.EmailField()
    code = models.PositiveSmallIntegerField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.email} - {self.code} - {self.created}'


class UserComment(models.Model):
    user_name = models.CharField(max_length=250)
    email = models.EmailField()
    comment = models.TextField()
    subject = models.CharField(max_length=250)
    status = models.BooleanField(default=False)
    created = models.DateField(auto_now_add=True)
    is_delete = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.user_name}-{self.subject}-{self.status}-{self.created}'
    

class ContactUs(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=250)
    subject = models.CharField(max_length=250)
    description = models.TextField()
    created = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f'{self.name} - {self.subject} - {self.email}'