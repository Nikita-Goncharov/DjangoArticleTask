from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, db_column='username', on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add=True)
    body = models.TextField()

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author = models.ForeignKey(User, db_column='username', on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add=True)
    body = models.TextField()

    def __str__(self):
        return f'{self.author}-{self.body if len(self.body) < 50 else self.body[:50] + "..."}'