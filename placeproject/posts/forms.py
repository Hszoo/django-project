from django import forms
from .models import Post

class PostModelForm(forms.ModelForm) :
    class Meta:
            model = Post
            fields = '__all__' # 모델 post에 정의된 필드 all 입력받음