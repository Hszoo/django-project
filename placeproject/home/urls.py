from django.contrib import admin
from django.urls import path
from home import views, include

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/', include('accounts.urls', namespace='accounts')),
]
