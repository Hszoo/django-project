from django.contrib import admin
from django.urls import path
from posts import views

urlpatterns = [
    path('', views.home, name='posthome'),
    path('post_list/',views.post_list, name='post_list'),
    
    # 게시글 경로 
    path('create/', views.post_create, name='post_create'),
    path('updadte/<int:id>/', views.post_update, name='post_update'),
    path('delete/<int:id>/', views.post_delete, name='post_delete'),
    path('post_detail/<int:id>/', views.post_detail, name='post_detail'),
    
    # comment 경로 
    path('create_comment/<int:id>', views.create_comment, name='create_comment'),
    path('update_comment/<int:post_id>/<int:com_id>', views.update_comment, name='update_comment'),
    # path converter <int:id> , 특정 객체에 따라 url 상이
    # 넘겨받은 id에 해당하는 post의 디테일 페이지 표시
    path('delete_comment/<int:post_id>/<int:com_id>', views.delete_comment, name='delete_comment'),  
]
