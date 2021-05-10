from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Post, Project
from .forms import FeedbackForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

class BlogListView(ListView):
  model = Post
  template_name = "mainpage/index.html"
  context_object_name = 'posts'

  def get_context_data(self, *args, **kwargs):
    context = super().get_context_data(*args, **kwargs)
    context['default'] = Post.objects.filter(is_head=False, status=1)
    context['heading'] = Post.objects.filter(is_head=True, status=1)
    context['all_projects'] = Project.objects.filter(status=1)
    context['form'] = FeedbackForm()
    return context

  def post(self, request):
    form = FeedbackForm(request.POST)
    if form.is_valid():
      feedback = form.save()
      name = form.cleaned_data.get('name')
      email = form.cleaned_data.get('email')
      phone = form.cleaned_data.get('phone')
      num = feedback.uuid
      messages.add_message(request, messages.INFO, f'Спасибо за оставленную заявку, {name}!')
      send_mail(
        'Ваша заявка успешно добавлена.',
        f'Здравствуйте, {name}.\n\nВаша заявка № {num} успешно зарегистрирована. \n\nВ скором времени наша команда свяжется с вами по номеру {phone}.',
        settings.EMAIL_HOST_USER,
        [f'{email}'],
        fail_silently=False,
      )
      return redirect('blog')
    else:
      form = FeedbackForm()

class BlogDetailView(DetailView):
    model = Post
    template_name = "mainpage/post-detail.html"


class ProjectDetailView(DetailView):
  model = Project
  template_name = "mainpage/project-detail.html"