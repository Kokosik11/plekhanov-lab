from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class UserRegistration(UserCreationForm):
  username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Иван Иванов'}))
  email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Ваш email'}))
  password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': '6+ символов, 1 заглавная', 'class': 'input-password1'}))
  password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль еще раз'}))

  class Meta:
    model = User
    fields = ['email', 'username', 'password1', 'password2']

class UserAuthentication(AuthenticationForm):
  username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Иван Иванов'}))
  password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Введите свой пароль', 'class': 'input-password1'}))

  class Meta:
    model = User
    fields = ['username', 'password']
