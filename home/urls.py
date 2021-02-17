from django.contrib import admin
from django.urls import path
from . import views
from home.finished_apps import simpleexample

urlpatterns = [
    path('', views.home, name='home'),
    path('dash', views.mydash, name='mydash')
]
