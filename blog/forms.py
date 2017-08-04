from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:                 # 모델 내부의 메타데이터
        model = Post
        fields = ('title', 'text',)