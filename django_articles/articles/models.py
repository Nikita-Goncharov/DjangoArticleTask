from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, db_column='username', on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add=True)
    body = models.TextField()


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author = models.ForeignKey(User, db_column='username', on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add=True)
    body = models.TextField()
