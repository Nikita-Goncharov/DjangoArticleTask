from django import forms


class ArticleForm(forms.Form):
    title = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form_article_title'}))
    body = forms.CharField(widget=forms.Textarea(attrs={'class': 'form_article_body'}))


class LoginForm(forms.Form):
    name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': ''}))
    password = forms.CharField(widget=forms.PasswordInput())


class RegisterForm(forms.Form):
    name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': ''}))
    password = forms.CharField(widget=forms.PasswordInput())
    password_repeat = forms.CharField(widget=forms.PasswordInput())


class CommentForm(forms.Form):
    body = forms.CharField(widget=forms.Textarea(attrs={'class': ''}))


class SearchForm(forms.Form):
    field = forms.CharField(max_length=200)