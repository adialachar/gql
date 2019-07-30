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
    ("Freshman","Freshman"),
    ("Sophomore","Sophomore"),
    ("Junior","Junior"),
    ("Senior","Senior"),
    ("Prefer not to disclose","Prefer not to disclose"),
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

    RACE_CHOICES = (
      (None, ''),
      ('American Indian or Alaskan Native','American Indian or Alaskan Native'),
      ('Asian/Pacific Islander', 'Asian/Pacific Islander'),
      ('Black or African American','Black or African American'),
      ('Hispanic','Hispanic'),
      ('White/Caucasian', 'White/Caucasian'),
      ('Multiple ethnicity/Other (Please Specify)','Multiple ethnicity/Other (Please Specify)'),
      ('Prefer not to diclose', 'Prefer not to disclose'),
    )
    race = models.CharField(max_length=45, choices=RACE_CHOICES, default="")
    race_other = models.CharField(max_length=50, blank=True, default="")
    phone_number = models.CharField(max_length=13, default="")
    SHIRT_SIZE_CHOICES = (
      (None, ''),
      ("XS", "XS"),
      ("S", "S"),
      ("M", "M"),
      ("L", "L"),
      ("XL", "XL"),
      ("XXL", "XXL"),
    )
    shirt_size = models.CharField(max_length=3, choices=SHIRT_SIZE_CHOICES, default="")
    dietary_restrictions = models.CharField(max_length=100, default="", blank=True)

    #Profile Information
    linkedin = models.URLField(max_length=200, blank=True, default="")
    github = models.URLField(max_length=200, blank=True, default="")
    additional_link = models.URLField(max_length=500, blank=True, default="")
    description = models.CharField(max_length=50, default="")
    learn_or_gain = models.TextField(max_length=1000, default="")
    resume = models.URLField(max_length=500, blank=True, default="")

    #Conduct and Policies
    conduct_box = models.BooleanField(default=False)
    share_box = models.BooleanField(default=False)





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
