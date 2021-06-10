from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    # form을 만들기 위해 어떤 model이 쓰여야 하는지 파악
    # model = post
    class Meta:
        model = Post
        fields = ('title', 'text', )