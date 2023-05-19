from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Post(models.Model) :
    title = models.CharField(verbose_name='제목', max_length=50)
    writer = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, blank=True)
    create_at = models.DateTimeField(verbose_name='작성일', auto_now_add=True)
    like_count = models.IntegerField(verbose_name='평점', null=True)
    image = models.ImageField(verbose_name='썸네일', upload_to='', blank=True, null=True)
    content = models.TextField(verbose_name='내용')
    category = models.CharField(verbose_name='분류',  max_length=50, null=True)

# 이건 나중에 이미지 여러개 선택하도록 할떄.. 쓸거임 
class Photo(models.Model) :
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

# 댓글에 해당하는 model 정의 
class Comment(models.Model) : 
    content = models.TextField(verbose_name='내용')
    create_at = models.DateTimeField(verbose_name='작성일', auto_now_add=True)
    post = models.ForeignKey(to='Post', on_delete=models.CASCADE) 
    writer = models.ForeignKey(to=User, on_delete=models.CASCADE) 