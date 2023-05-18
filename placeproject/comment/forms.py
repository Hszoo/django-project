from django import forms
from .models import Comment

class CommentModelForm(forms.ModelForm) :
    class Meta:
            model = Comment
            fields = '__all__' # 모델 post에 정의된 필드 all 입력받음