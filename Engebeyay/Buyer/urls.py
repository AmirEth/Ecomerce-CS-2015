from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signin', views.signin, name='signin'),
    path('signup', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    path('autenication_main', views.autenication_main, name='autenication_main'),

]
