from django.contrib import admin
from django.urls import path
from menus import views

urlpatterns = [
    path('', views.home, name='home'),
]
