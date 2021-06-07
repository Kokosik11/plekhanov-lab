from users.models import Order
from django import forms
from .models import Feedback, Comment
from captcha.fields import ReCaptchaField

class FeedbackForm(forms.ModelForm):
  name = forms.CharField(label="Введите ваше имя", widget=forms.TextInput(attrs={'placeholder': 'Введите ваше имя'}))
  email = forms.EmailField(label="Введите ваш email", widget=forms.TextInput(attrs={'placeholder': 'Введите ваш email'}))
  phone = forms.CharField(label="Введите ваш номер телефона", widget=forms.TextInput(attrs={'placeholder': 'Введите ваш номер телефона'}))

  class Meta:
    model = Feedback
    fields = ['name', 'email', 'phone']

class CommentForm(forms.ModelForm):
  content = forms.CharField(widget=forms.Textarea(attrs={'rows': '3', 'cols': '70'}))
  class Meta:
    model = Comment
    fields = ('content',)

class OrderCreateForm(forms.ModelForm):
  commentary = forms.CharField(required=False, label='Комментарий', widget=forms.Textarea(attrs={'placeholder': 'Примечания к заказу'}))
  class Meta:
    model = Order
    fields = ('commentary', 'item',)