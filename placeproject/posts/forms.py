from django import forms
from .models import Post

# 모델 post에 정의된 필드 all 입력받음
class PostModelForm(forms.ModelForm) :
    class Meta:
            model = Post
            fields = '__all__' 