from django.contrib import admin
from .models import Post

# 관리자 페이지에서 모델 확인하기
admin.site.register(Post)
