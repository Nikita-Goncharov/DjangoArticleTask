from django import forms


class ArticleForm(forms.Form):
    title = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form_article_title', 'placeholder': 'Title'}))
    body = forms.CharField(widget=forms.Textarea(attrs={'class': 'form_article_body', 'placeholder': 'Your text'}))


class LoginForm(forms.Form):
    name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form_name', 'placeholder': 'Name'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form_password', 'placeholder': 'Password'}))


class RegisterForm(forms.Form):
    name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form_name', 'placeholder': 'Name'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form_password', 'placeholder': 'Password'}))
    password_repeat = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form_password_repeat', 'placeholder': 'Repeat password'}))


class CommentForm(forms.Form):
    body = forms.CharField(widget=forms.Textarea(attrs={'class': 'comment_body', 'placeholder': 'Leave your comment'}))


class SearchForm(forms.Form):
    field = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'search_field', 'placeholder': 'Search by title or by author'}))