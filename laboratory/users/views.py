from django.shortcuts import render, redirect
from django.views.generic import ListView
from .forms import UserRegistration
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

class RegisterView(ListView):
  model = User
  template_name = "users/registration.html"

  def get_context_data(self, *args, **kwargs):
    context = super().get_context_data(*args, **kwargs)
    context['form'] = UserRegistration()
    return context

  def post(self, request):
      form = UserRegistration(request.POST)
      if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        messages.success(request, f'Пользователь {username} успешно зарегистрирован')
        send_mail(
          'Ваша учетная запись на сайте Лаборатории успешно создана.',
          f'Здравствуйте, {username}.\n\nСпасибо за создание учетной записи на сайте Лаборатории. \n\nНапоминаем, что вы выбрали имя пользователя {username}. В своем профиле вы можете просмотреть ваши заказы, изменить ваши данные и прочее.\n\nДо скорой встречи.',
          settings.EMAIL_HOST_USER,
          [f'{email}'],
          fail_silently=False,
        )
        return redirect('blog')