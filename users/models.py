from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Users(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    who = models.CharField(max_length=50, blank=True, default='')
