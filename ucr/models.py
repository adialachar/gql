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
    school = models.CharField(max_length=30)

    LEVEL_OF_STUDY_CHOICES = (

    (None, ''),
    ("Freshman","Freshman")
    ("Sophomore","Sophomore")
    ("Junior","Junior")
    ("Senior","Senior")
    ("Prefer not to disclose","Prefer not to disclose")
    )

    level_of_study = models.CharField(max_length=30,choices=LEVEL_OF_STUDY_CHOICES)


    GRADUATION_YEAR_CHOICES = (

    (None, ''),
    ("2019", "2019"),
    ("2020","2020"),
    ("2021","2021"),
    ("2022","2022"),
    ("2023","2023"),
    ("2024 or later", "2024 or later"),
    ("Prefer not to disclose","Prefer not to disclose")
    )


    graduation_year=models.CharField(max_length=30, choices=GRADUATION_YEAR_CHOICES, default="")
    major = models.CharField(max_length=30)

    GENDER_CHOICES = (
    (None,''),
    ("Female","Female"),
    ("Male","Male"),
    ("Other (Please Specify)","Other (Please Specify)"),

    )

    gender = models.CharField(max_length=30, choices=GENDER_CHOICES)
    gender_other = models.CharField(max_length=30, blank=True)

    date_of_birth = models.CharField(max_length=10)


    RACE_CHOICES =(

    (None, ''),






    )




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
