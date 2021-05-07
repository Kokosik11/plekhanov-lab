from django import forms
from .models import Feedback
from captcha.fields import ReCaptchaField

class FeedbackForm(forms.ModelForm):
  name = forms.CharField(label="Введите ваше имя", widget=forms.TextInput(attrs={'placeholder': 'Введите ваше имя'}))
  email = forms.EmailField(label="Введите ваш email", widget=forms.TextInput(attrs={'placeholder': 'Введите ваш email'}))
  phone = forms.CharField(label="Введите ваш номер телефона", widget=forms.TextInput(attrs={'placeholder': 'Введите ваш номер телефона'}))

  class Meta:
    model = Feedback
    fields = ['name', 'email', 'phone']