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


class ProfileManager(models.Manager):

    def create_profile(self,user,profile_data):

        pf = Profile(user=user, first_name = profile_data['first_name'], last_name = profile_data['last_name'], school = profile_data['school'], level_of_study = profile_data['level_of_study'], graduation_year=profile_data['graduation_year'], major=profile_data['major'], gender=profile_data['gender'], gender_other=profile_data['gender_other'], race=profile_data['race'], race_other=profile_data['race_other'], phone_number=profile_data['phone_number'], date_of_birth=profile_data['date_of_birth'],shirt_size=profile_data['shirt_size'], dietary_restrictions=profile_data['dietary_restrictions'], linkedin=profile_data['linkedin'], github=profile_data['github'], resume=profile_data['resume'], conduct_box=profile_data['conduct_box'], share_box=profile_data['share_box'])
        pf.save()

# user, first_name, last_name, school, level_of_study, graduation_year, major, \
#     gender, gender_other, race, race_other, phone_number, date_of_birth, shirt_size, dietary_restrictions, linkedin, \
#     github, resume, conduct_box, share_box

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

    objects = ProfileManager()
    # LEVEL_OF_STUDY_CHOICES = (

    # (None, ''),
    # ("Freshman","Freshman"),
    # ("Sophomore","Sophomore"),
    # ("Junior","Junior"),
    # ("Senior","Senior"),
    # ("Prefer not to disclose","Prefer not to disclose"),
    # )

    # level_of_study = models.CharField(max_length=30,choices=LEVEL_OF_STUDY_CHOICES)

    level_of_study = models.CharField(max_length=30)


    # GRADUATION_YEAR_CHOICES = (

    # (None, ''),
    # ("2019", "2019"),
    # ("2020","2020"),
    # ("2021","2021"),
    # ("2022","2022"),
    # ("2023","2023"),
    # ("2024 or later", "2024 or later"),
    # ("Prefer not to disclose","Prefer not to disclose")
    # )


    graduation_year=models.CharField(max_length=30, default="")
    major = models.CharField(max_length=30)

    # GENDER_CHOICES = (
    # (None,''),
    # ("Female","Female"),
    # ("Male","Male"),
    # ("Other (Please Specify)","Other (Please Specify)"),

    # )

    gender = models.CharField(max_length=30)
    gender_other = models.CharField(max_length=30, blank=True)

    date_of_birth = models.CharField(max_length=10)

    # RACE_CHOICES = (
    #   (None, ''),
    #   ('American Indian or Alaskan Native','American Indian or Alaskan Native'),
    #   ('Asian/Pacific Islander', 'Asian/Pacific Islander'),
    #   ('Black or African American','Black or African American'),
    #   ('Hispanic','Hispanic'),
    #   ('White/Caucasian', 'White/Caucasian'),
    #   ('Multiple ethnicity/Other (Please Specify)','Multiple ethnicity/Other (Please Specify)'),
    #   ('Prefer not to diclose', 'Prefer not to disclose'),
    # )
    race = models.CharField(max_length=45, default="")
    race_other = models.CharField(max_length=50, blank=True, default="")
    phone_number = models.CharField(max_length=13, default="")
    # SHIRT_SIZE_CHOICES = (
    #   (None, ''),
    #   ("XS", "XS"),
    #   ("S", "S"),
    #   ("M", "M"),
    #   ("L", "L"),
    #   ("XL", "XL"),
    #   ("XXL", "XXL"),
    # )
    shirt_size = models.CharField(max_length=3, default="")
    dietary_restrictions = models.CharField(max_length=100, default="", blank=True)

    #Profile Information
    linkedin = models.URLField(max_length=200, blank=True, default="")
    github = models.URLField(max_length=200, blank=True, default="")
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
