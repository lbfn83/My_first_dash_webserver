from django.contrib import admin
from django.urls import path
from . import views
from home.finished_apps import simpleexample
from home.finished_apps import Converter_Data_Graph


urlpatterns = [
    path('', views.home, name='home'),
    path('dash', views.mydash, name='mydash')
]
