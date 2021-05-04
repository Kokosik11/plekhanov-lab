from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

class BlogListView(ListView):
  model = Post
  template_name = "mainpage/index.html"
  context_object_name = 'posts'

  def get_context_data(self, *args, **kwargs):
    context = super().get_context_data(*args, **kwargs)
    context['default'] = Post.objects.filter(is_head=False, status=1)
    context['heading'] = Post.objects.filter(is_head=True, status=1)
    return context

class BlogDetailView(DetailView):
    model = Post
    template_name = 'mainpage/post-detail.html'