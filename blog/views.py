from django.shortcuts import render
from .models import Post
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect

# pk를 식별하기위한 뷰에 매개변수 pk 추가
# Post.objects.get(pk=pk)

# post_list 함수 생성
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    # post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_list.html', {'posts': posts})
# request를 넘겨받아 render 메소드를 호출
# 호출하여 받은 return > blog/post_list.html 템플릿을 보여줌.


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post':post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form' : form})
# url로 부터 추가로 pk 매개변수를 받아서 처리
# get_object_or_404(Post, pk=pk) 를 호출하여 수정하고자하는 글의 Post 모델 인스턴스로 가져옴.
# 가져온 데이터를 폼을 만들때, 저장할때 사용






