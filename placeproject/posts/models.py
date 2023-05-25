from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Post(models.Model) :
    title = models.CharField(verbose_name='제목', max_length=50)
    writer = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, blank=True)
    create_at = models.DateTimeField(verbose_name='작성일', auto_now_add=True)
    like_count = models.IntegerField(verbose_name='평점', null=True)
    photo = models.ImageField(verbose_name='썸네일', blank=True, null=True, upload_to='post_photo')
    content = models.TextField(verbose_name='내용')
    category = models.CharField(verbose_name='분류',  max_length=50, null=True)

    def __str__(self): 
        return self.title
    
# # 이건 나중에 이미지 여러개 선택하도록 할떄.. 쓸거임 
# class Photo(models.Model) :
#     post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
#     image = models.ImageField(upload_to='images/', blank=True, null=True)

# 댓글에 해당하는 model 정의 
class Comment(models.Model) : 
    comment = models.TextField(max_length=200, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    # post 객체를 참조해서 만들 컬럼 -> target_post 
    article = models.ForeignKey(Post, on_delete=models.CASCADE)
    
    def __str__(self): 
        return self.comment