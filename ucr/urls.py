from django.urls import path, re_path

from . import views



urlpatterns = [

    path('api/apply', views.apply, name='apply'),
    path('api/profile', views.profile, name='profile'),
    path('api/login', views.login, name='login'),
    path('api/emailconf', views.email, name='email'),
    path('api/passwordReset', views.passwordReset, name='passwordReset'),


]
