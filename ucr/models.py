from django.db import models
from django.contrib.auth.models import AbstractBaseUser


# Create your models here
class MyUser(AbstractBaseUser):
    email = models.EmailField(max_length=30)


class Profile(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

