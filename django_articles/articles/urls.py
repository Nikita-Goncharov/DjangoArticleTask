from . import views

from django.urls import path


urlpatterns = [
    path("", views.home, name="home"),
    path("create_article/", views.create_article, name="create_article"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register_view, name="register"),
]