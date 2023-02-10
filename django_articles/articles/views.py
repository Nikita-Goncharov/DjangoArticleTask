from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import Http404, JsonResponse
from django.contrib import messages
from django.core import serializers

from .forms import ArticleForm, LoginForm, RegisterForm, CommentForm
from .models import Article, Comment


def home(request):
    context = {}
    if request.method == 'POST':
            search_request = request.body.decode()
            print(search_request)
            filtered_articles = Article.objects.filter(title__contains=search_request) | Article.objects.filter(author__username__contains=search_request)
            filtered_articles = serializers.serialize('json', filtered_articles)
            return JsonResponse({'filtered_articles': filtered_articles})
    else:
        articles = Article.objects.all()
        context.update({'articles': articles})
    return render(request, 'articles/home.html', context=context)


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            if form.cleaned_data['password'] == form.cleaned_data['password_repeat']:
                name = form.cleaned_data['name']
                password = form.cleaned_data['password']

                try:
                    already_registred_user = get_object_or_404(User, username=name)
                    messages.error(request, 'User with this name already created')
                except Http404:
                    user = User.objects.create_user(username=name, password=password)
                    return redirect('login')
            else:
                messages.error(request, 'Password mismatch')
        else:
            messages.error(request, 'Form is not valid')

        return redirect('register')  # if error
    else:
        form = RegisterForm()
    return render(request, 'articles/register.html', context={'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            password = form.cleaned_data['password']

            user = authenticate(username=name, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'User not found')
        else:
            messages.error(request, 'Form is not valid')
        return redirect('login')  # if error
    else:
        form = LoginForm()
    return render(request, 'articles/login.html', context={'form': form})


@login_required
def logout_view(request):
    logout(request)
    return redirect('home')


def article_detail(request, pk):
    article = Article.objects.get(pk=pk)
    comments = Comment.objects.filter(article=article)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            body = form.cleaned_data['body']
            user = request.user

            comment = Comment(article=article, author=user, body=body)
            comment.save()
        else:
            messages.error(request, 'Form is not valid')
        return redirect('article_detail', pk)
    else:
        form = CommentForm()
    return render(request, 'articles/article_detail.html', context={'form': form, 'article': article, 'comments': comments})


@login_required
def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data['title']
            body = form.cleaned_data['body']
            user = request.user

            article = Article(title=title, author=user, body=body)
            article.save()
            return redirect('home')
        else:
            messages.error(request, 'Form is not valid')
        return redirect('create_article')
    else:
        form = ArticleForm()
    return render(request, 'articles/create_article.html', context={'form': form})