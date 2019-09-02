from django.urls import path, re_path, include

from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('apply', views.MyUserView)

urlpatterns = [

    path('', include(router.urls)),
    path('api/profile', views.profile, name='profile'),
    path('api/login', views.login, name='login'),
    path('api/email', views.email, name='email'),
    path('api/validateToken', views.validateToken, name='validateToken')

]
