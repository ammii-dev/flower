from django.db import models
# Create your models here.
from django.contrib.auth.models import User



class EscortPost(models.Model):
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    awards = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    tall = models.IntegerField()
    weight = models.IntegerField()
    lowest_price = models.IntegerField()
    package = models.CharField(max_length=100)
    body_ratio = models.CharField(max_length=100)
    zone = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    contactLine = models.CharField(max_length=100)
    contactPhone = models.CharField(max_length=100)
    views_count = models.IntegerField()
    isVerified = models.BooleanField(default=False)
    isTopstar = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    # image = models.ImageField(upload_to='photos', max_length=254)
    class Meta:
        ordering = ('name',)
