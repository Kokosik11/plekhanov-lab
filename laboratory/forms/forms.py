from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
  class Meta:
    model = Feedback
    fields = ('first_name', 'email', 'phone',)
    widgets = {
      'first_name': forms.TextInput(attrs={'placeholder': 'Введите ваше имя'}),
      'email': forms.TextInput(attrs={'placeholder': 'Введите ваш email'}),
      'phone': forms.TextInput(attrs={'placeholder': 'Введите ваш номер телефона'}),
    }