from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Post, Project
from .forms import FeedbackForm
from django.core.mail import send_mail
from django.conf import settings

class BlogListView(ListView):
  model = Post
  template_name = "mainpage/index.html"
  context_object_name = 'posts'

  def get_context_data(self, *args, **kwargs):
    context = super().get_context_data(*args, **kwargs)
    context['default'] = Post.objects.filter(is_head=False, status=1)
    context['heading'] = Post.objects.filter(is_head=True, status=1)
    context['all_projects'] = Project.objects.filter(status=1)
    return context

  def feedback(self):
    if request.method == "POST":
      form = FeedbackForm(request.POST)
      if form.is_valid():
        form.save()
        name = form.cleaned_data.get('name')
        email = form.cleaned_data.get('email')
        send_mail(
          'Ваша заявка успешно отправлена команде Лаборатории',
          f'Здравствуйте, {name}.\n\nВаша заявка с заказом успешно отправлена нашей команде. \n\nВ ближайшее время мы свяжемся с вами!',
          settings.EMAIL_HOST_USER,
          [f'{email}'],
          fail_silently=False,
        )
        return redirect('blog')
    else:
      form = FeedbackForm()
    return render(request, "mainpage/index.html", {'form': form})

class BlogDetailView(DetailView):
    model = Post
    template_name = "mainpage/post-detail.html"


class ProjectDetailView(DetailView):
  model = Project
  template_name = "mainpage/project-detail.html"