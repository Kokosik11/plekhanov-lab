from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Profile

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

class UserProfile(forms.ModelForm):
  email = forms.EmailField(widget=forms.TextInput)

  class Meta:
    model = User
    fields = ['username', 'last_name', 'first_name', 'email']

class ProfileImage(forms.ModelForm):
  birthdate = forms.DateField(widget = forms.SelectDateWidget(years=range(1930, 2021)))

  def __init__(self, *args, **kwards):
    super(ProfileImage, self).__init__(*args, **kwards)
    self.fields['image'].label = 'Изображение'
    self.fields['phone'].label = 'Ваш номер телефона'
    self.fields['birthdate'].label = 'Дата рождения'
    
  class Meta:
    model = Profile
    fields = ['image', 'phone', 'birthdate']