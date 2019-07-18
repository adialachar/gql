from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Create your models here
class MyUserManager(BaseUserManager):

    def create_user(self, email, password=None):

        user = self.model(email=self.normalize_email(email))

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):

        user = self.create_user(email, password = password)

        user.is_admin = True
        user.is_active = True

        user.save(using=self._db)
        return user






class MyUser(AbstractBaseUser):

    email = models.EmailField(
            verbose_name='email address',
        max_length=255,
        unique=True,

    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()


    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    @property
    def is_staff(self):

        return self.is_admin



class Profile(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)





'''
class UserModel(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
'''

'''
class MyUser(AbstractBaseUser):
    email = models.EmailField(max_length=30)


class Profile(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
'''
