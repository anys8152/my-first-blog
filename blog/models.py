from django.conf import settings
from django.db import models
from django.utils import timezone

# 객체 정의
class Post(models.Model):

    # 속성 정의
    # '속성' = '데이터 타입' 정의
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)


    # 함수/메소드 정의
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


# python manage.py makemigrations blog
# 데이터베이스에 반영할 수 있도록 마이크레이션 파일(migration file)을 준비
# 실제 데이터베이스에 모델 추가 반영