from django.db import models

# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    update_date = models.DateTimeField(auto_now=True) # 글쓴 시간 + 수정된 시간 저장
    #created_at = models.DateTimeField(auto_now_add=True) # 글쓴 시간 자동저장


    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:50]