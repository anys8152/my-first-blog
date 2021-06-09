from django.shortcuts import render
from .models import Post
from django.utils import timezone
from django.shortcuts import render, get_object_or_404


# pk를 식별하기위한 뷰에 매개변수 pk 추가
# Post.objects.get(pk=pk)

# post_list 함수 생성
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    # post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post':post})
# request를 넘겨받아 render 메소드를 호출
# 호출하여 받은 return > blog/post_list.html 템플릿을 보여줌.

