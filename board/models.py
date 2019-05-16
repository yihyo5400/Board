from django.db import models
from datetime import datetime

# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    update_date = models.DateTimeField(auto_now=True) #현재시각
    #created_at = models.DateTimeField(auto_now_add=True) # 해당 레코드 생성시 현재 시간 자동저장

    def now():
        return datetime.datetime

    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:50]