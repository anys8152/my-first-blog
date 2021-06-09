from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]
    # <int:pk> : 정수 값을 받고 이를 'pk'라는 변수로 뷰에 전송하는 것
    # post/'정수값'/ --> post_detail이 '정수값'인 것을 찾아 뷰로 전달함.