from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=122)
    tg_username = models.CharField(max_length=150)
    avatar = models.ImageField(upload_to='avatars',default='avatars/default.png')
    
    def __str__(self):
        return self.username