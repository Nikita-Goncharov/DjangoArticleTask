from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import Http404
from django.contrib import messages

from .forms import ArticleForm, LoginForm, RegisterForm, SearchForm
from .models import Article


def home(request):
    form = SearchForm()
    articles = Article.objects.all()

    # ar = Article(title='dfhbgdiv', author=u, body='dsfsgd')
    # ar.save()
    return render(request, 'articles/home.html', context={'articles': articles, 'form': form})


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
                    return redirect('register')
                except Http404:
                    user = User.objects.create_user(username=name, password=password)
                    return redirect('login')
            else:
                messages.error(request, 'Password mismatch')
                return redirect('register')
        else:
            messages.error(request, 'Form is not valid')
            return redirect('register')
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
                return redirect('login')
        else:
            messages.error(request, 'Form is not valid')
            return redirect('login')
    else:
        form = LoginForm()
    return render(request, 'articles/login.html', context={'form': form})


@login_required
def logout_view(request):
    logout(request)
    return redirect('home')


@login_required
def create_article(request):
    form = ArticleForm()
    if request.method == 'POST':
        pass
    return render(request, 'articles/create_article.html', context={'form': form})