from django.contrib import admin
from django.urls import path
from posts import views

urlpatterns = [
    path('', views.home, name='posthome'),
    # C
    path('post_list/',views.post_list, name='post_list'),
    path('create/', views.post_create, name='post_create'),
    path('updadte/<int:id>/', views.post_update, name='post_update'),
    path('delete/<int:id>/', views.post_delete, name='post_delete'),
    path('post_detail/<int:id>/', views.post_detail, name='post_detail'),
    # path converter <int:id> , 특정 객체에 따라 url 상이
    # 넘겨받은 id에 해당하는 post의 디테일 페이지 표시  
]
