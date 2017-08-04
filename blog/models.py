from django.db import models
from django.utils import timezone

class Post(models.Model):                       # Post 모델 정의
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):      # 제목반환 함수
        return self.title
    



# 모델을 저장하면 그 내용이 데이터베이스에 저장