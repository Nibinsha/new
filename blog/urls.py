from django.urls import path

from . import views

urlpatterns=[
    path('', views.login),
    path('registration', views.registration),
    path('loggedin', views.loggedin),
    path('index', views.index),
    path('leaveSave', views.leaveSave),
    path('fetchleaveData', views.fetchleaveData),
    path('fetchParticularLveData', views.fetchParticularLveData),
    path('SavefetchParticularLveData', views.SavefetchParticularLveData),
    ]