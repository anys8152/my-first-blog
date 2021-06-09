from django.shortcuts import render
from .models import Post
from django.utils import timezone


# post_list 함수 생성
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

# request를 넘겨받아 render 메소드를 호출
# 호출하여 받은 return > blog/post_list.html 템플릿을 보여줌.

