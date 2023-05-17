from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Post(models.Model) :
    title = models.CharField(verbose_name='제목', max_length=50)
    writer = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(verbose_name='썸네일', null=True)
    content = models.TextField(verbose_name='내용')
    create_at = models.DateTimeField(verbose_name='작성일', auto_now_add=True)
    like_count = models.IntegerField(verbose_name='평점')
    category = models.TextField(verbose_name='분류', null=True)

# 댓글에 해당하는 model 정의 
class Comment(models.Model) : 
    content = models.TextField(verbose_name='내용')
    create_at = models.DateTimeField(verbose_name='작성일', auto_now_add=True)
    post = models.ForeignKey(to='Post', on_delete=models.CASCADE) 
    writer = models.ForeignKey(to=User, on_delete=models.CASCADE) 