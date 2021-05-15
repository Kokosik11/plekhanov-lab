from django.shortcuts import render, redirect
from django.views.generic import ListView, UpdateView
from .forms import UserRegistration, UserProfile, ProfileImage
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class RegisterView(ListView):
  model = User
  template_name = "users/registration.html"

  def get_context_data(self, *args, **kwargs):
    context = super().get_context_data(*args, **kwargs)
    context['form'] = UserRegistration()
    return context

  def post(self, request):
    if request.method == "POST":
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
        return redirect('login')
    else:
      form = UserRegistration()
    return render(request, 'users/registration.html', {'form': form})

@login_required
def profile(request):
    if request.method == "POST":
        img_profile = ProfileImage(
            request.POST, request.FILES, instance=request.user.profile)
        update_user = UserProfile(request.POST, instance=request.user)

        if update_user.is_valid() and img_profile.is_valid():
            update_user.save()
            img_profile.save()
            messages.success(request, f'Информация была успешно обновлена')
            return redirect('profile')
    else:
        img_profile = ProfileImage(instance=request.user.profile)
        update_user = UserProfile(instance=request.user)

    data = {
        'img_profile': img_profile,
        'update_user': update_user,
    }

    return render(request, 'users/profile.html', data)