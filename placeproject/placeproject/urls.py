from django.contrib import admin
from django.conf import settings # settings 파일에 있는 값들을 가져올 수 있음 
from django.conf.urls.static import static 
from django.urls import path, include
import home.views # 시작 앱 
import posts.views # views에 정의된 create 함수 이용하기 위해 import 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home.views.home, name='home'), #시작앱 : home
    path('comment/', include('comment.urls')),
    path('posts/', include('posts.urls')), 
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)