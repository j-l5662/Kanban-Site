from django.db import models
from django.urls import reverse
# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=20,blank=False,null=False)
    email = models.CharField(max_length=20,blank=False,null=False)
    password = models.CharField(max_length= 100,blank=False,null=False)
