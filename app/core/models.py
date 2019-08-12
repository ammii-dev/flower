from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
    PermissionsMixin
from django.conf import settings
import uuid
import os

GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female'),
]

def user_image_file_path(instance, filename):
    """Generate file path for new recipe image"""
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return os.path.join('uploads/user/', filename)

def escort_image_file_path(instance, filename):
    """Generate file path for new recipe image"""
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return os.path.join('uploads/escort/', filename)



class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a new User"""
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Creates and saves a new superuser"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports using email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    who = models.CharField(max_length=20)
    image = models.ImageField(null=True, upload_to=user_image_file_path)
    awards = models.CharField(max_length=20)
    points = models.IntegerField()
    # escorts = models.ManyToManyField('Escort', related_name='+')

    objects = UserManager()

    USERNAME_FIELD = 'email'


class Escort(models.Model):
    """Tag to be used for a recipe"""
    name = models.CharField(max_length=255)
    price = models.IntegerField(blank=True, default=0)
    shape = models.CharField(max_length=20, blank=True)
    height = models.IntegerField(blank=True, default=0)
    weight = models.IntegerField(blank=True, default=0)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES ,blank=True)
    age = models.IntegerField()
    isVerified = models.BooleanField(default=False)
    image = models.ImageField(null=True, upload_to=escort_image_file_path) 
    contact_line = models.CharField(max_length=30,blank=True)
    contact_phone = models.CharField(max_length=10 ,blank=True)
    status = models.CharField(max_length=10, default="available")
    viewscount = models.IntegerField(default=0)
    zone = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=100, blank=True)
    excerpt = models.CharField(max_length=100, blank=True)
    desc = models.CharField(max_length=255, blank=True)

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        unique=True,
    )

    # def __str__(self):
    #     return self.name
