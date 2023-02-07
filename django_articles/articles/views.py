from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

from .forms import ArticleForm, LoginForm, RegisterForm
from .models import Article


def home(request):
    articles = Article.objects.all()
    return render(request, 'articles/home.html', context={'articles': articles})


def register(request):
    form = RegisterForm()
    return render(request, 'articles/register.html', context={'form': form})


def login(request):
    form = LoginForm()
    return render(request, 'articles/login.html', context={'form': form})


@login_required
def logout(request):
    logout(request)
    return redirect('home')


@login_required
def create_article(request):
    form = ArticleForm()
    return render(request, 'articles/create_article.html', context={'form': form})