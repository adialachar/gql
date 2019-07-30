from django.urls import path, re_path

from . import views



urlpatterns = [

    path('api/apply', views.apply, name='apply'),
    path('api/profile', views.profile, name='profile'),
    path('api/login', views.login, name='login')


]
