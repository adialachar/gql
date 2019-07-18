from django.contrib import admin
from .models import MyUser, Profile
#from .models import UserModel
# Register your models here.
admin.site.register(MyUser)
admin.site.register(Profile)
#admin.site.register(UserModel)
