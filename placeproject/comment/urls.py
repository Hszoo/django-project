from django.contrib import admin
from django.urls import path
from comment import views

urlpatterns = [
    path('', views.commenthome, name='commenthome'),
    
]
