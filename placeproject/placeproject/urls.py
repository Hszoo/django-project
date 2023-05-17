from django.contrib import admin
from django.urls import path, include
import home.views # 시작 앱 
import posts.views # views에 정의된 create 함수 이용하기 위해 import 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home.views.home, name='home'), #시작앱 : home
    path('comment/', include('comment.urls')),
    path('posts/', include('posts.urls')), 
]
