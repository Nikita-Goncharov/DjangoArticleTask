from django.contrib import admin

from .models import Article, Comment


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_date', 'body')
    list_filter = ('author', 'created_date')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('article', 'author', 'created_date', 'body')
    list_filter = ('author', 'created_date')


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
