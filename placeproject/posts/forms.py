from django import forms
from .models import Post, Comment

# 모델 post에 정의된 필드 all 입력받음
class PostModelForm(forms.ModelForm) :
    class Meta:
            model = Post
            fields = '__all__' 

class CommentModelForm(forms.ModelForm) :
    class Meta:
            model = Comment
            fields = ['comment']
