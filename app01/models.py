from django.db import models

from django.contrib.auth.models import User, AbstractBaseUser

# Create your models here.

# class User(models.Model):
#     username = models.CharField(max_length=16)
#     password = models.CharField(max_length=32)
#
# class UserDetail(models.Model):
#     phone = models.CharField(max_length=11)
#
#     user = models.OneToOneField(to='User')

class UserInfo(AbstractBaseUser):
    identifier = models.CharField(max_length=40, unique=True)
    USERNAME_FIELD = 'identifier'

    phone = models.CharField(max_length=11)
    addr = models.CharField(max_length=128)

