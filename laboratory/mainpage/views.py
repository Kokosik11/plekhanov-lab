from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from .models import Post, Project, Comment
from .forms import FeedbackForm, CommentForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from taggit.models import Tag
from django.template.defaultfilters import slugify

def mainpage(request):
  posts = Post.objects.filter(is_head=False, status=1).order_by('-created_on')
  heading = Post.objects.filter(is_head=True, status=1)
  all_projects = Project.objects.filter(status=1)
  form = FeedbackForm(request.POST)
  common_tags = Post.tags.most_common()[:4]
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

  context = {
      'posts': posts,
      'heading': heading,
      'all_projects': all_projects,
      'form': form,
      'common_tags': common_tags,
  }
  
  return render(request, 'mainpage/index.html', context)

def posts(request):
  posts = Post.objects.filter(is_head=False, status=1).order_by('-created_on')

  context = {
    'posts': posts,
  }

  return render(request, 'mainpage/posts.html', context)


def tagged(request, slug):
  tag = get_object_or_404(Tag, slug=slug)
  posts = Post.objects.filter(tags=tag)
  context = {
    'tag': tag,
    'posts': posts,
  }
  return render(request, 'mainpage/posts.html', context)

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, status=1)
    comments = Comment.objects.filter(post=post, reply=None).order_by('-id')
    post_object = Post.objects.get(slug=slug)
    post_object.views = post_object.views + 1
    post_object.save()

    if request.method == 'POST':
      comment_form = CommentForm(request.POST or None)
      if comment_form.is_valid():
        content = request.POST.get('content')
        comment_qs = None
        comment = Comment.objects.create(post=post, user=request.user, content=content)
        comment.save()
        # return HttpResponseRedirect(post.get_absolute_url())
    else:
      comment_form = CommentForm()

    context = {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
    }

    if request.is_ajax():
      html = render_to_string('mainpage/comments.html', context, request=request)
      return JsonResponse({'form': html})

    return render(request, 'mainpage/post-detail.html', context)


class ProjectDetailView(DetailView):
  model = Project
  template_name = "mainpage/project-detail.html"