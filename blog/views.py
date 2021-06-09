from django.shortcuts import render

# post_list 함수 생성
def post_list(request):
    return render(request, 'blog/post_list.html', {})

# request를 넘겨받아 render 메소드를 호출
# 호춣하여 받은 return > blog/post_list.html 템플릿을 보여줌.