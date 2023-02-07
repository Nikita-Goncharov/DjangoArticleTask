from . import views

from django.urls import path


urlpatterns = [
    path("", views.home, name="home"),
    path("create_article/", views.create_article, name="create_article"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("register/", views.register, name="register"),
]