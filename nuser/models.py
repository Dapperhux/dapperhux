import email
from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime


class User(AbstractUser):
    is_vip = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=11)
    email = models.EmailField(max_length=150)
    password = models.CharField(max_length=100)
    is_adult = models.BooleanField(default=False)


class post(models.Model):
    body = models.TextField(max_length=10000000000000000000000000)
    date = models.DateTimeField(auto_now_add=True, blank=True)


class dailypost(models.Model):
    body = models.TextField(max_length=10000000000000000000000000)
    date = models.DateTimeField(auto_now_add=True, blank=True)



class viptest(models.Model):
    body = models.TextField(max_length=10000000000000000000000000)
    date = models.DateTimeField(auto_now_add=True, blank=True)