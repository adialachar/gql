from django.urls import path, re_path

from . import views



urlpatterns = [

    path('', views.index, name='index'),
    path('dummyapply/', views.dummyapply, name='dummyapply'),
    path('dummyAllData/', views.dummyallData, name='dummyAllData'),
    path('dummyParametrizedData/', views.dummyParametrizedData, name='dummyParametrizedData')


]
